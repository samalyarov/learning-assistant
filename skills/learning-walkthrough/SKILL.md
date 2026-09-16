---
name: learning-walkthrough
description: Use when the user is learning something and asks to have it explained, walked through, taught, or broken down - course lessons, lecture notes, textbook chapters, papers, formulas, or a notebook they cannot follow. Triggers on "explain this to me", "I don't understand this", "the lecturer didn't explain", "walk me through", "explain like I'm new to this", "I'm not good at math", "explain it like you did before", or a request for a study walkthrough, cheat sheet, or worked examples the user can do by hand.
metadata:
  version: "1.0.0"
  scope: study-walkthrough-authoring
  reference: https://doi.org/10.1177/1529100612453266
---

# Learning Walkthrough

Use this skill to turn course material a learner does not yet understand into a walkthrough they can actually study from: a standalone document that builds every idea from the ground up, names every symbol before using it, and carries small worked examples the learner can reproduce by hand on paper.

The useful output is not a summary. A summary compresses material for someone who already understands it. A walkthrough expands material for someone who does not. If the document is shorter than the source notes, it is the wrong artifact.

## Activation

Use when the user asks to explain, teach, unpack, or walk through:

- A lesson, lecture, or course module, with or without their own notes.
- Lecture slides, official PDF notes, a textbook chapter, or a paper.
- A Jupyter notebook whose code or math they do not follow.
- A formula, derivation, algorithm, or method they cannot read.
- Anything phrased as "explain it like you did last time" for a previous lesson.

Also use when the user says they are studying, taking a course, or preparing for an exam and wants material made understandable.

Do not use for ordinary code review, for writing production code, for reference lookups where the user already understands the topic and just needs a fact, or for tasks where the user has asked for a short answer.

## The Learner Contract

Unless the user says otherwise, these are the standing assumptions. Do not renegotiate them per request; do not ask permission to be thorough.

- **The learner is a beginner in the underlying math.** Build from the ground up. "Recall that" and "as we know" are banned openings - nobody recalls.
- **Thorough is the default.** Length is not a cost here. Only compress when the user explicitly asks for a short version.
- **The learner works by hand.** They will copy the document onto paper, redraw the diagrams, and redo the arithmetic with a pen. Every example must survive that.
- **Nothing is invented.** Every non-obvious claim traces to a real source (see `references/sourcing-and-rigor.md`).
- **Output is a file**, not chat prose. A walkthrough is a study artifact the learner returns to.
- **The file lands in Obsidian.** All maths is LaTeX, and the whole document must paste into an Obsidian vault and render correctly with zero cleanup (see `references/obsidian-output.md`).

## Mandatory First Step

Read the whole evidence base before writing a single line of explanation. Do not start from the user's notes alone - notes are a compressed record of a lesson, and the gaps in them are exactly what needs explaining.

1. **Inventory the sources.** The user's own notes, official PDFs or slides, notebooks, linked articles and papers, textbook sections. Read them fully, not by skimming headers.
2. **List every concept** the lesson touches, including ones the notes only name in passing.
3. **List every symbol, operator, and piece of notation** that appears anywhere in the material. This becomes the math toolbox (`references/math-toolbox.md`).
4. **Find the gaps.** Where do the notes assert something without deriving it? Where does the lecturer skip a step? Those gaps are the walkthrough's real work.
5. **Read the cited sources** the notes link to, then research beyond them to substantiate and check (`references/sourcing-and-rigor.md`).

State the source inventory at the top of the finished walkthrough so the learner knows what it is built from.

## Non-Negotiables

These seven hold in every walkthrough, in every output format.

1. **Math toolbox first.** Before any concept section, a prerequisites section that defines every symbol and operation the document will use, with a tiny numeric example for each. The learner should never meet an unexplained symbol in the body.
2. **Every symbol named at its formula.** When a formula appears, immediately below it name each symbol, say it out loud in words, and give its units or type. A formula with unnamed parts is not an explanation.
3. **The arithmetic gate.** Every number in every worked example is computed and verified before it is written down - run it in a script, do not eyeball it. One wrong intermediate value destroys a learner's trust in the whole document and wastes an hour of their paper time. This gate is not optional and not skippable under time pressure.
4. **Hand-scale examples.** Small integers, tiny datasets, clean denominators, logs of powers of two. Every step shown, one operation per line, arithmetic written out. See `references/worked-examples.md`.
5. **Real sources, honest status.** Cite what exists; never fabricate a reference. Where a claim has been superseded, contested, or failed to replicate, say so at the point it is used.
6. **LaTeX maths, Obsidian-ready.** Every formula is LaTeX - inline `$...$`, display `$$...$$` - and the document uses Obsidian conventions throughout: YAML frontmatter, callouts, collapsed answers, wikilinks. After saving, run `"${CLAUDE_PLUGIN_ROOT}/skills/learning-walkthrough/scripts/check_obsidian.py"` against the file and fix every hit (if that variable is unset, the skill was not installed as a plugin - use this skill's own `scripts/check_obsidian.py`). A formula that does not render is a formula the learner cannot copy onto paper.
7. **Plain register, plain hyphens.** No hype, no puffery, no cheerleading, no "obviously". No em dashes or en dashes anywhere - use a plain hyphen `-`, or restructure the sentence. A walkthrough explains; it never sells, and it never tells the learner that something is easy. Thorough means more *explanation*, never more words - the expansion mandate above is exactly where padding creeps in, so the length budget buys derivation steps, symbol tables, and examples, not adjectives. Before handing the file over, run the `slop-proofcheck` skill.

## Depth Dial

Thoroughness is the default, but depth is allocated, not sprayed evenly. Spend the most words where the learner is most likely to stall:

| Material | Depth |
|---|---|
| A formula with more than two symbols | Full: derivation, symbol table, worked example, your-turn problem |
| A named method or algorithm | Full, plus what it is competing against and when it fails |
| A definition the learner already met last lesson | One-line refresher plus a pointer back |
| A historical or contextual aside | One paragraph, clearly marked as optional |

## Reference Routing

- Load `references/walkthrough-structure.md` before writing - it carries the section-by-section output contract. Always.
- Load `references/obsidian-output.md` before writing - LaTeX and Obsidian rendering rules. Always.
- Load `references/math-toolbox.md` when building the prerequisites section.
- Load `references/worked-examples.md` when designing any example, exercise, or number.
- Load `references/sourcing-and-rigor.md` when researching, citing, or flagging a contested claim.
- Load `references/notebook-mode.md` when the deliverable is a Jupyter notebook rather than a markdown document.
- Load `references/learning-science.md` when the user asks why the walkthrough is shaped this way, or when adapting the format for a new kind of material.
- Use the `slop-proofcheck` skill as the last step before handing over, and whenever the user says a draft reads as generic or AI-written. It runs after the document is finished; it never restructures it and never touches a verified number.

## Default Output

A single standalone Obsidian-ready markdown file, per the contract in `references/walkthrough-structure.md`.

- **Name it** for the lesson: `lesson-07-walkthrough.md`, or `<topic>-walkthrough.md` when there is no lesson number. Save it beside the source notes.
- **Obsidian-ready by default.** YAML frontmatter, LaTeX maths, callouts, collapsed answers. The learner drops it into their vault unmodified.
- **Standalone.** The learner should be able to open it a month later, with the source notes closed, and still follow it.
- **Do not modify the user's own notes** unless they ask. The walkthrough is a new file next to them.
- **Notebook deliverables** follow `references/notebook-mode.md` instead: explanation lives in markdown cells, and the user's code cells are left alone unless they ask. The same LaTeX conventions apply.

Report at the end: the file path written, which sources it was built from, that both the render check and the slop proofcheck ran clean, and any point where the source material and the wider literature disagree.
