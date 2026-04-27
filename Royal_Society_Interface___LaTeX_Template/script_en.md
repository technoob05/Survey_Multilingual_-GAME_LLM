# Presentation Script (English) — Babel's Machines

**Venue:** *Interface Focus* theme issue talk / RSIF symposium
**Audience:** interdisciplinary — life, physical, and social scientists studying machine behaviour
**Duration:** ~17 minutes (21 slides, ~45–55 s each)
**Tone:** plain-spoken, honest about uncertainty, foreground contradictions

---

## Slide 1 — Title
**[0:00 – 0:40]**

"Good morning. Thank you to the organisers — Professors Han, Rahwan, Song, and Perc — for putting this theme issue together, and for the invitation.

I'm Dao Sy Duy Minh, from the University of Science at VNU-HCM. Today I want to walk you through a perspective my co-author Vu Nguyen and I have written for *Interface Focus*.

The argument in one sentence: when LLMs act as agents in multilingual environments, language is not a passive medium. It actively reshapes their cooperation, deception, and theory-of-mind performance. The right tools to study this come from evolutionary game theory and cultural evolution — not engineering benchmarks alone."

## Slide 2 — Roadmap
**[0:40 – 1:10]**

"Four parts. First, why language matters for the machine-behaviour programme. Second, what these agents actually do across languages — including the contradictions. Third, why — the architectural mechanism, and the causal loop we still need to close. Fourth, so what — the evolutionary frame, governance, and four falsifiable predictions."

---

## Part 1 — Why language matters

## Slide 3 — LLMs no longer just produce text. They act.
**[1:10 – 2:20]**

"Let me start where Rahwan and colleagues started in their 2019 *Nature* paper. The argument: AI systems have entered a regime where they can no longer be studied purely as engineered artefacts. They behave. They have an ethology.

LLMs in 2026 are exactly that case. They negotiate trades. They cooperate and defect in iterated games. They deceive in social-deduction games. They manage budgets in auctions and collaborate on hours-long tasks.

The right tools to study them are tools we have built over a century for studying biological and social behaviour: evolutionary game theory, the statistical physics of cooperation in the tradition of Perc, cultural evolution in the tradition of Boyd, Richerson and Henrich, and the cognitive science of theory of mind. This is an ethology, not a benchmark."

## Slide 4 — Our claim, in one sentence
**[2:20 – 3:30]**

"Inside that programme, our perspective makes one specific claim. The language an LLM agent operates in systematically reshapes its strategic behaviour, theory-of-mind performance, and prosocial defaults. Following Wang and colleagues, we call this the *Algorithmic Sapir–Whorf Switch*.

Two things to be clear about. First, this is *not* the strong Whorfian claim that language determines thought. It is the weaker, mechanistically grounded claim that language-specific representations inside the model modulate the policies the model executes in interactive environments. Second, the claim is empirical, not metaphysical. We devote real space to evidence against it.

The contribution we are trying to make is to bridge three traditions: NLP empirics on the behavioural side, mechanistic interpretability on the architectural side, and evolutionary game theory and cultural evolution on the population side."

---

## Part 2 — What LLM agents do

## Slide 5 — Seven families of interactive games
**[3:30 – 4:00]**

"Before we can talk about behaviour, we need a substrate. The literature has converged on roughly seven families of interactive environments — social dilemmas, negotiation, persuasion and auction, social deduction, cooperative communication, open-world games, and dialogue games like clembench.

The point I want to flag is the take-away on the slide: every one of these families has been run multilingual, and every one of them has reported language-dependent divergence. That convergence across very different task structures is what makes the phenomenon worth taking seriously."

## Slide 6 — Same model, same game, different language → different strategy
**[4:00 – 5:10]**

"Let me show one set of numbers. This table aggregates iterated Prisoner's Dilemma strategy distributions across four model families and five languages. I want to be transparent about what this is and isn't. These are *descriptive proportions*, not a meta-analytic estimate. Prompts, payoff matrices, horizon disclosure, and opponent policies all vary across studies. The original studies report classifier reliability between 0.78 and 0.91, and the qualitative ranking is stable under threshold sweeps — so we trust the rank order, not the exact percentages.

Three patterns. Arabic produces *both* the highest unconditional cooperation *and* the second-highest unconditional defection — a bimodal distribution, not monotonic competitiveness. Vietnamese subverts the collectivist prior; one model collapses to two percent cooperation. Chinese favours Win-Stay-Lose-Shift over Tit-for-Tat — outcome-driven rather than reciprocity-driven. And model-family effects swamp language effects: GPT-4o is hawkish, Mistral is dovish, regardless of language."

## Slide 7 — LLMs are "nicer than humans" — in a very specific regime
**[5:10 – 6:20]**

"Sitting on top of all that variation is a baseline finding I think this audience will care about. Across recent studies, frontier LLMs default to prosocial play at rates well above typical human players in iterated Prisoner's Dilemma.

I want to bound this claim immediately. Fontana and colleagues' result holds for a cooperative-payoff matrix where the temptation to defect equals five and mutual cooperation equals three, with the horizon disclosed at 100 rounds, against random adversaries with substantial defection probability. The regime where this prosocial default holds is: cooperative-payoff dominance, known horizon, exploitable opponent.

The picture inverts outside that regime. Pure-competitive games like rock-paper-scissors? LLMs play *deeper* than humans. Unknown horizon? Cooperation universalises across all languages — framing swamps language. So the prosocial default is real but conditional. With that bound in place, the finding is still striking: LLMs are cooperating *before* the Axelrodian scaffolds — repeated interactions, reputation, punishment — operate at all. We come back to that in the evolutionary section."

## Slide 8 — Foregrounding contradictions
**[6:20 – 7:30]**

"A responsible perspective bounds its own claim. Four findings push back against a strong reading of linguistic relativity here.

Biswas and colleagues, in a controlled CHI 2025 study of cross-lingual persuasive co-writing, found prior LLM-language exposure shifts *usage* but not aggregate persuasiveness. What mattered to donors was their belief about whether the ad was AI-generated.

Madmoun and Lahlou last October found that adding a single one-word communication channel raises Stag-Hunt cooperation from zero to ninety-six point seven percent — across every language tested.

Buscemi and colleagues, and Loré and Heydari before them, find that when game horizons are unknown, cooperation universalises across languages. And Vietnamese 'defection' under low stakes sometimes turns out to be arithmetic miscomprehension, not strategy.

The reading is: language effects exist, but they interact with framing, stakes, communication channels and tasks. They are not a fixed cultural dial."

---

## Part 3 — Why (mechanism)

## Slide 9 — Two mechanisms account for the cross-lingual gap
**[7:30 – 8:40]**

"On to mechanism. The dominant account in mechanistic interpretability has two parts. The Semantic Hub Hypothesis from Wu and colleagues at ICLR 2025 says multilingual models project heterogeneous linguistic inputs into a centralised, English-dominant intermediate hub. The causal evidence is striking: English-derived activation steering vectors — sentiment vectors, for example — work just as well on Spanish or Chinese inputs as they do on English. The hub is causally engaged.

The Translation Barrier Hypothesis from Bafna and colleagues complements this: many multilingual failures are not upstream reasoning failures but late-layer realisation failures — the model reaches the right conclusion internally and then fails projecting into the target language.

Together they predict the calibration crisis on the right of the slide. Expected Calibration Error is roughly five times higher in non-English than English on the MEGA benchmark — Ahuja's 2022 paper across XGLM, BLOOM, and PaLM at 15-bin equal-width. Models are confidently wrong in exactly the languages where reasoning is weakest."

## Slide 10 — We don't claim a monopoly
**[8:40 – 9:40]**

"We are explicit in the paper that this two-mechanism account is not the only architectural story available. Three alternatives deserve serious treatment.

Pires, Schlinger and Garrette showed back in 2019 that multilingual BERT supports zero-shot transfer between typologically distant languages but exhibits *systematic* deficiencies on certain language pairs — suggesting partially separated language-specific microcircuits alongside any shared hub. Conneau and colleagues on XLM-R, and Xue and colleagues on mT5, show that scale alleviates but does not eliminate cross-lingual subspace interference. And Wendler and colleagues, in *Do Llamas Work in English?*, push the claim further: Llama decoders pass through a latent intermediate that is statistically *closer to English* than to the input language.

The cleanest test we know of involves language-prioritised models. CT-LLM was trained with eight hundred billion Chinese tokens against three hundred billion English; TigerLLM was built for Bangla. If the Semantic Hub asymmetry is principally about training data and not architecture, those models should *invert* the asymmetry — better calibration and stronger ToM in their priority languages than in English. That is an immediately runnable empirical test."

## Slide 11 — Closing the loop — from representation to behaviour
**[9:40 – 10:40]**

"A reasonable critic will point out that everything in the previous two slides is *representational*. We have evidence that intermediate representations differ across languages and that they can be manipulated. We have separate evidence that behaviour differs across languages. The link between the two is currently inferential.

Several recent results in interpretability supply both the methodology and the precedent for closing this loop directly. Chen and colleagues showed in 2023 that spatial representations in DeBERTa and GPT-Neo have *causal* effects on next-token prediction, not merely correlational structure. Zhang's 2026 work on world models shows latent state variables are linearly decodable *and* causally engaged. And layer-resolved tools — LogitLens4LLMs, the four-stage trajectory of arithmetic processing in Llama-3, and the early-syntax / late-semantics dissociation in GPT-2 — supply the methodology.

The natural next experiment, which we encode in our extended P2: derive an activation-steering vector from English IPD traces of cooperative versus defective play; apply it to the same model running an Arabic or Vietnamese IPD prompt; measure whether the strategy distribution shifts in the predicted direction. A positive result converts the Semantic Hub from a representational curiosity into a behavioural lever."

---

## Part 4 — Theory of mind and moderators

## Slide 12 — Bilingual children get better at ToM. LLMs get worse.
**[10:40 – 11:50]**

"Theory of mind. Cooperation and deception both require it. The human baseline points one way: bilingual children, work by Kovács and by Goetz tells us, pass false-belief tasks *earlier* than monolingual peers — the executive demands of code-switching scaffold the same control machinery that ToM recruits. The implicit prediction for machines: a multilingual model should be a *stronger* ToM agent than a monolingual one.

LLMs show the opposite pattern. The XToM benchmark from Chan and colleagues shows what they call a 'pronounced dissonance': models that excel at multilingual language understanding nonetheless show ToM accuracy varying sharply across languages on the same items. GPT-4o has an eleven-point gap between Japanese and Chinese on XFANToM. LLM-Hanabi confirms that *first-order* ToM is the stronger predictor of cooperative success, and degrades in lower-resource languages.

A construct-validity caveat: Ullman in 2023 and Sap and colleagues in 2022 have argued that LLM ToM benchmarks may reflect surface pattern-matching rather than mental-state representation. We read cross-lingual ToM *differences on parallel items* as the more interpretable signal here — even if absolute ToM accuracy is contestable, asymmetry across languages is well-defined regardless."

## Slide 13 — Language is one modulator
**[11:50 – 12:50]**

"Three recent studies establish that language is one modulator among several whose interactions deserve joint study.

Ong and colleagues this year show that representation-engineering steering of Big-Five Agreeableness reliably modulates Iterated Prisoner's Dilemma cooperation — and increases exploitation susceptibility. Direct evidence that internal representations *can* causally steer cooperative play.

Nishimoto and colleagues this February documented a U-shaped relationship between communication delay and cooperation — agents *spontaneously* begin to exploit slower partners, with no language change at all. Infrastructure shapes behaviour.

And Jiang and colleagues last March show that human cooperation against an agent depends on the *declared identity* of that agent. Language is one of several signals that frame agent identity.

The methodological point: any clean test of linguistic relativity must hold these three moderators — internal-trait steering, communication infrastructure, partner-identity framing — explicitly constant."

---

## Part 5 — Evolutionary frame

## Slide 14 — LLM cooperation doesn't fit Axelrod's mould
**[12:50 – 14:00]**

"Now the move I think will most interest this audience. Thirty years of work after Axelrod tells us cooperation is an *achievement* — selected over a history of repeated interactions, reputation, punishment, network reciprocity. Nowak's five rules. Perc's statistical physics.

LLMs do not fit this mould. They arrive at their first interaction *pre-cooperative*. Pretraining and RLHF act as a form of *cultural inheritance* — pretraining corpora are cumulative cultural products of millions of human authors, and RLHF injects a layer of selected human preferences. The agents exhibit *culturally inherited cooperation*, not evolved reciprocity.

This is most naturally read as a Boydian–Richersonian cultural-evolution process applied to a new substrate. And the corollary is testable: languages whose pretraining corpora carry more cooperative discourse should yield more cooperative play. The corpus-audit machinery already exists. That hypothesis becomes our prediction P1."

## Slide 15 — The WEIRD problem and the transmission bottleneck
**[14:00 – 14:50]**

"Two further moves on the evolutionary side. First, the WEIRD problem. Pretraining corpora are massively skewed toward Western, Educated, Industrial, Rich, Democratic sources. Henrich, Heine and Norenzayan's 2010 paper, Muthukrishna and colleagues' 2020 follow-up, both show WEIRD populations are statistical *outliers* on individualism, analytic thinking, fair-procedure framings. If LLMs inherit cooperation from these corpora, they encode WEIRD norms while presenting as universal. Multilingual deployment risks normative imposition, not just performance gaps.

Second, machine populations are themselves now subject to cultural evolution. Distillation is high-fidelity oblique inheritance. RLHF preferences are a form of selection. If the transmission bottleneck is largely English — because English is the lingua franca of benchmarks and of RLHF annotators — then non-English behavioural traits drift independently. The English-Arabic gap in TCG-Bench at thirty-two-billion parameters is consistent with a drift that scale alone does not correct."

---

## Part 6 — Society and governance

## Slide 16 — Three societal consequences — already shipping
**[14:50 – 15:40]**

"The societal stakes are not abstract. UlizaLlama provides health information in Swahili, Yoruba, Hausa, isiXhosa and isiZulu. Aya Expanse covers twenty-three languages including Vietnamese. Bhashini routes public-sector queries through multilingual LLMs that millions of Indian citizens depend on. Stanford HAI's policy programme has explicitly mapped the language gap as a structural issue.

Three consequences. First, unequal institutional quality: a fivefold ECE gap means public-facing agents in the Global South will systematically offer more confidently wrong advice to populations with fewer alternatives. Second, linguistically uneven attack surfaces: Code-Switching Red-Teaming gets a forty-six-point-seven-percent boost in attack success by mixing languages at token level; Agent-in-the-Middle attacks exploit inter-agent channels in multilingual systems. Third, co-evolution: LLM outputs re-enter human discourse, making the cultural-inheritance loop bidirectional."

## Slide 17 — Three governance levers
**[15:40 – 16:30]**

"The framework gives us three actionable levers, none of which require a research breakthrough.

Benchmark diversification: pair safety benchmarks like M-ALERT with interactive multi-agent benchmarks like clembench, MultiAgentBench and TCG-Bench, so that language-induced behavioural gaps and language-induced safety gaps are reported jointly, not as two separate literatures.

Multilingual RLHF coverage standards: annotator-pool composition by language and dialect on every model card. We propose, as a starting point, a minimum coverage threshold of at least five percent of preference labels per language, with documented dialectal stratification, for any model deployed across more than five official languages.

And audit standards for multi-agent deployments: code-switching adversarial probes and Agent-in-the-Middle threat models become a default test bed for any multilingual multi-agent product, the way prompt-injection probes already are for single-agent ones.

What is missing is the institutional infrastructure that makes these routine."

---

## Part 7 — Predictions

## Slide 18 — Four predictions
**[16:30 – 17:00]**

"Four predictions, each formulated to be falsifiable with currently available methods.

P1, corpus-cooperation correspondence: cooperative-discourse density in pretraining corpora, measured via prosocial speech-act n-grams calibrated against hand-annotated gold sets, should rank-correlate with IPD cooperation rates across languages. Closed corpora are a real obstacle; we recommend three workarounds — open-data models like CT-LLM and TigerLLM, proxy corpora matched on Common Crawl shards, or controlled small-model pretraining runs. Falsifier: Spearman rho indistinguishable from zero across at least eight languages.

P2, hub probe with behavioural readout: pre-registered probes at L-over-three and two-L-over-three classify failures into hub-level and realisation-level. Then — and this is the new step — apply an English-derived activation-steering vector to a non-English IPD prompt and measure the resulting strategy shift. Positive result converts representation into behaviour; negative result forces us to look beyond the hub.

P3, distillation drift: a controlled distillation chain should show traits propagating with high fidelity in English but degrading in lower-resource languages.

P4, evaluation reliability ceiling: multilingual LLM-as-Judge with three-or-more heterogeneous judges, self-translation, and checklist rubrics should raise Fleiss' kappa above point-five. If it saturates below, cross-lingual quantitative work needs bilingual human adjudication, not better aggregation."

---

## Part 8 — Conclusion

## Slide 19 — Five things to remember
**[17:00 – 17:30]**

"Five take-aways. Language is an active modulator, not a passive medium. The mechanism is architectural, not cultural-essentialist. Cooperation here is culturally inherited, not evolved — with WEIRD corollaries that multilingual deployment makes urgent. Contradictions are informative, not embarrassing — they bound the claim. And the four predictions turn synthesis into a research agenda — closing the representation-to-behaviour loop is the most urgent of them."

## Slide 20 — Where this sits
**[17:30 – 17:50]**

"Briefly, where this sits. We see the perspective as continuous with Rahwan on machine behaviour as a discipline, with Han on evolutionary game theory for emergent multi-agent systems, with Perc on statistical physics of cooperation, with Boyd, Richerson and Henrich on cultural evolution as transmission, and with Axelrod and Nowak on cooperation without design. The distinct contribution is treating language as a modulating variable in machine ethology, reframing 'nicer than human' as cultural inheritance, and supplying an immediately falsifiable agenda."

## Slide 21 — Thank you
**[17:50 – 18:00]**

"Machine populations now offer a new — uncomfortably consequential — empirical substrate for the science of cooperation. Thank you. I look forward to discussion."

---

## Anticipated Q&A — short answers

**Q: Why prioritise the cultural-inheritance reading over a simpler 'corpus statistics → behaviour' reading?**
"On our view, they are the same reading. Cultural inheritance *is* transmission of behavioural patterns through corpus statistics. The reframing is rhetorical: it makes the empirical predictions interpretable in the same vocabulary that this audience already uses for human cooperation."

**Q: How do you isolate pure language effects from tokenisation entropy?**
"You cannot, in a single experiment. The cleanest design holds the tokeniser constant — byte-level decoding, or a shared SentencePiece vocabulary — and varies the prompt language. Yong and Bach's low-resource-jailbreak work supplies the methodology."

**Q: Doesn't Diplomacy with CICERO already show competent cross-cultural play?**
"It shows competent play in English. To our knowledge, the same architecture has not been replicated multilingual under controlled conditions. P3 in our agenda is exactly that experiment."

**Q: Are language-prioritised models like CT-LLM really comparable, given different pretraining recipes?**
"They are not perfectly comparable. They are the cleanest *natural experiment* we currently have. A purpose-built ablation study would be better; CT-LLM and TigerLLM are what is on the table now."

**Q: The ToM gap might just reflect benchmark leakage in Japanese vs.\ Chinese.**
"It might. That is exactly Ullman's and Sap's concern. Our defence: we read cross-lingual *differences on the same items* as the more interpretable signal, regardless of absolute ToM scores. The asymmetry argument is robust to the construct-validity dispute."

**Q: Your governance numbers — 5% per language — feel arbitrary.**
"They are. We propose them as a starting point for community discussion, not as an evidence-based threshold. The contribution is the *form* of the recommendation — annotator composition reported on every model card with documented dialectal stratification — not the specific percentage. The community can converge on the right number."
