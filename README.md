# Learning Assistant - Agent Skills for Studying

Two [Agent Skills](https://agentskills.io/specification) for Claude:

- **`learning-walkthrough`** turns course material you don't understand into a study document you can actually work through - built from the ground up, every symbol named, every example small enough to redo on paper, every claim traceable to a real source.
- **`slop-proofcheck`** reads the finished document back and strips the tells of machine-written prose, without flattening it into generic polish.

Output is [Obsidian](https://obsidian.md)-ready: LaTeX maths, YAML frontmatter, callouts, and answers that stay collapsed until you open them.

---

## The problem

Ask an assistant to "explain this lesson" and you get a **summary** - material compressed for someone who already understands it. That is the opposite of what a learner needs, and it is also, empirically, one of the weakest ways to study: in the largest review of learning techniques, summarisation, rereading and highlighting all rated *low utility*, while practice testing and distributed practice rated highest.[^1]

This skill produces a **walkthrough** instead: material *expanded* for someone who doesn't understand it yet, with the retrieval practice built in.

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

## The second skill: `slop-proofcheck`

Telling a model "length is not a cost" is the single most reliable way to summon padding. So the walkthrough gets read back by a second skill before it is handed over.

It borrows its pattern list from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), then re-scopes it, because that framework is written for personal essays and a lesson is not an essay. The differences are the point:

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

**House rule: no long dashes.** No em dashes (`U+2014`), no en dashes (`U+2013`), anywhere. Plain hyphens only. This is deliberately stricter than correct typography: the em dash has become a loud surface tell of machine-written text, and readers now discount prose on sight of it. That costs more than the typographic nicety is worth, so it is enforced mechanically rather than left to judgment.

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
