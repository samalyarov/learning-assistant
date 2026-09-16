# Sourcing And Rigor

A walkthrough is a study document. The learner will believe it, memorise it, and repeat it in an exam or an interview. Everything in it must be traceable to something real.

## Never Fabricate

**If you cannot verify that a source exists, do not cite it.**

A plausible-looking citation - right-sounding authors, a real journal, a year that fits - is the most damaging thing this skill can produce, because it is unfalsifiable to a beginner and it propagates into their own work. Fabricated references have ended real academic careers.

When you know a result but cannot pin the source:

- Say so: "this is standard in the literature; I could not locate the original statement of it."
- Or state the mechanism without attribution and mark it as unattributed.
- Never round a vague memory up to a specific citation.

The same applies to numbers. Do not attribute "a 40% improvement" to a paper unless you have seen that figure in it.

## Research Order

1. **The learner's own materials first.** Their notes, the official PDFs and slides, the notebook, and every source those link to. This is the course canon - it is what the exam will test, and where the walkthrough's vocabulary must come from.
2. **The primary source next.** If the notes reference a method, find the paper or textbook chapter that introduced it. Restatements drift; the original usually explains *why* the method is shaped that way, which is exactly what a lecturer skipped.
3. **A standard textbook for the field.** For grounding definitions and notation that the notes assume.
4. **Recent literature last**, to check whether the lesson's version of the story still holds.

Do the research before writing, not to patch citations onto finished prose. Preliminary literature research changes what the explanation should say, not just what it cites.

## Attribution Standard

Every non-obvious claim carries an attribution. "Non-obvious" means anything a learner could reasonably ask "says who?" about: an empirical result, a performance claim, a historical origin, a rule of thumb with a specific threshold, a statement about what practitioners do.

Arithmetic, definitions internal to the course, and derivations shown in full do not need citations - they carry their own evidence.

Cite at the point of use, not only in the source list. A superscript or a parenthetical is enough; the full entry lives in the Sources section.

## Flag The Status Of Every Claim

The literature is not a flat set of true statements. Mark the ones that are moving:

| Status | When | How to write it |
|---|---|---|
| **Current** | Well-replicated, uncontested | Cite and move on |
| **Superseded** | A later result extends or replaces it | "X showed A (year); Y later refined this to B, which is what modern implementations use" |
| **Contested** | Serious disagreement in the field | Give both positions and say which one the course takes |
| **Failed to replicate** | The original result did not hold up | State the original, state the replication, and say what survives |
| **Popular oversimplification** | A textbook version that practice contradicts | "Textbooks say X; in practice, Y, because Z" |

A learner who is told only the tidy version is being set up to be surprised later. A learner who is told "this is the clean story, and here is where it gets messy" is being taught.

## When The Lecturer Is Wrong

It happens, and it is a common reason this skill gets invoked. Handle it without undermining the learner's course:

- State what the notes say.
- State what the literature says.
- Explain the difference, and whether it is a simplification, a different convention, or an error.
- Say which one to write in the exam. That is usually the lecturer's version, and saying so plainly is more useful than being right.

Do not be coy about it, and do not silently correct - a learner whose notes and walkthrough disagree without explanation will trust neither.

## Sources Section Format

Split by role so the learner knows what is examinable:

```markdown
### From your course materials

- <Author(s)> (<year>). *<Title>*. <venue / publisher / URL>
  - used for: <the specific section or claim it backs>
  - status: <current | superseded by ... | contested, see ...>

### Additional reading

- <same format>
  - read this if: <the specific gap it fills>
```

The "read this if" line matters. A bare reading list is ignored; a list that says which one answers which lingering question gets used.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Citation added after the prose was written | Research first; let the sources shape the explanation |
| A blog post cited for a result the blog got from a paper | Trace it to the paper and cite that |
| "Studies show..." with no study named | Name the study or drop the claim |
| Presenting a contested position as settled | Give both sides and say which the course uses |
| Citing a paper's abstract for a claim in its discussion | Read the part you are citing |
| Correcting the lecturer without saying what to write in the exam | Always tell the learner which version to reproduce |
