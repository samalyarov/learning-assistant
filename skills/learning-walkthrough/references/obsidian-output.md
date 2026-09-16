# Obsidian Output

The walkthrough lands in an Obsidian vault. It must paste in and render correctly on the first try, with no cleanup - a learner who has to hand-fix fifty broken formulas will not use the document.

Obsidian renders math with MathJax and supports a superset of standard Markdown. Write to that target by default.

## Math: The Rules That Actually Bite

**Inline math** uses single dollars: `$\hat{y}$`.

> **No whitespace before the closing dollar.** `$S_n$` renders; `$S_n $` does not. This is the single most common breakage. Check every inline formula for a trailing space.

**Display math** uses double dollars on their own lines, with a blank line before and after:

```markdown
Text above.

$$
H(S) = -\sum_{i=1}^{c} p_i \log_2 p_i
$$

Text below.
```

**Multi-line derivations** go inside one `$$` block using `aligned` (not `align`), with `&` marking the alignment point and `\\` ending each line:

```markdown
$$
\begin{aligned}
L &= (y - \hat{y})^2 \\
\frac{\partial L}{\partial \hat{y}} &= 2(y - \hat{y}) \cdot (-1) \\
&= -2(y - \hat{y})
\end{aligned}
$$
```

Align on the `=` so the learner's eye tracks down the chain of equalities.

**Pipes inside math inside a table will destroy the table.** Markdown reads `|` as a column separator before MathJax ever sees it, and `\|` is not a fix because it is also valid LaTeX. Use `\mid` or `\vert`:

| Wrong | Right |
|---|---|
| `$P(A|B)$` | `$P(A \mid B)$` |
| `$\|x\|$` | `$\lVert x \rVert$` |

**Other traps:**

- A literal dollar sign near math is ambiguous and will not render. Write `\$` and keep currency away from formulas.
- Underscores in ordinary prose italicise text. Write variable names in math (`$x_i$`) or code (`` `x_i` ``), never bare.
- Do not use `\newcommand` macros. They do not reliably carry across notes in a vault, and the learner pasting one section into a new note will get raw LaTeX.
- Stick to standard MathJax. No `\usepackage`, no TikZ, no LaTeX document environments.
- `\text{...}` works and should be used for words inside formulas: `$p_{\text{spam}}$`.

## Callouts

Use Obsidian callouts to give each part of a concept section a distinct visual shape. Syntax is `> [!type] Title`, with every subsequent line also prefixed by `> `. Appending `-` makes the callout **collapsed by default**, and `+` makes it foldable but open.

Standard mapping for a walkthrough:

| Section part | Callout |
|---|---|
| Intuition | `> [!tip] The intuition` |
| The formula | `> [!abstract] The formula` |
| Worked example | `> [!example] Worked example - by hand` |
| Your turn | `> [!question]- Your turn` |
| Answer | `> [!success]- Answer` |
| Where it breaks | `> [!warning] Where it breaks` |
| Optional aside | `> [!note]- Aside (optional)` |

The collapsed variants are why this matters: **answers hide inline** rather than living in a section at the bottom. The learner attempts the problem with the answer one click away but not visible - which is exactly the retrieval condition the walkthrough is designed for.

```markdown
> [!question]- Your turn
> Compute the information gain for splitting on `sender_unknown`.
> You should get a value between 0 and 1, in bits.

> [!success]- Answer
> $H(\text{yes}) = H(\text{no}) = 0.811$ bits, so the weighted average is $0.811$.
> $$\text{Gain} = 1.000 - 0.811 = 0.189 \text{ bits}$$
> Same as `contains_free` - and both lose to `has_attachment`.
```

Display math inside a callout still needs each line prefixed with `> `.

## Note Frontmatter

Open every walkthrough with YAML properties so it files itself in the vault:

```yaml
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
```

Keep property names stable across lessons so the vault can query them. `status` lets the learner track their own progress.

## Linking Into The Vault

- Link to sibling lessons with wikilinks: `[[Lesson 06 - Decision Trees]]`. Use the learner's actual note titles when they are known from the vault; otherwise use the title the walkthrough itself declares, and say that the link will resolve once that note exists.
- Link to the learner's own notes file for the lesson rather than duplicating it.
- Unresolved wikilinks are harmless in Obsidian - they show as a link that creates the note on click. Prefer a hopeful link over no link.
- Use `![[image.png]]` embed syntax only for files that actually exist in the vault.

## What Else Renders

- **Mermaid** diagrams render natively in fenced ` ```mermaid ` blocks. Good for the Map section.
- **Footnotes** `[^1]` render, and suit source citations at point of use.
- **Tables** render, but keep them narrow - Obsidian does not wrap wide tables gracefully in reading view.
- **Task lists** `- [ ]` render as checkboxes; useful for the Check Yourself section, since the learner can tick items off in place.

## Verify Before Delivering

These four account for nearly every rendering failure:

1. Inline math with a space before the closing `$`.
2. A raw `|` inside math inside a table.
3. A display `$$` block without blank lines around it.
4. A callout whose continuation lines are missing the `> ` prefix.

Do not eyeball them. Run the checker in the skill folder against the finished file:

```bash
python <skill>/scripts/check_obsidian.py path/to/walkthrough.md
```

It exits non-zero and prints `file:line: problem` for each hit. Fix every one before delivering. A clean exit is not proof the maths is *right* - that is the arithmetic gate's job - only that it will render.
