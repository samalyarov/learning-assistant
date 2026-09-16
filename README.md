# Learning Assistant - Agent Skills for Studying

Two [Agent Skills](https://agentskills.io/specification) for Claude:

- **`learning-walkthrough`** turns course material into a study document you can actually work through - built from the ground up, every symbol named, every example small enough to redo on paper, every claim traceable to a real source.
- **`slop-proofcheck`** reads the finished document back and strips the tells of machine-written prose, without flattening it into generic polish.

Output is [Obsidian](https://obsidian.md)-ready: LaTeX maths, YAML frontmatter, callouts, and answers that stay collapsed until you open them.

---

## The problem

Ask an assistant to "explain this lesson" and you get a **summary** - material compressed for someone who already understands it. That is the opposite of what a learner needs, and it is also, empirically, one of the weakest ways to study: in the largest review of learning techniques, summarisation, rereading and highlighting all rated *low utility*, while practice testing and distributed practice rated highest.[^1]

This skill produces a **walkthrough** instead: material *expanded* for someone who doesn't understand it yet, with the appropriate practice built in.

| A summary | A walkthrough |
|---|---|
| Shorter than the source | Longer than the source |
| Assumes the notation | Defines every symbol before use |
| States results | Derives them, one algebraic move per line |
| Illustrative examples | Examples sized to redo by hand, arithmetic verified |
| You read it | You work through it, then test yourself |

---

## What it produces

A single markdown file, structured the same way every time:

```
Frontmatter + header  →  what you'll be able to DO by the end
The map               →  the 4-8 concepts and how they connect
Math toolbox          →  every symbol, how to say it aloud, a tiny worked example
Concept sections      →  problem → intuition → formula → derivation →
                         worked example → your turn → where it breaks → in the code
Putting it together   →  one end-to-end example through every concept
Cheat sheet           →  one page, formulas only, for rewriting from memory
Check yourself        →  recall / compute / explain / transfer / discriminate
Sources               →  real citations, with status flags
Answers               →  full working, not just final values
```

**See it:** [`examples/lesson-07-decision-trees-walkthrough.md`](examples/lesson-07-decision-trees-walkthrough.md) - an abridged sample covering entropy end to end.

---

## Why it's shaped this way

Two of the design choices here are mine and build upon the way I study and the tools I use.

### It targets Obsidian, because that is where I study

I keep my notes in [Obsidian](https://obsidian.md), I use it daily, and I recommend it to anyone studying technical material. Or any material, to be honest. Three things earn it that recommendation:

- **The notes are plain markdown files on your disk.** No proprietary format, no lock-in, no export step. A walkthrough this skill writes is a `.md` file you own, and it stays readable in any text editor a decade from now. This seems nice to have until some cloud software locks you out of your notes - and I've had this happen.
- **LaTeX renders natively.** `$H(S) = -\sum_i p_i \log_2 p_i$` becomes real notation in the reading view. For maths-heavy material that is the whole ballgame, and it is why every formula this skill emits is LaTeX rather than a picture or a code block.
- **It is built for editing, not just reading.** You annotate, correct, and extend a walkthrough as you work through it. Wikilinks connect a lesson to the one before it, so a course becomes a graph instead of a pile of files. There are also plenty of editing tools and addons.

So the output is written for that workflow on purpose: YAML frontmatter, `$...$` and `$$...$$` maths, callouts for intuitions and warnings, answers in collapsed callouts so you cannot see them before you try, and `[[wikilinks]]` back to the previous lesson. It drops into a vault unmodified. [`check_obsidian.py`](skills/learning-walkthrough/scripts/check_obsidian.py) exists for one reason: a formula that does not render is a formula you cannot copy onto paper.

None of that locks you in. It is still just a markdown file, and it opens anywhere. 

### It is built for working by hand, because that is how I learn maths

I learn a mathematical idea by writing it out on by hand. I used to use actual pen and paper, but storing this information quickly became tedious and actually searching for something in hand-written notes is hell - so I moved over to a tablet. Copying a derivation line by line, doing the arithmetic myself, redrawing the diagram is what really makes the math click for me. Reading a proof and nodding along does not do it, and I do not think I am unusual in that.

That approach is why the format is what it is. Every example is sized for a pen rather than a machine:

- 4 to 10 rows of data, never a realistic dataset
- clean denominators, small integers, logs of powers of two
- one operation per line, with the substitution step written out, because not knowing which number goes where is the most common place to stall
- the reason for each algebraic move named in the margin
- every intermediate number computed in a script and verified before it is written down, so an hour of your paper time is never wasted chasing a typo
- a cheat sheet designed to be copied onto one sheet and then rewritten from memory

**An honest caveat, since this repo's own rule is to flag what is contested.** The popular claim that handwriting beats typing for notes did not cleanly replicate.[^4] I am not going to cite a shaky result to justify a preference. What *does* hold up is the reason the format works anyway: retrieval practice, the worked-example effect for beginners, and the generation effect all have solid support, and all three are things you get from working a problem rather than reading one. Do it by hand because the practice is well-founded. 

---

## The second skill: `slop-proofcheck`

Telling a model "length is not a cost" is the single most reliable way to summon padding. So the walkthrough gets read back by a second skill before it is handed over. It's also great for making the resulting docs much more readable, as LLMs have their own way of writing and once you go through enough LLM-generated text it might get a bit annoying.

It borrows its pattern list from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), but re-scopes it, because that framework is written for personal essays and a lesson is not an essay. The differences are the point:

| A general anti-slop pass says | For teaching prose |
|---|---|
| Vary your sentence and section structure | **Keep it identical.** The repeated `3.1-3.8` concept shape is deliberate; predictability lowers cognitive load |
| Cut headers over short sections, prefer prose to bullets | **Keep them.** The structure contract requires short labelled sections, tables and callouts |
| Preserve the writer's voice | There is no prior voice in a generated document. It targets a *register* instead |
| Ban `robust`, `leverage`, `significant`, `harness` | These are **defined terms** in ML and statistics. They are flagged for review, never auto-cut |

And three failure modes that only appear in explanatory writing, which a general pass does not look for:

- **Condescension.** `obviously`, `clearly`, `trivially`, `it's easy to see`. When a beginner does not find it obvious, these tell them the failure is theirs. That is the sentence that makes someone quit.
- **The magic step.** `it can be shown that`, `after some algebra`. A skipped step wearing the costume of an obvious one.
- **Synonym cycling**, promoted from style tic to hard error. A learner reading *feature*, *attribute*, *variable* and *predictor* for one object concludes there are four.

**Another house rule: no long dashes.** No em dashes (`U+2014`), no en dashes (`U+2013`), anywhere. Plain hyphens only. This is deliberately stricter than correct typography: the em dash has become a loud surface tell of machine-written text, and readers now discount prose on sight of it. I blame LLMs for making me hate the long dashes, but WCYD at this point.

Run it on anything, not just walkthroughs. Installed as a plugin the skill is namespaced; copied into `~/.claude/skills/` it is not:

```
/learning-assistant:slop-proofcheck README.md
/slop-proofcheck README.md
```

The mechanical half is a plain script with no dependencies, so it also runs on its own, in CI or a pre-commit hook:

```bash
python skills/slop-proofcheck/scripts/check_slop.py <file.md>
```

`cut:` hits are failures. `check:` hits are terms with a legitimate technical sense - confirm and move on. The judgment half, which no script can do, is in [`slop-patterns.md`](skills/slop-proofcheck/references/slop-patterns.md), along with a **keep list** of things that trip a slop detector and should survive untouched.

---

## Install

**Claude Code, as a plugin (recommended - this is the one you can update in place).** The repo is its own plugin marketplace:

```
/plugin marketplace add samalyarov/learning-assistant
/plugin install learning-assistant@learning-assistant
```

Both skills arrive namespaced, as `/learning-assistant:learning-walkthrough` and `/learning-assistant:slop-proofcheck`, and Claude still triggers them on its own from the descriptions.

**Updating.** No `version` is pinned in either manifest, so the plugin tracks the repository's commit SHA rather than a release number. Every push is picked up, and nothing needs bumping to publish a change. Pull the latest with:

```
/plugin update learning-assistant@learning-assistant
```

Or from a terminal, outside Claude Code:

```bash
claude plugin marketplace update learning-assistant
claude plugin update learning-assistant@learning-assistant
```

Claude Code refreshes the marketplace listing on its own once per session, but the installed copy advances only when you run the update, and a restart applies it. Use the fully qualified `plugin@marketplace` id - the bare name returns "not found", since the plugin and the marketplace share a name.

**Claude Code, as plain folders.** Skills are just directories, so copying them works too. You give up in-place updating, and have to re-copy by hand to pick up changes:

```bash
git clone https://github.com/samalyarov/learning-assistant.git
cp -r learning-assistant/skills/learning-walkthrough ~/.claude/skills/
cp -r learning-assistant/skills/slop-proofcheck ~/.claude/skills/
```

Project-scoped instead of personal: copy into `<your-project>/.claude/skills/`.

**Other runtimes** - Codex, Copilot CLI and Gemini CLI also read `~/.agents/skills/`:

```bash
cp -r learning-assistant/skills/* ~/.agents/skills/
```

**Claude.ai / API** - upload either skill folder through the Skills UI, or reference it through the Skills API.

Verify with `/skills` in Claude Code; both `learning-walkthrough` and `slop-proofcheck` should be listed.

---

## Use

It triggers on its own when you ask for something explained:

> Go through `my_notes.md` and the lecture PDF and explain all of this to me - I don't follow the maths.

> The lecturer didn't explain any of this. Walk me through lesson 5 step by step.

> Explain this notebook like you did for the last lesson.

Or call it directly:

```
/learning-walkthrough lesson 7 - use my_notes.md and lecture-07-slides.pdf
```

**What it assumes about you**, unless you say otherwise:

- You are a beginner at the underlying maths. Nothing starts with `recall that`.
- Thoroughness is the default. Length is not a cost.
- You will redo the examples on paper.
- You keep your notes in Obsidian.

---

## How it's built

```
.claude-plugin/
├── plugin.json                    # plugin manifest, so the repo installs as a plugin
└── marketplace.json               # marketplace manifest, so the repo serves itself

skills/
├── learning-walkthrough/
│   ├── SKILL.md                   # activation, the learner contract, non-negotiables, routing
│   ├── references/
│   │   ├── walkthrough-structure.md   # the section-by-section output contract
│   │   ├── obsidian-output.md         # LaTeX + Obsidian rendering rules and the traps
│   │   ├── math-toolbox.md            # building the prerequisites section
│   │   ├── worked-examples.md         # designing hand-scale examples; the arithmetic gate
│   │   ├── sourcing-and-rigor.md      # research order, citation standard, flagging bad claims
│   │   ├── notebook-mode.md           # when the deliverable is a Jupyter notebook
│   │   └── learning-science.md        # the evidence base, with its caveats
│   └── scripts/
│       └── check_obsidian.py      # validates the output renders in Obsidian
└── slop-proofcheck/
    ├── SKILL.md                   # the register, the two gates, what the pass must not do
    ├── references/
    │   └── slop-patterns.md       # the pattern catalogue, and the keep list
    └── scripts/
        └── check_slop.py          # flags hype vocabulary and phrasing
```

`SKILL.md` stays small - only its `description` is loaded until the skill triggers, and only the reference files it routes to are loaded after that. This is [progressive disclosure](https://agentskills.io/specification), and it's why the detail lives in `references/` rather than in one long file.

### Five rules that do most of the work

1. **The arithmetic gate.** Every number in every example is computed in a script and verified *before* it is written down. A confidently wrong intermediate value costs the learner an hour on paper and all their trust in the document.
2. **Never fabricate a source.** A plausible-looking citation is unfalsifiable to a beginner and propagates into their own work. If it can't be verified, it's marked unattributed.
3. **Render checks are mechanical.** `scripts/check_obsidian.py` catches the four LaTeX/Obsidian traps (space before a closing `$`, a raw `|` inside math in a table, an unspaced `$$` block, a callout missing its `> ` prefix) so nobody has to eyeball fifty formulas.
4. **Flag what's contested.** Superseded results, failed replications and textbook oversimplifications get said out loud, at the point of use - including in this skill's own evidence base.
5. **Thorough is not the same as padded.** "Length is not a cost" is the instruction most likely to turn into filler, so a second skill, [`slop-proofcheck`](skills/slop-proofcheck/SKILL.md), runs over the finished document and strips hype, puffery, cheerleading and `obviously`. It is calibrated for teaching prose, so it leaves alone the things a general anti-slop pass would wrongly cut: repeated section structure, short labelled sections, tables, and technical terms like `robust`, `leverage` and `significant`.

---

## Grounding

The format isn't invented. Each part maps to a documented effect, and the caveats are in [`learning-science.md`](skills/learning-walkthrough/references/learning-science.md):

| Feature | Principle |
|---|---|
| Math toolbox before the body | Pre-training (Mayer & Moreno, 2003) |
| Fully worked examples first | Worked-example effect (Sweller & Cooper, 1985) |
| Completion problems before unaided ones | Fading (Renkl & Atkinson, 2003) |
| "Your turn" and "Check yourself" | Testing effect (Roediger & Karpicke, 2006) |
| Questions mixing in the previous lesson | Interleaving (Rohrer & Taylor, 2007) |
| Cheat sheet rewritten from memory | Generation effect (Slamecka & Graf, 1978) |
| Intuition → concrete → formal | Concreteness fading (Fyfe et al., 2014) |

It also states what *doesn't* hold up - the worked-example effect reverses once you're no longer a novice,[^2] learning styles have no supporting evidence,[^3] and the popular "handwriting beats typing" result did not cleanly replicate.[^4] Working problems by hand is still well-founded, just for different reasons than the headline claims.


---

## Credits

`slop-proofcheck` is built on **[no-ai-slop](https://github.com/petergyang/no-ai-slop) by [Peter Yang](https://github.com/petergyang)**, MIT licensed. That project is the origin of the pattern vocabulary used here: binary contrasts, throat-clearing openers, faux-insight setups, colon reveals, importance puffery, weasel attribution, superficial `-ing` analysis, synonym cycling, fake-profound kickers, recap endings, and the banned-word list. Its portability test - *if the sentence would be equally true about something else, it is filler* - is the single most useful idea in this repo and is lifted from there directly.

What is different here is scope, not substance. no-ai-slop is written for personal essays, where the job is to sharpen a draft while preserving a human writer's voice. A generated lesson has no prior voice to preserve, and several of the essay rules actively damage teaching material, so the catalogue was re-scoped rather than copied: structural repetition is protected instead of flagged, domain terms like `robust` and `leverage` are exempted, and a set of explanation-specific failures was added (condescension markers, the magic step, restatement disguised as explanation, cheerleading, analogy stacking). Those changes are this repo's; the foundation is Peter Yang's.

If you write essays, posts, or anything with your own voice in it, use the original - it is the better tool for that job.

Grounding for the walkthrough format is credited inline in [`learning-science.md`](skills/learning-walkthrough/references/learning-science.md) and in the footnotes below.

---

## License

MIT - see [LICENSE](LICENSE), which also carries the upstream no-ai-slop copyright notice.

---

[^1]: Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4-58. <https://doi.org/10.1177/1529100612453266>
[^2]: Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1).
[^3]: Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3).
[^4]: Morehead, K., Dunlosky, J., & Rawson, K. A. (2019). How much mightier is the pen than the keyboard for note-taking? A replication and extension of Mueller and Oppenheimer (2014). *Educational Psychology Review*, 31.
