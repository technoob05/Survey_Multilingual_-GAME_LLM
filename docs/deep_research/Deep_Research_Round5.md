
## nder the Shadow of Babel: A Position Survey on Linguistic Relativity and Strategic Deception in Multilingual LLM Games

EMNLPSubmitted: March 7, 2026

### Contents

* [Summary](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#summarySection)
* [Strengths](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#strengthsSection)
* [Weaknesses](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#weaknessesSection)
* [Detailed Comments](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#detailedSection)
* [Questions](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#questionsSection)
* [Overall Assessment](https://paperreview.ai/review?token=KrlmvAtiCvVHmUIixNXOrSl_P5cSXusHxvqBRkDz_kU#assessmentSection)

### Summary

This position survey argues that language can act as an “Algorithmic Sapir–Whorf Switch” for LLM agents, modulating strategic behavior, Theory-of-Mind (ToM), and deception across interactive, multi-agent games. It synthesizes evidence across seven game categories, highlights contradictory and null findings, and grounds cross-lingual divergences in two mechanistic accounts—the Semantic Hub and Translation Barrier hypotheses—while exposing evaluation fragility in multilingual LLM-as-judge settings. The paper culminates in a concrete proposal for a Cross-Cultural Agentic Sandbox Benchmark with controls for confounds, ensemble judging, adversarial code-switching, and intermediate-layer diagnostics.

### Strengths

* Technical novelty and innovation
  * Introduces a unifying conceptual lens (“Algorithmic Sapir–Whorf Switch”) that explicitly treats language as an independent variable in multi-agent strategic behavior, bridging behavioral observations with mechanistic hypotheses (Semantic Hub and Translation Barrier).
  * Connects multilingual miscalibration and late-layer realization failures to practical diagnostic and mitigation strategies (intermediate probes, dual-pass translation, constrained decoding).
  * Provides an actionable benchmark blueprint spanning confound control, code-switching red-teaming, collusion detection, and ensemble judging—moving beyond abstract calls for “better evaluation.”
* Experimental rigor and validation
  * Proactively surfaces and discusses negative and contradictory evidence (e.g., persuasion null result; volatile Arabic IPD distributions; clembench formatting vs strategy distinction) rather than over-claiming universal language effects.
  * Identifies and structures key confounds (tokenization, RLHF coverage, decoding hyperparameters, training distribution) with concrete ablation recommendations.
  * Highlights reliability concerns with multilingual LLM-as-judge (Fleiss’ κ ≈ 0.3) and proposes ensemble judging with checklist rubrics to restore moderate agreement.
* Clarity of presentation
  * Well-organized taxonomy of interactive environments and risks; clearly maps observations to mechanistic pillars with diagnostic tables and concrete examples.
  * Terminology is generally well-defined (e.g., formalization of Bayesian Belief Manipulation) and caveats are explicitly signposted (evidence “suggestive,” not causal).
* Significance of contributions
  * Addresses a timely, high-impact gap in multilingual agentic evaluation and safety, with practical implications for deployment, auditing, and policy.
  * The benchmark proposal, if realized, could materially improve cross-lingual validity and robustness of agentic LLM evaluation.k9

### Questions for Authors

1. Can you specify a pre-registered diagnostic protocol for distinguishing Semantic Hub vs Translation Barrier failures (layers to probe, probe models, acceptance criteria), and how you will validate it across at least two distinct model families?
2. How will you mitigate bias introduced by the proposed self-translation step in ensemble judging (e.g., evaluate both with and without self-translation; include human bilingual adjudication; use professional translation baselines)?
3. For IPD strategy classification, can you report or recommend language-wise calibration curves, confidence intervals, and human-validated error analyses (e.g., confusion between TFT variants) to strengthen classifier validity?
4. Which minimal viable subset of your benchmark design (languages, game genres, adversaries) do you recommend for first release to balance coverage and cost? What concrete auditing of RLHF coverage will be feasible?
5. For BBM measurement, how will you assess intentionality robustly without relying on potentially unfaithful CoT? Would counterfactual utterance generation or constrained rationales be considered?
6. Several cited results are from anonymized or forthcoming work; can you provide a supplementary registry with persistent identifiers and public artifacts to ensure traceability and reproducibility?

### Overall Assessment

This is a thoughtful and ambitious position survey that addresses an important and under-explored intersection: multilinguality, strategic behavior, and safety in agentic LLMs. Its key contributions are a coherent framing that unites behavioral findings with mechanistic hypotheses, a candid integration of contradictory evidence and confounds, and a detailed, practical benchmark proposal that, if realized, could materially improve multilingual agent evaluation. The main limitations are the lack of new controlled experiments, reliance on preliminary or under-documented evidence for some mechanistic claims, and occasional over-reliance on weak evaluators (LSTM strategy classifiers, single-judge LLM scoring) in the surveyed literature. Nonetheless, the synthesis, rigor of caveating, and concreteness of proposed methods make this work valuable to the EMNLP community. I recommend acceptance as a position/survey contribution, contingent on tightening traceability to sources, clarifying diagnostic protocols, and tempering mechanistic claims where replication is limited.
