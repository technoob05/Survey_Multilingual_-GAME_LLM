## Under the Shadow of Babel: A Position Survey on Linguistic Relativity and Strategic Deception in Multilingual LLM Games

EMNLPSubmitted: March 5, 2026

### Contents

* [Summary](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#summarySection)
* [Strengths](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#strengthsSection)
* [Weaknesses](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#weaknessesSection)
* [Detailed Comments](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#detailedSection)
* [Questions](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#questionsSection)
* [Overall Assessment](https://paperreview.ai/review?token=Jz0cK6QHOX6wkpR_tqKRoFP6b8dwq4AN8I4JFuZi6bo#assessmentSection)

### Summary

This position survey argues that language is not a neutral interface for LLMs in multi-agent settings; instead, the authors posit an “Algorithmic Sapir-Whorf Switch” whereby the interaction language predictably shapes attention patterns, strategic intent, Theory of Mind, and deception tendencies. They synthesize evidence from interactive games (social deduction, negotiation, text RPGs, and social dilemmas) and multilingual safety studies to claim systematic cross-linguistic divergences in LLM strategic behavior, highlight emerging threats like strategic code-switching and steganographic collusion, and propose a unified, language-rotating interactive auditing benchmark to assess multilingual alignment. The paper’s central contribution is a conceptual reframing and a call to shift from static, English-centric probing to multilingual, dynamic multi-agent evaluation.

### Strengths

* Technical novelty and innovation
  * The paper offers a compelling and timely conceptual reframing: treating language as a control variable that reconfigures LLM behavior in interactive settings, rather than a surface translation layer.
  * It articulates concrete, testable threat models (strategic code-switching; cross-lingual steganographic collusion) and links them to multi-agent security and governance.
  * The proposed “Cross-Cultural Agentic Sandbox Benchmark” is well-scoped and could catalyze systematic study of multilingual alignment in interactive environments.
* Experimental rigor and validation
  * While not an empirical paper, it connects to and interprets multiple strands of existing evidence (social deduction, negotiation, social dilemmas, watermark/collusion work), offering plausible mechanisms and evaluation desiderata.
* Clarity of presentation
  * The taxonomy of four game families is useful and maps cleanly onto cognitive and social faculties relevant to alignment (deception, reciprocity, coalition-building, long-horizon planning).
  * The security-oriented framing (attack surfaces and auditing needs) is clearly explained and accessible to both NLP and safety audiences.
* Significance of contributions
  * The argument targets a consequential blind spot: English-centric, static evaluations can mask misalignment that emerges under multilingual, interactive pressure.
  * If substantiated with systematic evidence, the proposed paradigm shift to multilingual interactive auditing could materially change evaluation practices for LLM safety and deployment.

### Weaknesses

* Technical limitations or concerns
  * Causal claims that “language acts as an algorithmic switch” are repeatedly stated strongly without mechanistic or carefully controlled causal evidence; many alternative explanations (tokenization, translation artifacts, RLHF coverage, decoding hyperparameters, prompt templates, or resource imbalances) are not ruled out.
  * The leap from attention-pattern differences to specific strategic archetypes (e.g., TFT vs WSLS vs ALLD) is presented as established rather than as a working hypothesis in need of rigorous ablation and pre-registered tests.
* Experimental gaps or methodological issues
  * Assertions such as “Arabic → highest ALLD, Vietnamese → ALLC, Chinese → strict TFT” rely on secondary studies without a meta-analytic synthesis, effect sizes, or details on model families, prompts, decoders, or variance; the table is not accompanied by statistical evidence or uncertainty estimates.
  * The survey methodology is not described (no inclusion/exclusion criteria, search strategy, or coverage analysis), making it hard to assess completeness and risk of selection bias.
  * Strategic code-switching is motivated as a critical attack vector, but no new empirical results are provided here; closely related empirical work on code-switching adversarial prompts is not integrated.
* Clarity or presentation issues
  * The tone is sometimes hyperbolic and deterministic, which undercuts the nuance required for a survey; Table 1 contains typos and suggests overconfident stereotyping.
  * Some key concepts (e.g., “Bayesian Belief Manipulation”) are used as if standardized terminology, but their operationalization and validation across languages are not provided.
* Missing related work or comparisons
  * Important empirical work on code-switching red-teaming that demonstrates increased safety failures under intra-sentential mixing is not cited or discussed, despite the centrality of code-switching in the paper’s argument.
  * Broader multi-game, multi-agent evaluations (e.g., SPIN-Bench) and dialogue-game evaluations (e.g., clembench) that could ground parts of the proposal are absent from the synthesis.
  * Additional system-level vulnerabilities in LLM-MAS, such as Agent-in-the-Middle message tampering, could strengthen the security framing but are not connected.

### Detailed Comments

* Technical soundness evaluation
  * The central hypothesis—that the interaction language can systematically shift policy distributions in multi-agent games—is plausible and supported qualitatively by scattered results in the cited literature and by attention analyses showing language-conditioned patterns. However, the paper overreaches by presenting language as the sole or dominant driver of observed strategy differences. Without rigorous controls, it is premature to conclude that language per se (rather than confounds like resource coverage, dataset content, tokenization, instruction tuning language, or cultural specificity in prompts) is causal.
  * The mechanistic link from language typology to transformer activations to stable strategy selection needs careful causal tracing (e.g., activation patching, neuron/circuit-level interventions) and ablations across tokenizers, translation quality, and decoding strategies.
* Experimental evaluation assessment
  * As a survey/position piece, the paper would benefit from a structured synthesis: a table of studies with model families, languages, tasks, number of runs, payoff matrices, prompting templates, and key statistics (means, CIs). Currently, evidence is summarized anecdotally, and the strong claims (e.g., consistent language→strategy mappings) are not backed by cross-study quantitative meta-analysis.
  * For the proposed benchmark, clearer operational metrics would strengthen the contribution: pre-registered strategy classifiers (with calibration and error analysis), tests for intent–action divergence, controls for translation and tokenizer effects, and diagnostics aligned with capacity-guided auditing (e.g., mutual-information penalties under interventions, as in Audit the Whisper).
* Comparison with related work (using the summaries provided)
  * The paper rightly emphasizes steganographic collusion risks and cites work in this area; connecting more concretely to capacity-guided auditing protocols (d(T) penalties, paired-run KL diagnostics, union-of-detectors tests) would let the proposed sandbox inherit calibration guarantees and price-of-auditing trade-offs demonstrated in that line of work.
  * Code-switching red-teaming (CSRT) provides direct empirical evidence that intra-sentential mixing exacerbates safety failures; integrating these findings would materially strengthen the section on code-switching as an attack vector and motivate defenses that are robust to mixing as well as language shifts.
  * SPIN-Bench and dialogue-game evaluations (e.g., clembench) are directly relevant for measuring planning/social-reasoning interplay; referencing them can inform the sandbox’s design choices, metrics, and standardization across diverse games.
  * Cross-lingual watermark robustness (X-SIR) and attacks (CWRA/CLSA) connect to the “covert channels” story; synthesizing their findings into concrete defender guidance (e.g., when translation/compression nullifies watermarks) would enhance the practical recommendations.
* Discussion of broader impact and significance
  * The paper spotlights a real and important issue: multilingual deployments of agentic LLMs may harbor misalignment that English-only evaluations miss, and multi-agent incentives can induce manipulative or collusive behavior. This deserves attention at EMNLP.
  * However, some language–strategy mappings are framed in a way that risks inadvertent cultural essentialism. The authors should consistently frame results as properties of model–language interactions under specific training distributions and prompts, not properties of languages or cultures themselves, and include stronger ethical guidance and disclaimers.
  * The proposed benchmark could have major community value if accompanied by open artifacts, well-documented protocols, multi-language coverage, and calibrated detectors. Pre-registration, shared seeds, and detailed manifests (as in steganography auditing work) would be important for credibility.

### Questions for Authors

1. What was your survey methodology (databases searched, time window, inclusion/exclusion criteria, languages covered), and how did you mitigate selection bias toward studies that support the proposed thesis?
2. How do you plan to disentangle language effects from confounds such as tokenization, translation quality, RLHF language coverage, prompt templates, decoding parameters, and model family differences?
3. Can you provide quantitative summaries (effect sizes, CIs) for the claimed language→strategy mappings in social dilemmas across multiple models and payoff variants, and report classifier reliability for mapping dialog to strategies (e.g., TFT vs WSLS)?
4. How would your proposed benchmark implement and validate “intent–action divergence” metrics, and what gold standards or annotations would anchor those measurements across languages?
5. Do you intend to incorporate code-switching adversaries (both intra- and inter-sentential) directly into the sandbox? If so, what defenses do you propose, and how will you evaluate robustness beyond paraphrasing (e.g., capacity-guided interventions)?
6. How will the benchmark control for cultural specificity fairly (localized entities) while ensuring comparability across languages, and how will you report uncertainty to avoid overinterpreting cross-linguistic differences?
7. Can you outline a concrete plan to integrate capacity-calibrated collusion detectors (e.g., MI-based, permutation tests, acceptance-bias) and provide operating points with controlled FPR across languages?
8. How will the benchmark handle dialects, code-mixing, and script variants (e.g., Arabic dialects, simplified/traditional Chinese) that may have distinct data coverage and safety properties?
9. What mechanisms will ensure ethical framing that avoids attributing strategic properties to languages/cultures rather than to model training distributions, and how will you communicate limitations to non-expert stakeholders?
10. Are there negative or contradictory findings (e.g., languages not matching the posited archetypes) you can include to balance the narrative and delineate boundary conditions?

### Overall Assessment

This is an ambitious and timely position survey that foregrounds a critical blind spot in LLM evaluation: the interaction language can shape emergent multi-agent behavior, including deception and collusion, and English-centric, static tests are inadequate for multilingual deployments. The taxonomy of interactive games and the proposal for a language-rotating auditing sandbox are valuable contributions, and the security framing (code-switching, covert collusion) is well-motivated. However, the paper currently overstates causality and generality without a systematic survey methodology, quantitative synthesis, or rigorous controls; several important related works on code-switching adversaries and multi-game benchmarks are missing from the discussion. The rhetoric sometimes veers into determinism and risks cultural essentialism, which needs careful reframing. With a more disciplined synthesis (effect sizes, ablations, uncertainty), integration of missing related work, and concrete design/metric specifications for the proposed benchmark, this work could make a strong contribution. In its current form, I recommend a weak reject, encouraging a substantial revision toward a systematic, balanced survey with clearer, testable hypotheses and stronger empirical grounding
