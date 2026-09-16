# Walkthrough Structure

The output contract. A walkthrough is these sections, in this order. Fill every one that applies; skip a section only when the lesson genuinely has nothing for it, and never reorder.

The document targets an Obsidian vault: YAML frontmatter, LaTeX maths, callouts. Read `obsidian-output.md` alongside this file for the syntax rules.

## Section 0 - Frontmatter And Header

```markdown
---
tags:
  - course/<course-slug>
  - lesson/<nn>
  - walkthrough
lesson: <nn>
topic: <topic>
status: unread
sources:
  - <source file or PDF name>
---

# Lesson <n>: <topic>

**What this covers:** <one sentence>
**What you'll be able to do by the end:** <3-5 concrete capabilities, phrased as actions>
**Built from:** <every source read: notes file, PDF names, notebook, papers>
**Prerequisites:** <what to have read or understood first; "none" is a valid answer>
**Previous lesson:** [[Lesson <n-1> - <topic>]]
```

The capability list is the promise. Phrase it as things the learner can *do* ("compute an information gain for a candidate split by hand"), never as things they will *know about*.

## Section 1 - The Map

Before any detail, orient. The learner needs a place to hang each new idea before they meet it; without it, every concept lands as an isolated fact.

- A numbered list of the 4-8 concepts in the lesson, one line each.
- A statement of how they connect - what feeds into what, what is a special case of what.
- A diagram when the structure is not linear. ASCII or a mermaid block; the learner will redraw it by hand, so keep it under about ten boxes.

Close with the single sentence version: *if you remember one thing from this lesson, it is this.*

## Section 2 - Math Toolbox

Every symbol and operation the document will later use, defined from zero. This is a hard prerequisite for the body, and it goes here, at the front, not in an appendix. Build it per `math-toolbox.md`.

## Section 3 - Concept Sections

One per concept from the Map, in the order the Map lists them. Each concept section has this internal shape, and the shape does not vary between concepts:

**3.1 What problem does this solve?**
Open with the problem, not the solution. What goes wrong without this idea? Give the concrete failing situation first - a learner who does not feel the problem cannot appreciate the fix.

**3.2 The intuition**
The plain-language version, before any notation. One analogy, chosen so it does not break under the weight the learner will put on it. Say explicitly where the analogy stops being true. Wrap it in `> [!tip] The intuition`.

**3.3 The formula, and every symbol in it**

````markdown
> [!abstract] The formula
> $$
> H(S) = -\sum_{i=1}^{c} p_i \log_2 p_i
> $$

| Symbol | Say it | What it is | Example value |
|---|---|---|---|
| $p_i$ | "p-sub-i" | The proportion of items in class $i$ | $3/4 = 0.75$ |
````

Then one sentence reading the whole formula out loud as an English sentence - "for each class, multiply its proportion by the log of its proportion, add them all up, and flip the sign." A learner who can read a formula aloud can remember it.

**3.4 Where it comes from**
The derivation, or the reasoning that motivates the definition. Small steps, one algebraic move per line, aligned on the `=`, with the move named in words:

```markdown
$$
\begin{aligned}
L &= (y - \hat{y})^2 && \text{start from squared error} \\
\frac{\partial L}{\partial \hat{y}} &= 2(y - \hat{y}) \cdot (-1) && \text{chain rule: outer power, then inner derivative} \\
&= -2(y - \hat{y}) && \text{tidy up the sign}
\end{aligned}
$$
```

The `&&` column holds the reason for each move. If a derivation is genuinely out of scope, say so explicitly and state what result is being taken on faith - never let a skipped step masquerade as an obvious one.

**3.5 Worked example - by hand**
A full numeric example the learner reproduces on paper, in `> [!example] Worked example - by hand`. Built per `worked-examples.md`. Non-negotiable: every intermediate number verified before writing.

**3.6 Your turn**
A near-identical problem with different numbers, in `> [!question]- Your turn`, immediately followed by `> [!success]- Answer` with the full working. Both callouts are collapsed, so the learner sees the prompt only when they open it and the answer only when they choose to. One per concept, minimum.

**3.7 Where it breaks**
The failure modes, the assumptions, and the mistakes a beginner actually makes here, in `> [!warning] Where it breaks`. Phrase mistakes as symptoms the learner can recognise in their own work ("your probabilities sum to 1.3"), not as abstract cautions.

**3.8 In the code**
If a notebook or code accompanies the lesson, connect the formula to the lines that implement it. Name the file and the function. Point out where the code differs from the textbook formula and why - vectorisation, numerical stability, a library's different default.

## Section 4 - Putting It Together

One end-to-end example that runs through every concept in the lesson in sequence, on a single small dataset. This is where the learner sees why the pieces were introduced in that order. Reuse the numbers from Section 3 examples where possible so the arithmetic is already familiar.

## Section 5 - Cheat Sheet

One page, formulas and definitions only, no prose. Designed to be copied onto a single sheet of paper. Table format. No derivations, no examples - this is the thing the learner rewrites from memory to test themselves.

## Section 6 - Check Yourself

8-12 questions as a task list (`- [ ]`) so the learner can tick them off in the vault, with answers in Section 8. Mix the types deliberately:

- **Recall:** state a definition or formula from memory.
- **Compute:** a small numeric problem.
- **Explain:** put an idea in your own words, or explain it to someone else.
- **Transfer:** apply the idea to a situation not in the lesson.
- **Discriminate:** given two similar methods, say which applies here and why.

Include at least one question that mixes this lesson with the previous one. Interleaving concepts across lessons is harder in the moment and retains better than blocking them.

## Section 7 - Sources

Every source, with what it supports:

```markdown
- <Author(s)> (<year>). *<Title>*. <venue / publisher / URL>
  - used for: <the specific claim or section it backs>
  - status: <current | superseded by X | contested, see Y>
```

Split into "from your course materials" and "additional reading" so the learner knows what is examinable and what is context. Follow `sourcing-and-rigor.md`.

## Section 8 - Answers

Answers to the Section 6 questions, each in its own `> [!success]- Answer <n>` collapsed callout, with full working shown - not just the final value. A learner who got it wrong needs to find the step where they diverged.

"Your turn" answers stay inline with their questions in Section 3; they are not repeated here.

## Formatting Rules

- **Tables for anything with more than two parallel items.** Symbol lists, comparisons, parameter meanings. Remember `\mid`, never `|`, for maths inside a table cell.
- **All maths is LaTeX.** Display with `$$` on its own lines, inline with `$...$` and no space before the closing dollar. Keep both simple enough to hand-copy. Full rules in `obsidian-output.md`.
- **Bold the term** at its first definition, once, so the learner can scan back to find where a word was introduced.
- **Never use a term before defining it.** If section 5 needs a word from section 7, either move the definition forward or define it in place.
- **No walls of prose.** A paragraph longer than about six lines is hiding a list, a table, or a worked example.
- **Run the four-point render check** from `obsidian-output.md` before saving.
