# Math Toolbox

The prerequisites section at the front of every walkthrough. It exists so that the body of the document never asks the learner to meet a new symbol and a new idea in the same sentence - a beginner who has to decode `Σ` while also absorbing what entropy means will fail at both.

Assume no prior notation knowledge, every time. It costs a paragraph to re-explain a symbol and costs the whole document to skip it.

## Build It In Three Passes

**Pass 1 - Inventory.** Go through every source: the notes, the PDFs, the notebook, the papers. Write down every symbol, operator, function name, and piece of notation that appears anywhere. Include the ones that look obvious. `x_i`, `∑`, `log`, `E[·]`, `‖·‖`, `argmax`, `∂`, `∇`, `~`, `∝`, `:=`, `ŷ`, superscripts in parentheses, bold versus italic letters.

**Pass 2 - Rank.** Order them by when the learner first meets them in the body, not alphabetically. The toolbox is read front to back once, then used as a lookup.

**Pass 3 - Explain.** One row per symbol, and a short subsection for anything that needs more than a row.

## The Notation Table

Every walkthrough's toolbox opens with this:

```markdown
| Symbol | Say it out loud | What it means | Tiny example |
|---|---|---|---|
| $\sum_{i=1}^{n} x_i$ | "sum from i equals 1 to n of x-sub-i" | Add up all the $x$ values, from the first to the $n$-th | $x = [2, 5, 3]$, so $\sum x_i = 2+5+3 = 10$ |
| $\hat{y}$ | "y-hat" | The model's *prediction*, as opposed to $y$, the true value | True $y = 7$, predicted $\hat{y} = 6.4$ |
| $\log_2 x$ | "log base two of x" | The power you raise 2 to, to get $x$ | $\log_2 8 = 3$, because $2^3 = 8$ |
```

The "say it out loud" column is not decoration. A learner who cannot pronounce a symbol cannot rehearse it, cannot ask about it, and cannot hold it in working memory while reading a formula.

The "tiny example" column must contain actual numbers, computed and verified. `$x = [2,5,3]$, so the sum is 10` teaches; "the sum of the elements" does not.

## Beyond The Table

Some things need a subsection, not a row. Give each of these a short block with a worked micro-example whenever the lesson uses them:

- **An operator with real machinery behind it.** Matrix multiplication, the gradient, expectation, convolution. Show one complete small instance - a 2×2 times a 2×1, computed entry by entry.
- **Index conventions.** Whether $x_i$ means the $i$-th sample or the $i$-th feature, and how the course writes the other one. This single ambiguity derails more beginners than any concept.
- **Functions whose base or convention varies.** In machine learning `log` usually means natural log; in information theory it usually means $\log_2$. Say which one *this course* means, and check the notebook to confirm.
- **Notation collisions.** When the same letter means two things in the same lesson, say so explicitly and up front.

## Prerequisite Concepts

Symbols are not the whole toolbox. Some lessons need a concept the learner is assumed to have and may not. Add a short "before we start" block for each, at the depth of a full concept section but shorter:

- Rebuild it from the ground up in a paragraph.
- Give one hand-scale numeric example.
- Say exactly where in the lesson it gets used, so the learner knows why they are reading it.

Typical candidates: what a derivative *is* (a slope, a rate of change) before any gradient method; what a probability distribution *is* before Bayes; what a vector *is* geometrically before any embedding; what a logarithm *does* before entropy or log-loss.

## Useful Constants

When a lesson's arithmetic repeatedly needs an irrational value, list it once in the toolbox so the learner is not re-deriving it on paper:

```markdown
| Value | ≈ | Where it shows up |
|---|---|---|
| $\log_2 3$ | 1.585 | Any three-way split or 1/3 probability |
| $\ln 2$ | 0.693 | Converting between $\log_2$ and $\ln$ |
| $e$ | 2.718 | Softmax, sigmoid, exponential decay |
```

## Common Mistakes

| Mistake | Why it fails | Do instead |
|---|---|---|
| Toolbox in an appendix | The learner meets the symbol before the definition and stops reading | Front of document, before the concept sections |
| "Recall that $\sigma$ denotes..." | The learner does not recall; the word signals they should already know, so they feel stupid and skim | "$\sigma$ is the standard deviation - here is what that measures" |
| Defining only the exotic symbols | The gap is rarely `∇`; it is `x^{(i)}` versus `x_i` | Inventory everything, including the obvious |
| Definitions with no numbers | "The mean of the sample" is a restatement, not an explanation | Every entry gets a computed example |
| One toolbox reused across lessons | Notation drifts between lecturers and chapters | Rebuild the inventory from *this* lesson's sources every time |
