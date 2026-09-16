# Notebook Mode

When the deliverable is a Jupyter notebook rather than a standalone markdown file. The teaching standard does not drop - a notebook is a walkthrough whose worked examples happen to execute.

## The Core Rule

**Explanation lives in markdown cells, at the same depth as a markdown walkthrough.**

The common failure is treating a notebook as an excuse to explain less: a one-line comment above a twenty-line cell, or a heading with no body. A learner reading a notebook has *more* to decode than one reading prose, not less - they must follow the maths and the code and the mapping between them.

Maths in markdown cells is LaTeX, same as the markdown walkthrough: `$...$` inline, `$$...$$` display. Jupyter renders both through MathJax, so a cell written to the rules in `obsidian-output.md` will render in the notebook *and* survive a copy-paste into the learner's Obsidian vault. Write to that standard so the two artifacts stay interchangeable.

## Cell Pattern

Every code cell gets a markdown cell immediately above it, containing:

1. **What this cell does**, in one sentence, in plain language.
2. **Why it is here** - which step of the method it implements, tied back to the formula by name.
3. **What to look at in the output**, and what a correct result looks like.

```markdown
### Computing the entropy of each candidate split

This implements $H(S) = -\sum_i p_i \log_2 p_i$ from Section 2, once per feature.

`np.bincount` counts how many rows fall in each class; dividing by the total turns
counts into the probabilities $p_i$. The `p > 0` mask exists because $\log_2 0$ is
undefined - mathematically we treat $0 \log 0 = 0$, and this is how that is enforced in code.

**Look for:** three numbers between 0 and 1. `has_attachment` should be lowest -
that is the split we will pick.
```

Then the code cell.

## Structure Of The Notebook

Mirror the walkthrough contract in `walkthrough-structure.md`, adapted:

| Walkthrough section | Notebook form |
|---|---|
| Header | Title markdown cell: what this covers, what you will be able to do, sources |
| The Map | Markdown cell with the concept list and the flow diagram |
| Math Toolbox | Markdown cell(s) before any code, with the notation table |
| Concept sections | Markdown explanation → code cell → markdown reading of the output |
| Worked example | A code cell that *prints intermediate values*, not just the final answer |
| Your turn | A code cell with a `TODO` and an `assert` the learner can run to check themselves |
| Cheat sheet | Final markdown cell |
| Sources | Final markdown cell |

## Code That Teaches

- **Print the intermediates.** A cell that prints only the final number teaches nothing. Print each $p_i$, each log, each partial sum, so the learner can compare against their paper working line by line.
- **Use the same numbers as the paper example.** The notebook confirms the hand calculation; different numbers make it a separate exercise.
- **Prefer explicit loops over clever vectorisation** in teaching cells, and show the vectorised version afterwards as "how you would actually write it". The learner needs to see the sum before they see `np.einsum`.
- **Name variables after the symbols.** `p_i`, `H_parent`, `weighted_H` - not `x`, `tmp`, `res`. The mapping between formula and code should need no explanation.
- **Give "your turn" cells a self-check**: `assert abs(gain - 0.189) < 0.001, "check your probabilities"`. The learner gets feedback without scrolling to answers.

## Do Not Touch Their Code

Unless the user explicitly asks for changes:

- Do not refactor, rename, or "improve" the user's existing code cells.
- Do not reorder cells.
- Do not delete their scratch cells or outputs.

Add markdown cells around the existing code. If a code cell is genuinely wrong or will not run, say so in the markdown cell above it and propose the fix there - do not silently apply it.

If new code is needed to demonstrate something, add it as a new cell, clearly marked as an addition.

## Common Mistakes

| Mistake | Fix |
|---|---|
| One markdown cell for five code cells | One per code cell |
| Explanation shallower than the .md walkthrough | Same depth; the format changed, the learner did not |
| Comments inside the code instead of markdown above it | Both - markdown for the concept, comments for the line |
| Final answer printed, intermediates hidden | Print every value the hand calculation produces |
| Silently fixing the user's broken cell | Explain the bug in markdown, propose the fix, let them apply it |
| Markdown cell placed *below* the code it explains | Above. The learner reads top to bottom and needs the frame first |
