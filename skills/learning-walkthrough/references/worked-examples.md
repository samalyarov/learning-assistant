# Worked Examples

The learner reproduces these on paper with a pen. That single constraint determines everything below: the size of the numbers, the granularity of the steps, and the standard of correctness.

## The Arithmetic Gate

**Compute every number before you write it. Verify it with a script, not by eye.**

This is the one rule with no exceptions. Plausible-looking-but-wrong arithmetic is the failure mode that ruins a study document: the learner spends forty minutes on paper trying to reproduce `0.918`, concludes they cannot do arithmetic, and abandons the material. A confidently wrong intermediate value is worse than no example at all.

Before writing an example into the document:

1. Write the calculation in a scratch script - Python, or the notebook if one exists.
2. Run it. Print every intermediate value the walkthrough will show, not just the final answer.
3. Copy the printed values into the document.
4. State the rounding: "≈ 0.811 (3 d.p.)".

If the numbers come out ugly, that is a signal to redesign the example, not to round quietly and hope.

## Choosing Numbers

Design the example backwards from the arithmetic the learner will do.

| Ingredient | Choose | Avoid |
|---|---|---|
| Dataset size | 4-10 rows | Anything needing a spreadsheet |
| Values | Small integers, or one decimal place | 7-digit floats |
| Fractions | Halves, quarters, thirds; clean denominators | 17/23 |
| Logs | $\log_2$ of powers of 2; at most one irrational, given in the toolbox | $\log_2 7$ scattered through every step |
| Matrices | 2×2 and 2×3 | 5×5 |
| Probabilities | Sum to exactly 1 with clean parts (0.25 / 0.25 / 0.5) | Values that leave 0.3333... everywhere |
| Answers | Land on something recognisable - an exact 1, a clean 0, a memorable 0.5 | A number with no character |

A good example has a **punchline**: the result should teach something, not just exist. Two candidate splits where the intuitively appealing one loses. A gradient step that overshoots because the learning rate is too high. A prior that flips the conclusion. If the numbers produce no insight, redesign them.

## Showing The Steps

One operation per line. Name the operation. Show the substitution before showing the result.

**Not this:**

```
Entropy of the left branch is 0.811.
```

**This:**

```
  H(left) = -(3/4)·log₂(3/4) - (1/4)·log₂(1/4)      substitute the counts: 3 spam, 1 ham out of 4

  log₂(3/4) = log₂3 - log₂4 = 1.585 - 2 = -0.415    split the fraction, use log₂3 ≈ 1.585
  log₂(1/4) = -2                                    because 2⁻² = 1/4

  H(left) = -(0.75)(-0.415) - (0.25)(-2)            put the two logs back in
          = 0.311 + 0.5                             two minus signs cancel each time
          = 0.811 bits                              (3 d.p.)
```

Rules that make the difference:

- **Write the substitution line.** The learner's most common stall is not knowing which number goes where.
- **Annotate the right margin** with the reason for the move, in words.
- **Show sign handling explicitly.** Cancelled negatives are the single largest source of hand-arithmetic errors.
- **Carry units.** "0.811 bits", "3.2 units of loss", "a probability, so between 0 and 1."
- **Never write "it can be shown that".** Either show it, or say plainly that it is out of scope and being taken on trust.

## Fading: The Three-Rung Ladder

Do not give the learner three identical worked examples, and do not jump from one example straight to an unaided problem. Fade the support:

1. **Fully worked.** Every step shown. The learner copies it out and follows.
2. **Completion problem.** The same shape, first steps given, last steps blank. This is where the learner does the work while the structure still holds them up.

   ```
   H(right) = -(1/4)·log₂(1/4) - (3/4)·log₂(3/4)
            = -(0.25)(____) - (0.75)(____)
            = ____ bits
   ```

3. **Unaided.** Same shape, new numbers, nothing given. This is the "Your turn" item.

For a beginner, studying a worked example beats attempting an unaided problem, and completion problems bridge the two. Jumping straight to unaided practice is where beginners stall and conclude they are bad at the subject. See `learning-science.md` for the evidence and its limits.

## Diagrams

The learner redraws them by hand, so:

- Under about ten boxes or nodes.
- Label every arrow with what flows along it.
- ASCII or mermaid, both hand-copyable. Avoid anything needing precise curves.
- If a diagram has numbers, they are the *same* numbers as the worked example beside it.

## Your Turn Problems

- Same structure as the worked example, different numbers.
- Verified answer, held back to the answers section, with the full working shown there - the learner who got it wrong must be able to find the step where they diverged.
- State the expected answer's shape in the prompt ("you should get a value between 0 and 1"). This lets a learner self-check without flipping to the answers.
- At least one problem per lesson where the answer is *surprising* relative to the obvious guess.

## Common Mistakes

| Mistake | Consequence |
|---|---|
| Unverified arithmetic | Learner loses an hour and their trust in the document |
| Realistic dataset sizes | Impossible on paper; the example becomes decorative |
| Skipping to the answer | Learner sees the destination, learns nothing about the route |
| Three examples of the same difficulty | No progression; the learner never leaves the training wheels |
| Different numbers in the diagram and the text | Learner assumes they made an error and re-does correct work |
| Rounding silently mid-calculation | Learner's answer differs in the third decimal and they cannot tell why |
