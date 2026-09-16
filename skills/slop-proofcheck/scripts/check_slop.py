#!/usr/bin/env python3
"""Flag AI-slop vocabulary and phrasing in a finished draft.

Usage: python check_slop.py <file.md> [...]
Exit 0 if no `cut:` hits, 1 otherwise. `check:` hits are for review, not failures.

Skips frontmatter, code fences, maths and link targets, so formulas and
variable names are never flagged. Long dashes are the one rule checked against
the raw line, since they are banned everywhere. See references/slop-patterns.md.
"""
import re
import sys

# No technical sense in an explanation. Always wrong.
CUT_WORDS = """delve foster utilize utilise facilitate empower streamline
paramount multifaceted meticulous intricate transformative elevate embark
supercharge seamless unleash unlock revolutionize revolutionise tapestry
realm beacon testament""".split()

# Hype in prose, defined terms in the domain. Confirm the sense, then move on.
CHECK_WORDS = """leverage robust robustness harness significant significantly
optimal optimize optimise optimized optimised normalize normalise critical
landscape trivial trivially clearly simply essentially basically""".split()

CUT_PHRASES = [
    (r"it'?s worth noting", "throat-clearing"),
    (r"it'?s important to note", "throat-clearing"),
    (r"needless to say|goes without saying", "throat-clearing"),
    (r"let'?s (dive in|unpack|break (it|this) down)", "throat-clearing"),
    (r"here'?s the thing|let me be clear", "throat-clearing"),
    (r"at the end of the day|in today'?s world|in the age of", "filler"),
    (r"recall that|as we know|as you'?ll remember", "nobody recalls - restate it"),
    (r"what if i told you|plot twist|think about it:", "rhetorical setup"),
    (r"here'?s what nobody tells you|the part everyone misses", "faux-insight"),
    (r"what most people get wrong|most people skip", "faux-insight"),
    (r"the key (point|insight|takeaway) is", "metadiscourse"),
    (r"in conclusion|to summari[sz]e", "recap ending"),
    (r"studies show|experts agree|research suggests", "weasel attribution"),
    (r"it is widely (regarded|believed|accepted)", "weasel attribution"),
    (r"plays? an? (vital|crucial|key|pivotal|important) role", "puffery"),
    (r"a testament to|marks? a pivotal|cornerstone of", "puffery"),
    (r"powerful tool|game.?changer|paradigm shift", "puffery"),
    (r"it can be shown that|after some algebra", "magic step - show it or scope it out"),
    (r"one can (easily )?verify|easy to see", "magic step - show it or scope it out"),
    (r", (highlighting|underscoring|showcasing|reflecting) (the|its|how)",
     "superficial analysis - give the consequence"),
    (r"great question|don'?t worry|you'?ve got this", "cheerleading"),
    (r"that'?s all there is to it|not so bad", "cheerleading"),
    (r"of course,|\bit'?s not just\b", "condescension / binary contrast"),
    (r"in this section,? we('?ll| will)", "hollow opener - start on the problem"),
    (r"cutting.edge|ever.evolving|deep dive", "hype"),
    # Author asserting obviousness. "looks obviously wrong" describes the
    # learner's perception and is fine, so only flag the assertive forms.
    (r"obviously,|(?:^|[.;:]\s*)obviously\b", "condescension - give the reason instead"),
]

CHECK_PHRASES = [
    (r"in other words|put simply|to put it another way", "restatement - add an anchor or cut"),
    (r"it follows that|it can be seen", "magic step unless the step is shown"),
    (r"this (distinction |difference )?matters", "metadiscourse unless it says why"),
    (r"as you can see|importantly,|notably,", "metadiscourse unless a fact follows"),
]

EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿]")

# House style: no long dashes anywhere. Written as chr() so a find-and-replace
# sweep over the repo can never silently turn these into plain hyphens.
LONG_DASHES = {chr(0x2014): "em dash", chr(0x2013): "en dash"}


def compile_words(words):
    return re.compile(r"\b(" + "|".join(words) + r")\b", re.I)


CUT_W, CHECK_W = compile_words(CUT_WORDS), compile_words(CHECK_WORDS)
CUT_P = [(re.compile(p, re.I), note) for p, note in CUT_PHRASES]
CHECK_P = [(re.compile(p, re.I), note) for p, note in CHECK_PHRASES]


def strip(line):
    """Remove everything that is not prose: maths, code, links, callout tags."""
    line = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", " ", line)   # maths
    line = re.sub(r"`[^`]*`", " ", line)                     # code spans
    line = re.sub(r"\[\[[^\]]*\]\]", " ", line)              # wikilinks
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)     # links, keep the text
    line = re.sub(r"\[!\w+\]-?", " ", line)                  # callout tags
    return line


def check(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    issues, in_fence, in_display, in_meta = [], False, False, False

    for n, line in enumerate(lines, 1):
        if line.strip() == "---" and n == 1:
            in_meta = True
            continue
        if in_meta:
            in_meta = line.strip() != "---"
            continue
        if line.lstrip("> ").startswith("```"):
            in_fence = not in_fence
            continue
        if line.lstrip("> ").strip() == "$$":
            in_display = not in_display
            continue
        if in_fence or in_display:
            continue

        body = strip(line)

        for m in CUT_W.finditer(body):
            issues.append((n, "cut", m.group(0), "hype with a plain replacement"))
        for rx, note in CUT_P:
            for m in rx.finditer(body):
                issues.append((n, "cut", m.group(0).strip(), note))
        for m in CHECK_W.finditer(body):
            issues.append((n, "check", m.group(0), "hype, or the technical term?"))
        for rx, note in CHECK_P:
            for m in rx.finditer(body):
                issues.append((n, "check", m.group(0).strip(), note))
        if EMOJI.search(body):
            issues.append((n, "check", EMOJI.search(body).group(0), "emoji in a study document"))
        # Checked against the raw line, not the stripped body: a long dash in a
        # heading or a link text is still a long dash.
        for d, name in LONG_DASHES.items():
            if d in line:
                issues.append((n, "cut", d, f"{name} - house style is a plain hyphen"))

    for n, tier, hit, note in issues:
        print(f"{path}:{n}: {tier}: {hit!r} - {note}")
    return not [i for i in issues if i[1] == "cut"]


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit("usage: check_slop.py <file.md> [...]")
    ok = all([check(f) for f in files])
    print("clean" if ok else "cut: hits found")
    sys.exit(0 if ok else 1)
