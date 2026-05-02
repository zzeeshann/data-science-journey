# Improvements

*Ten numbered points for the next investigation's planning brief. Each is a 2–4 sentence note on what this project would do differently if starting over. Not a self-criticism document — a checklist for the next time.*

*The lessons fall into three loose categories: methodological discipline (1–4), measurement choices (5–8), and process discipline (9–10). The most load-bearing single point is #1; the rest live downstream of it.*

---

1. **Write the unit of analysis at the top of every session brief, in one sentence, before any code runs.** The single biggest lesson the project produced. *"This session measures one number per country."* Or *"This session measures one number per paragraph pair."* If the unit shifts mid-session, the question has shifted with it, and the framing needs to acknowledge that. The mistake this catches — described in [Chapter 10](book/chapter_10.md) — is the country-scale residual question and the paragraph-pair cosine work being treated as if they answered the same question when they didn't.

2. **Build the statistical bridge before claiming the claim.** Whenever a session would link two units (countries to paragraphs, individuals to texts, sources to outcomes), the bridge is a separate piece of the brief — a dataset that has both units in it, an analysis that regresses one against the other. Without that, the link is rhetorical. The Session 11 *bridge grep before commit* habit — every chapter sentence that connects findings should have a corresponding session record entry showing the statistical link — is the verification side of this.

3. **Distinguish exploratory sessions from confirmatory ones up front.** Sessions 4 and 7 were exploratory; the question was *"what does the data look like?"* and the result wasn't a pre-registered prediction. Sessions 8 and 9 were confirmatory; predictions were written down and the data either supported or rejected them. Both modes are valid. Marking which is which on the brief — and not retroactively claiming exploration was confirmation — keeps the epistemic posture honest.

4. **Status-note hypotheses dated and incrementally, in the plan file, after every session that touches them.** The four hypotheses in [`research_plan_wholeness.md`](research_plan_wholeness.md) drifted between original wording and what was actually tested across nine sessions, without the plan being patched until Session 11's audit caught it. A dated status note appended after every session that touches a hypothesis would have surfaced the drift early. Don't rewrite the original wording; preserve it and append.

5. **Verify what kind of unit a numbering scheme refers to before treating cross-source comparisons as meaningful.** Session 8's catalogue-vs-position discovery — KTU 1.12 is a museum index, Faulkner's Spell 12 is a twentieth-century scholarly numbering, Gilgamesh Tablet 12 is an appended Sumerian source distinct from the eleven-tablet main work — surfaced this the hard way. A digit isn't a structural position. Spend a verification session on primary sources before the analysis session, and require disambiguating provenance in the corpus's citation header.

6. **Run a sensitivity check with at least one heavier embedding model.** The entire text-level body of evidence used `all-MiniLM-L6-v2` (22M parameters, 384-dim output, the small fast default). Whether a heavier model — `all-mpnet-base-v2`, or a 2026-class sentence transformer — would shift the cosines enough to change the conclusions is unverified. The signal of interest doesn't have to be re-tested with every model, but at least one positive finding (the Reddit↔James phenomenology resonance is the cleanest candidate) should be re-run on a stronger model as a robustness check.

7. **Plan sample sizes for the comparison, not the corpus availability.** Session 8 ran a 4-passage position-twelve set against an 11-passage null pool — the smallest n the project tested anywhere. The negative permutation result was clear enough, but a ten-text or twenty-text ancient corpus would have produced a more confident result either way. Decide what comparison the session is making, work out the n that comparison needs to be statistically interpretable, and *then* go find the corpus.

8. **Order corpus loading thoughtfully — first-loaded shapes the framing.** The Session 7 plan had Reddit; Reddit returned HTTP 403 and didn't load. The session ran on the three corpora that did load (TinW, Ackoff, James) and the cross-era resonance finding emerged from those three. If Reddit had been the first corpus loaded, the framing would likely have led with the Reddit↔James phenomenology pair — the cleanest signal in the entire project. Loading order is a methodological choice, not a logistical accident.

9. **Use the asymmetric-model-pair pattern for prose audits.** Sessions 1–5 were drafted by Sonnet-class models; Session 6 found a fabricated quote from one of those drafts when Opus 4.7 read it cold. Hallucination rates fall as model parameters and training compute rise; citation fabrication is one of the failure modes most sensitive to model size. For any prose that asserts a specific source quote, run a larger model over it before commit — the published evidence (HalluLens, Vectara hallucination leaderboard, Frontiers in AI 2025 survey) is consistent on this. Documented in [`sessions/session_06.md`](sessions/session_06.md).

10. **Cold-read every chapter once before commit.** Session 12's readability audit caught readability gaps that the original chapter commits didn't see because session and chapter were drafted in the same context. A 14-year-old reading the chapter for the first time has no inherited context; that's the bar. Build the cold-read in as a per-chapter step at end of session, not as a separate audit session months later. Scale-anchor every dense statistic on first use; glossary-anchor every technical term on first use.

---

## What's not on this list

A few things the audit considered and chose not to include:

- **Substantive lessons about the world.** *"Don't trust the dashboard"* and *"the residual is the interesting part when the model fails everywhere the same way"* are real lessons, but they're about the WHR-residual subject matter, not about doing data science better. They live in [Chapter 5](book/chapter_05.md) and [Chapter 6](book/chapter_06.md) where they belong.
- **Tooling-specific recommendations.** This list is model-agnostic and corpus-agnostic; it should be useful regardless of whether the next investigation uses Claude or a different model, Hugging Face or a different mirror, Colab or a different compute environment.
- **Forward-looking research questions.** The next investigation's *what* is the user's call. This list is about *how*, not what.

The list is one page on purpose. A planning brief that says *"do these ten things"* is more useful than one that says *"here are forty things to consider."*
