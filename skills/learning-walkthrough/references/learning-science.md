# Learning Science

Why the walkthrough is shaped the way it is. Read this when adapting the format to unusual material, or when the learner asks why the document works this way.

The skill's own rigor rule applies here: every claim below names its source, and where a popular result has failed to replicate or been narrowed, that is stated rather than smoothed over.

## The Format, And What Backs Each Part

| Walkthrough feature | Principle | Source |
|---|---|---|
| Math toolbox before the body | **Pre-training** - teaching component names and concepts before the process itself reduces load during the main explanation | Mayer's multimedia learning principles; Mayer & Moreno (2003) |
| Fully worked examples for a beginner | **Worked-example effect** - novices learn more from studying a solution than from attempting the problem | Sweller & Cooper (1985); Sweller, van Merriënboer & Paas (1998) |
| Completion problems between worked and unaided | **Fading** - removing support gradually beats removing it all at once | Renkl & Atkinson (2003) |
| "Your turn" and "Check yourself" | **Retrieval practice / testing effect** - retrieving beats rereading, and the benefit grows over time | Roediger & Karpicke (2006); Karpicke & Blunt (2011) |
| Questions mixing this lesson with the previous one | **Interleaving** - mixing problem types is harder now and retains better later | Rohrer & Taylor (2007) |
| Cheat sheet for rewriting from memory | **Generation effect** - self-produced material is remembered better than read material | Slamecka & Graf (1978) |
| "Explain it in your own words" prompts | **Self-explanation effect** - learners who explain steps to themselves while studying examples learn more | Chi, Bassok, Lewis, Reimann & Glaser (1989) |
| The Map before the detail | **Advance organizers** - a structure to attach new material to, given first | Ausubel (1960) |
| Intuition → concrete example → formal notation | **Concreteness fading** - start concrete, move to abstract, do not start abstract | Fyfe, McNeil, Son & Goldstone (2014) |
| Study spread over sessions, not one pass | **Spacing effect** - distributed practice beats massed practice | Cepeda, Pashler, Vul, Wixted & Rohrer (2006) |

The two techniques with the strongest evidence across the whole literature are **practice testing** and **distributed practice**; **rereading**, **highlighting**, and **summarisation** rated low in the same review despite being what most students actually do (Dunlosky, Rawson, Marsh, Nathan & Willingham, 2013, *Improving Students' Learning With Effective Learning Techniques*, Psychological Science in the Public Interest 14(1), 4-58).

This is why a walkthrough is not a summary. Producing a summary for a learner hands them the low-utility technique and does the work they needed to do themselves.

## Caveats On The Above

Honest reporting, per `sourcing-and-rigor.md`:

- **The worked-example effect reverses with expertise.** What helps a novice actively hurts a learner who already knows the material - the *expertise reversal effect* (Kalyuga, Ayres, Chandler & Sweller, 2003). A walkthrough is calibrated for a beginner. Once the learner is fluent, they should be doing problems, not reading explanations. Say so in the document.
- **Cognitive load theory's instructional predictions replicate well; its underlying working-memory model has been contested** in the literature. The practical guidance - do not make a beginner decode notation and concepts simultaneously - stands on its own empirical footing.
- **Advance organizers have modest effects,** not dramatic ones (meta-analyses since Ausubel report small positive effects). The Map section is cheap and helps orientation; do not oversell it.
- **Desirable difficulties are difficulties.** Making study harder in the right way improves retention (Bjork & Bjork, 2011), but learners consistently *rate* the harder method as less effective while performing better on it. Warn the learner: if the "your turn" problems feel worse than reading, that is the mechanism working.

## Learning Styles: Do Not Use Them

**The "visual learner / auditory learner" model has no supporting evidence and should not shape a walkthrough.** The specific claim tested - that matching instruction to a stated style improves outcomes, the *meshing hypothesis* - has repeatedly failed to find support (Pashler, McDaniel, Rohrer & Bjork, 2008, *Learning Styles: Concepts and Evidence*, Psychological Science in the Public Interest).

What is true is that **material has a best modality**: geometry wants diagrams, sequences want tables, causal chains want arrows. Choose the representation to fit the *content*, never to fit a label the learner has applied to themselves.

## "I Learn Best By Hand" - What The Evidence Actually Says

A learner who says this is describing something real, but the popular headline behind it is shakier than the practice it justifies.

**The shaky part.** Mueller & Oppenheimer (2014), *The Pen Is Mightier Than the Keyboard*, reported that longhand note-takers outperformed laptop note-takers. Morehead, Dunlosky & Rawson (2019) ran a direct replication and extension (Educational Psychology Review): performance did not consistently differ between groups, and a meta-analysis of the direct replications found only a small, non-significant effect favouring longhand. The result is best described as unresolved, not established.

Separately, van der Weel & van der Meer (2024, Frontiers in Psychology) found broader EEG connectivity during handwriting than typing. A 2025 commentary by Pinet and Longcamp notes real limits: the study measured neither learning nor memory, and the typing condition used single-finger input rather than ecologically valid touch-typing. Broader connectivity is not, by itself, better learning.

**The solid part.** What a learner doing maths on paper is actually doing is *generating* the steps themselves (generation effect), *retrieving* rather than recognising (testing effect), and working at a pace slow enough to notice where they get stuck (a desirable difficulty). Those effects are well supported, and none of them depend on the pen. Handwriting is a reliable *delivery mechanism* for effortful self-generated practice, and that is why it works.

**What this means for the walkthrough.** Design every example to be doable on paper - small numbers, all steps shown, nothing that needs a spreadsheet. That constraint is what forces the effortful step-by-step work the evidence supports. Do not claim in the document that handwriting is neurologically superior; claim that doing the arithmetic yourself is, which is both true and better supported.

## Source List

- Ausubel, D. P. (1960). The use of advance organizers in the learning and retention of meaningful verbal material. *Journal of Educational Psychology*, 51(5).
- Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In *Psychology and the Real World*.
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3).
- Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). Self-explanations: How students study and use examples in learning to solve problems. *Cognitive Science*, 13(2).
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4-58. https://doi.org/10.1177/1529100612453266
- Fyfe, E. R., McNeil, N. M., Son, J. Y., & Goldstone, R. L. (2014). Concreteness fading in mathematics and science instruction: A systematic review. *Educational Psychology Review*, 26.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1).
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331(6018).
- Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist*, 38(1).
- Morehead, K., Dunlosky, J., & Rawson, K. A. (2019). How much mightier is the pen than the keyboard for note-taking? A replication and extension of Mueller and Oppenheimer (2014). *Educational Psychology Review*, 31.
- Mueller, P. A., & Oppenheimer, D. M. (2014). The pen is mightier than the keyboard. *Psychological Science*, 25(6).
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3).
- Pinet, S., & Longcamp, M. (2025). Commentary: Handwriting but not typewriting leads to widespread brain connectivity. *Frontiers in Psychology*.
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition. *Educational Psychologist*, 38(1).
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3).
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science*, 35.
- Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6).
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving. *Cognition and Instruction*, 2(1).
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, 10(3).
- van der Weel, F. R., & van der Meer, A. L. H. (2024). Handwriting but not typewriting leads to widespread brain connectivity. *Frontiers in Psychology*, 14:1219945.
