---
name: slop-proofcheck
description: Use when a draft explanation, walkthrough, lesson, tutorial, README, or technical document has been written and needs a final pass before it is handed over - or when the user says it "sounds like AI", "sounds generic", "reads like ChatGPT", asks to make it "sound human", "less robotic", "more authentic", or asks for a proofread, polish, slop check, or voice check. Also use when reviewing the user's own prose for filler, padding, hype, or vague claims.
metadata:
  version: "1.0.0"
  scope: prose-register-review
  companion: learning-walkthrough
  derived-from: https://github.com/petergyang/no-ai-slop
---

# Slop Proofcheck

A final pass over finished prose that strips the tells of machine-written text without flattening the document into generic polish.

The pattern catalogue is derived from [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang (MIT), re-scoped for explanatory and teaching prose. See `references/slop-patterns.md` for what was kept, narrowed, dropped, and added, and why.

This is a **review** skill, not a writing skill. It runs after a draft exists. It never restructures the document, never changes the maths, and never touches a verified number.

## Activation

Run this pass when:

- A `learning-walkthrough` document has been written and is about to be handed to the learner.
- The user says something reads as AI-generated, generic, robotic, corporate, or padded.
- The user asks for a proofread, a polish, or a "make this sound like a person" pass.
- Any explanatory document - tutorial, README, lesson, notebook markdown, design doc - is finished and being reviewed.

Do not run it on a draft that is still being written; padding is easier to spot once the argument has stopped moving. Do not run it on the user's own source notes unless they ask - their notes are theirs.

## The Register

Generic anti-slop advice is written for personal essays, where the job is to preserve a writer's voice. An explanation has no author voice to preserve, so protecting one is not the goal here. The target instead is a **specific register**:

> A competent person explaining something to one other person, in a room, without wanting anything from them.

That register has properties worth naming, because each one maps to a class of slop:

| Property | What it rules out |
|---|---|
| Says what happened, not how to feel about it | Puffery, hype, "this is huge" |
| Never performs expertise | Faux-insight setups, "what nobody tells you" |
| Never performs enthusiasm | Cheerleading, "great question!", exclamation marks |
| Names one thing one way | Synonym cycling |
| Would not say it about anything else | Portable filler |
| Does not tell you a thing is obvious | Condescension markers |
| Stops when finished | Recap endings, fake-profound kickers |

When a judgment call is genuinely close, read the sentence aloud in that voice. Slop is audible.

## The Two Gates

**Gate 1 - mechanical.** Run the script. It catches the vocabulary and phrase-level tells, which are not judgment calls:

```bash
python skills/slop-proofcheck/scripts/check_slop.py <file.md>
```

`cut:` hits are failures - fix every one. `check:` hits are candidates that have legitimate technical uses; confirm each one is the technical sense and move on.

**The house dash rule.** No em dashes (`U+2014`), no en dashes (`U+2013`), anywhere, ever. Replace every one with a plain hyphen `-`, or restructure the sentence around a comma, colon, brackets, or a full stop. This is stricter than correct typography on purpose: the em dash now reads as a machine-writing tell, and that costs more than the typographic nicety is worth. It is a `cut:` hit, not a judgment call. See §2.13.

**Gate 2 - judgment.** Read `references/slop-patterns.md` and pass the draft against the catalogue. The script cannot see a portable sentence, a stacked analogy, or a restatement wearing an explanation's clothes.

## The Prime Test

One test does more work than the whole catalogue:

> **Substitute a different subject into the sentence. Is it still true?**

"Entropy is a fundamental concept that plays a crucial role in machine learning" survives substitution of *any* concept - so it says nothing. Cut it, or replace it with the fact it was standing in front of: "Entropy is the number a tree uses to rank candidate splits."

Apply it to every sentence that contains no number, no name, no mechanism, and no consequence.

## What This Pass Must Not Do

These are the failure modes of an over-eager proofread. They cost more than the slop would have.

- **Never touch a verified number, a formula, or a derivation step.** The arithmetic gate outranks every rule in this skill. If a fix would change a value, stop and leave it.
- **Never flag repeated section structure.** A walkthrough repeats its concept-section shape on purpose. Predictable structure is the feature. Sentence-level monotony inside one paragraph is fair game; the document skeleton is not.
- **Never flag short sections, tables, bullet lists, or callouts.** The structure contract requires them. Essay formatting rules do not apply to a study document.
- **Never cut a genuine discrimination to kill a rhetorical pattern.** "Entropy is not variance: variance measures spread around a mean, entropy measures uncertainty over categories" is a contrast that names a real difference and earns its place. "It's not about the formula. It's about the intuition." is rhythm with no content. Keep the first, cut the second.
- **Never cut navigational signposting.** "We use this in section 4" points at a place. "This distinction matters" asserts importance without cashing it. Keep pointers, cut assertions.
- **Never sand off plain bluntness.** "Entropy is never negative. If you got a negative number, you dropped the minus sign." is direct and correct. Do not soften it into hedged prose.
- **Never compress to hit a length target.** Length is not a cost in a walkthrough. The goal is removing padding, not removing words.

## Output

Report as a list, one line per finding, with the line number, the quoted phrase, and the fix:

```
L142  "plays a crucial role in"        → puffery; state what it does
L207  "Simply substitute the values"   → condescension; cut "simply"
L311  "feature / attribute / variable" → synonym cycling; pick one, alias the rest in the toolbox
```

Then apply the fixes and state what changed. If the draft is clean, say so plainly and stop - do not invent findings to justify the pass.

When the user asked only "is this slop?", report the findings and stop. Do not rewrite unless asked.
