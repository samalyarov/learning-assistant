#!/usr/bin/env python3
"""Check a walkthrough for the four Obsidian rendering traps.

Usage: python check_obsidian.py <file.md> [...]
Exit 0 if clean, 1 if any issue found. See references/obsidian-output.md.
"""
import re
import sys

INLINE = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)")


def check(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    issues, in_fence, in_display = [], False, False

    for n, line in enumerate(lines, 1):
        if line.lstrip("> ").startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        body = line.lstrip("> ") if line.startswith(">") else line

        # 3. display $$ needs a blank line before it (outside callouts)
        if body.strip() == "$$" and not line.startswith(">"):
            if not in_display and n > 1 and lines[n - 2].strip() not in ("", "$$"):
                issues.append((n, "display $$ with no blank line before it"))
            in_display = not in_display
            continue
        if in_display:
            continue

        # 1. inline math with whitespace before the closing $
        for m in INLINE.finditer(body):
            if m.group(1) != m.group(1).rstrip():
                issues.append((n, f"space before closing $: ${m.group(1)}$"))

        # 2. raw | inside math inside a table row
        if body.count("|") > 1 and body.strip().startswith("|"):
            for m in INLINE.finditer(body.replace("|", "\x00")):
                if "\x00" in m.group(1):
                    issues.append((n, "raw | inside math in a table - use \\mid or \\vert"))

        # 4. callout continuation missing the '> ' prefix
        if re.match(r"^> \[!\w+\]", line):
            nxt = lines[n] if n < len(lines) else ""
            if nxt.strip() and not nxt.startswith(">"):
                issues.append((n + 1, "callout continuation missing '> ' prefix"))

    for n, msg in issues:
        print(f"{path}:{n}: {msg}")
    return not issues


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit("usage: check_obsidian.py <file.md> [...]")
    ok = all([check(f) for f in files])
    print("clean" if ok else "issues found")
    sys.exit(0 if ok else 1)
