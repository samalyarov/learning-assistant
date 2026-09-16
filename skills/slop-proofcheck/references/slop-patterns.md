# Slop Patterns

The judgment half of the pass. The script (`scripts/check_slop.py`) handles vocabulary; this file handles everything that needs a person to look at it.

Every example below is in explanatory register, because the same pattern is a different problem in a lesson than it is in a blog post. Where a rule has been narrowed or dropped for teaching material, that is stated.

## Provenance

Section 2 is derived from **[no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang**, MIT licensed. The pattern names, the banned-word list, and the portability test in the parent `SKILL.md` all come from there.

The re-scoping is what this file adds, and it goes in three directions:

| | |
|---|---|
| **Kept as-is** | Puffery, weasel attribution, throat-clearing, faux-insight setups, colon reveals, superficial `-ing` analysis, rhetorical setups, fake-profound kickers, recap endings (§2.1-2.9) |
| **Narrowed or hardened** | Synonym cycling hardened to a correctness rule (§2.10); binary contrasts narrowed to spare genuine discriminations (§2.11); metadiscourse split into interpretive and navigational (§2.12); formatting rules heavily cut back (§2.14) |
| **Dropped** | "Vary your structure" and "preserve the writer's voice". Both damage teaching material. See §4 |
| **Added** | §3 in full, and the long-dash ban in §2.13 |

If you are editing an essay, a post, or anything carrying a human writer's voice, use the original project instead. It is built for that and this is not.

---

## 1. Vocabulary

### Cut outright

No technical sense, no defensible use in an explanation:

> delve, foster, utilize, facilitate, empower, streamline, cutting-edge, paradigm shift, game changer, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, ever-evolving, seamless, unlock, unleash, revolutionize, testament, landscape *(figurative)*, delve into, deep dive

Most have a plain replacement: *utilize* → use, *facilitate* → let / help, *paramount* → most important, *intricate* → complicated.

### Check before cutting - real terms in technical writing

This is where an unfiltered anti-slop list does damage. Each of these is hype in prose and a defined term in the domain:

| Word | Slop use | Legitimate use - leave alone |
|---|---|---|
| **leverage** | "leverage the power of trees" | leverage points in regression; leverage in influence diagnostics; financial leverage |
| **robust** | "a robust solution" | robust statistics; robust to outliers; robustness checks |
| **harness** | "harness the potential of" | a test harness |
| **significant** | "significantly improved results" | statistically significant; a significance level |
| **optimal / optimize** | "optimal outcomes" | the optimum of a function; an optimizer; convex optimization |
| **normalize** | "normalize the discussion" | normalizing a vector, a distribution, a database schema |
| **kernel / regular / degenerate / naive** | - | all defined terms; never flag |
| **critical** | "critically important" | a critical point; a critical value |
| **dramatic** | "a dramatic improvement" | - no technical sense; cut |

Rule: if the word names something the learner could compute, look up, or point at in the maths, keep it. If it only rates the thing, cut it.

### Empty intensifiers

> very, really, quite, extremely, incredibly, remarkably, truly, fundamentally, essentially, basically, actually, literally, simply, just, of course

Not banned - banned *when they add nothing*. "The sum is just the total" loses nothing without *just*. "You just need the three log facts" is doing real work: it bounds the prerequisite. Read it with the word removed; if nothing changed, it was filler.

Two of these are worse than filler in a learner document. See §3.1.

---

## 2. Imported patterns, re-scoped for explanation

### 2.1 Importance puffery

Telling the learner a thing matters instead of showing them what it does.

> "Entropy plays a vital role in machine learning."
> "This formula is a cornerstone of information theory."
> "Understanding this is crucial to your success."

**Fix:** state the function. → "Entropy is the number a decision tree uses to rank candidate splits."

A learner cannot act on *important*. They can act on *what it is for*.

### 2.2 Weasel attribution

> "Studies show that…", "Experts agree…", "It is widely regarded as…", "Research suggests…", "It is commonly understood that…"

**Fix:** name the source, or drop the claim. In a walkthrough this is a hard failure, not a style problem - an unfalsifiable citation propagates straight into the learner's own coursework. If no source exists, say the claim is unattributed. See `learning-walkthrough/references/sourcing-and-rigor.md`.

### 2.3 Throat-clearing openers

> "Here's the thing.", "Let me be clear.", "Let's dive in.", "Let's unpack this.", "Let's break it down.", "Now, before we begin…", "It's worth noting that…", "It's important to note that…"

**Fix:** delete and start with the point. The header already announced the topic.

Related, and already banned by the learner contract: **"Recall that…"**, **"As we know…"**, **"As you'll remember…"**. Nobody recalls. State it again, or point at where it was defined.

### 2.4 Faux-insight setups

> "What nobody tells you about entropy is…", "The part everyone misses…", "Here's what most courses get wrong…", "This is the part most people skip."

Frames the explainer as the lone initiate. **Fix:** cut the setup, keep the claim. → "Entropy ignores group size. Information gain has to weight for it."

### 2.5 Colon reveals

A noun phrase, a colon, a dramatic lowercase payoff.

> "The detail that makes it work: the minus sign."
> "The best part: it needs no calibration."

**Fix:** write the sentence. → "The minus sign is what keeps entropy positive, because every log of a proportion is negative."

Colons are fine for lists, labels, table cells, and worked-example step headers. They are not fine as suspense.

### 2.6 Superficial `-ing` analysis

Trailing clauses that gesture at meaning without adding any.

> "The algorithm picks the highest-gain split, **highlighting the elegance of** the greedy approach."
> "…, **underscoring the importance of** entropy."
> "…, **showcasing** how the pieces fit together."

**Fix:** replace with the actual consequence. → "The algorithm picks the highest-gain split, so a feature that splits into many tiny branches always wins - which is the failure mode in §3.7."

### 2.7 Rhetorical setups

> "What if I told you…", "Think about it:", "Plot twist:", "Here's where it gets interesting.", and self-answered "So what does this mean? It means…"

**Fix:** make the point. A genuine question posed *to the learner to answer* is different and belongs - that is a "Your turn" prompt, not a rhetorical device.

### 2.8 Fake-profound kickers

The closing line that reaches for an aphorism.

> "And that's the beauty of entropy: sometimes the messiest questions give the clearest answers."
> "In the end, a decision tree is just a series of good questions - much like learning itself."

**Fix:** delete it. Do not rewrite it into a better metaphor. A walkthrough ends on the cheat sheet, the check-yourself questions, and the sources. It does not need a curtain line.

### 2.9 Recap endings

> "In conclusion…", "To summarize what we've learned…", "Overall, we covered entropy, information gain, and splits."

**Fix:** delete. The cheat sheet already is the summary, and it is a better one because the learner rewrites it from memory. A prose recap is the low-utility study technique the whole skill exists to avoid.

### 2.10 Synonym cycling - upgraded to a hard rule

In an essay, rotating words is a style tic. In a lesson it is a correctness failure: a beginner reading *feature*, *attribute*, *variable*, *predictor*, and *column* for the same object concludes there are five objects.

> "The **feature** splits the data. Each **attribute** is scored, and the best **variable** wins."

**Fix:** pick one name and use it every single time. → "The feature splits the data. Each feature is scored, and the best feature wins."

Where the field genuinely uses several names, declare them **once**, in the math toolbox, as an alias line - "*feature*, also called an attribute, a predictor, or a column" - then use the chosen one and never rotate again.

This applies to notation too. If the source slides write $|S|$ and the textbook writes $n$, choose one, say you are choosing, and stay with it.

### 2.11 Binary contrasts - narrowed

The rhetorical form is slop. The pedagogical form is required by the structure contract.

**Cut** - contrast with no content, built for rhythm:
> "It's not about the formula. It's about the intuition."
> "This isn't just a score. It's a way of thinking."

**Keep** - contrast that names a difference the learner can act on:
> "Entropy is not variance. Variance measures spread around a mean; entropy measures uncertainty across categories, and it has no mean in it at all."

The test: does the second half give a *concrete, checkable* difference? Then it is a discrimination, and Section 6 of the structure contract explicitly asks for these. Does it only invert the first half for cadence? Then it is slop.

### 2.12 Interpretive metadiscourse - split in two

**Cut** - asserts importance without paying for it:
> "This distinction matters more than it sounds."
> "The key point here is…", "As you can see…", "Notably,", "Importantly,"

**Keep** - points at something specific:
> "We use this again in §4, where the branch sizes come back."
> "Notice that entropy depends only on the proportions, not the group size - that is exactly why gain has to weight by branch size."

The second one directs attention to a named fact the learner will need. That is not metadiscourse; that is teaching. The test is whether a specific fact or location follows. If the sentence could be deleted with no information lost, delete it.

### 2.13 Long dashes - banned outright

**No em dashes (`U+2014`) and no en dashes (`U+2013`). Ever. Use a plain hyphen `-` (`U+002D`).**

The banned characters are named by codepoint rather than shown, so that this file passes its own check.

This is a house-style rule, and it is deliberately stricter than the typographically correct answer. The em dash has become one of the loudest surface tells of machine-written text, to the point where readers now discount prose on sight of it. That cost outweighs the typographic gain, so the rule is absolute rather than a judgment call.

It is enforced mechanically, as a `cut:` hit, and it is the one rule checked against the raw line rather than the stripped prose - a long dash in a heading, a table cell, or a link text is still a long dash.

**Fix:** replace with a plain hyphen. Where a hyphen reads badly, that is usually a sign the sentence wanted different punctuation anyway:

> "The tree picks the highest-gain split - the one that removes the most messiness."

Or restructure into a comma, a colon, brackets, or a full stop:

> "The tree picks the highest-gain split: the one that removes the most messiness."
> "The tree picks the highest-gain split, which is the one that removes the most messiness."

Do not substitute another long character to get around the rule. A double hyphen `--` is not a fix either.

**Not affected:** hyphens in compound words (*highest-gain*, *three-rung*), minus signs in maths (`$-1$`, which lives inside `$...$` and is never touched), and ranges written as `4-10`.

### 2.14 Formatting slop - heavily narrowed

**Cut:**
- Emoji in headings or body text.
- **Bold** sprinkled mid-sentence for emphasis. Bold has one job in a walkthrough: marking a term at its first definition, once.
- Bold on whole sentences.
- Exclamation marks, outside of a factorial.

**Do not cut** - these are required by the structure contract and are not slop here:
- Short sections with their own headers.
- Bullet lists and tables.
- Callouts.
- Repeated section shapes across concepts.

Essay formatting rules do not transfer to a study document. This is the single most common way an anti-slop pass damages a walkthrough.

---

## 3. Patterns specific to explanatory writing

These are not in general anti-slop guidance. They are the ways machine-written *teaching* material specifically goes wrong.

### 3.1 Condescension markers

The worst class, because the damage lands on the learner rather than the prose.

> "**Obviously**, the logs are negative."
> "**Simply** substitute the values."
> "It's **easy to see** that the terms cancel."
> "**Clearly**, this reduces to 0."
> "**Of course**, you'll recognise the chain rule here."
> "This is **trivial** once you see it."
> "**Just** apply the formula."

Every one of these tells a learner who does *not* find it obvious that the failure is theirs. That is the exact moment a beginner concludes they are bad at maths and stops. The learner contract already bans *recall that* and *as we know*; this is the same family and it is bigger.

**Fix:** delete the word, or replace it with the reason.
> "Obviously, the logs are negative." → "Every $p_i$ is between 0 and 1, and the log of a number below 1 is negative."

The deleted word cost nothing. The replacement taught something.

### 3.2 The magic step

> "It can be shown that…", "After some algebra…", "It follows that…", "One can easily verify…", "Through a bit of manipulation…", "Skipping the details…"

The cardinal sin of a walkthrough: a skipped step wearing the costume of an obvious one.

**Fix:** show the step, or say plainly that it is out of scope and name what is being taken on trust. → "The full derivation of this bound needs Jensen's inequality, which this lesson does not cover. We take the result on trust: $H(S) \le \log_2 c$."

Already stated in `worked-examples.md`; it is repeated here because it turns up in derivations and intuition sections, not only in numbered examples.

### 3.3 Restatement disguised as explanation

The second sentence renames the first without adding an anchor.

> "Entropy measures the uncertainty in a set. **In other words**, it captures how uncertain the set is."
> "**Essentially**, information gain is the gain in information."
> "**Put simply**, the weighted average is an average that is weighted."

**Fix:** either delete the restatement, or make it earn its place by introducing something new - a number, a picture, a mechanism, a unit.
> "Entropy measures the uncertainty in a set. Concretely: a bag of 4 spam and 4 ham scores 1.000 bits, and a bag of 8 spam scores 0."

A rephrase is only worth its line if it moves the idea closer to something the learner can hold.

### 3.4 Cheerleading

> "Great question!", "Don't worry - this is easier than it looks!", "You've got this!", "See? Not so bad!", "And that's all there is to it!", "Congratulations, you now understand entropy!"

Performed enthusiasm. It costs the learner attention and buys nothing, and the reassurance is unearned - the document has no idea whether they found it hard.

**Fix:** delete. If the intent was to flag genuine difficulty, say the true thing instead: "This step is where most people lose the sign. Check it twice."

### 3.5 Analogy stacking

The structure contract asks for **one** analogy per concept, chosen so it does not break under the weight the learner puts on it.

> "Entropy is like a messy room. It's also like a coin flip. Think of it as a game of twenty questions. It's the surprise of a lottery ticket."

Four models, four sets of edges, and the learner now has to work out which one to trust.

**Fix:** keep the one that survives the most pressure, say where it stops being true, and delete the rest.

### 3.6 Hollow section openers

> "## Entropy
> In this section, we will explore the concept of entropy."

The header said that. **Fix:** open on the problem the concept solves, as §3.1 of the structure contract requires.

Same pattern: "Before we get into X, let's talk about why X matters." Just get into X.

### 3.7 Rule-of-three padding

Three bullets, three adjectives, three examples - regardless of how many the material actually has. The third is usually invented to complete the rhythm, which means it is the weakest and sometimes the wrong one.

**Fix:** write the number of items that exist. Two is a fine number. So is five.

### 3.8 Hedge stacking

> "This **might** suggest that entropy **could potentially** be **somewhat** useful for **certain kinds of** splits."

Four hedges on one claim leaves the learner unable to tell whether the thing is true. **Fix:** one hedge maximum, and make it precise about *what* is uncertain. → "Entropy ranks splits well when branches are similar in size. When they are not, gain ratio does better - see Lesson 08."

Real uncertainty stated once is honest. Stacked uncertainty is the prose refusing to commit.

---

## 4. The keep list

Things that trip a slop detector and should survive the pass untouched. Check this list before cutting.

| Looks like slop | Actually | Why it stays |
|---|---|---|
| The same 3.1-3.8 shape on every concept | Deliberate structure | Predictability lowers cognitive load; the contract mandates it |
| "Your answer should be between 0 and 1" | Self-check scaffold | Lets a learner verify without flipping to answers |
| Short declarative fragments: "Entropy is never negative." | Plain statement | Direct and checkable; not dramatic fragmentation |
| "Where the analogy stops:" | Required by the contract | Naming an analogy's limits prevents a false model |
| "Notice that entropy ignores group size" | Pointer to a specific fact | Attention direction with a payload |
| Repeating the same term 30 times | The one-name rule | Consistency beats variety in teaching |
| "We come back to this in §4" | Navigation | Points at a real place |
| Passive voice in a derivation: "both sides are multiplied by 2" | Conventional register | Rewriting to active reads stilted; leave it |
| A worked example reusing earlier numbers | Required by the contract | Familiar arithmetic keeps attention on the new idea |
| Simple, repetitive sentence shapes in a step-by-step | Clarity | Varying cadence mid-derivation hurts comprehension |

---

## 5. Order of the pass

1. Run `check_slop.py`. Fix every `cut:` hit. Confirm every `check:` hit is the technical sense.
2. Apply the prime test - substitute a different subject - to every sentence with no number, name, mechanism, or consequence in it.
3. Sweep for §3.1 condescension markers and §3.2 magic steps. These two do the most damage per instance.
4. Sweep for §2.10 synonym cycling: list the nouns naming the lesson's central object and confirm exactly one is used.
5. Read the openers and closers. Sections open on the problem; the document ends on the sources.
6. Check the keep list before finalising any cut.
7. Re-run `check_obsidian.py` afterwards - prose edits inside callouts and tables can break the `> ` prefix or a math delimiter.

Step 7 is not optional. A slop fix that breaks a formula has made the document worse.
