## Under the Shadow of Babel: A Position Survey on Linguistic Relativity and Strategic Deception in Multilingual LLM Games

EMNLPSubmitted: March 9, 2026

### Contents

* [Summary](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#summarySection)
* [Strengths](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#strengthsSection)
* [Weaknesses](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#weaknessesSection)
* [Detailed Comments](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#detailedSection)
* [Questions](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#questionsSection)
* [Overall Assessment](https://paperreview.ai/review?token=JlxxS_fnpuLhYS7D2HRqhWcBywzct4FjLGchJyi6RtU#assessmentSection)

### Summary

This position survey argues that language is not merely a surface variable but can systematically modulate large language models’ strategic behavior in interactive, multi-agent games. It synthesizes evidence across seven categories of multilingual LLM games, proposes complementary mechanistic accounts (Semantic Hub and Translation Barrier) for observed cross-linguistic divergences, examines multilingual vulnerabilities such as code-switching red-teaming and steganographic collusion, and highlights critical fragility in multilingual LLM-as-judge reliability. The paper culminates in a concrete proposal for a Cross-Cultural Agentic Sandbox with confound controls, ensemble judging, and intermediate-layer diagnostics.

### Strengths

* Technical novelty and innovation
  * Frames “language as an Algorithmic Sapir-Whorf Switch” for multi-agent strategic behavior, connecting interactive-game phenomena to mechanistic hypotheses (Semantic Hub and Translation Barrier).
  * Integrates representation-editing insights (e.g., Activation Addition, sparse steering) into the multilingual safety/agentic setting, articulating falsifiable pathways (intermediate-layer probes, layer-wise diagnostics).
  * Introduces a clean formalization for Bayesian Belief Manipulation and proposes CoT-free proxies (counterfactual utterance search, structured intentionality templates) to operationalize deceptive intent.
* Experimental rigor and validation
  * Takes contradictory evidence seriously (e.g., persuasion null result; Arabic bimodality; clembench formatting vs strategy) and foregrounds confounds (tokenization, RLHF coverage, decoding hyperparameters).
  * Proposes a methodologically careful benchmark design with matched tokenizer ablations, RLHF coverage audits, pre-registered classifiers/metrics, and per-language intent–action gold standards.
  * Emphasizes evaluator reliability, documenting multilingual LLM-as-judge collapse and offering ensemble and calibration-aware mitigations.
* Clarity of presentation
  * Organizes the landscape via a clear seven-category taxonomy and an orienting figure that ties together threats, mechanisms, and evaluation.
  * Provides concrete, actionable benchmark design recommendations (languages, tasks, cost estimates, annotation protocols), making the position practically useful.
* Significance of contributions
  * Addresses a pressing and underexplored gap: multilingual, interactive, and adversarial settings where safety alignment often fails.
  * Bridges disparate subfields—multilingual robustness, agentic evaluation, mechanistic interpretability, and red-teaming—into a coherent research agenda that can guide benchmark builders and safety practitioners.

### Weaknesses

* Technical limitations or concerns
  * Several mechanistic claims (e.g., English-dominant hub, ActAdd scaling differences) are presented with caveats but remain speculative without stronger, replicated evidence; risk of over-attribution to hub/barrier without rigorous ablations.
  * The proposed distinction between upstream vs. late-layer failures needs sharper, quantitative acceptance criteria and broader architectural replication to support the central narrative.
* Experimental gaps or methodological issues
  * As a position survey, it does not contribute new experiments; many cited results lack reported confidence intervals or rely on fragile evaluators (LSTM classifiers at κ≈0.6, LLM-as-judge with κ≈0.3), which weakens claim support.
  * Strategy-classification pipelines and ToM metrics across languages often depend on English-centric tooling; the survey notes this but still aggregates results without a meta-analytic uncertainty model.
* Clarity or presentation issues
  * Dense with acronyms and novel terms; some sections (e.g., mechanisms and calibration) move quickly between heterogeneous evidence without a unifying quantitative synthesis.
  * Tables occasionally aggregate across models/languages without transparent weighting or dispersion, which can obscure heterogeneity.
* Missing related work or comparisons
  * Omits or under-emphasizes recent cross-lingual steering and latent-space interventions that bear directly on the Semantic Hub vs. language-specific subspace debate (e.g., CLAS and CLaS-Bench).
  * Could connect more explicitly to large-scale agent benchmarks in deception/cooperation (e.g., Mafia/Werewolf-style multi-agent frameworks) and recent Hanabi-scale LLM studies to contextualize ToM/collaboration claims.

### Detailed Comments

* Technical soundness evaluation
  * The central thesis—language modulates strategic behavior via internal representational pathways—is plausible and timely. The two-pronged mechanistic story (Semantic Hub vs. Translation Barrier) is appealing because it yields diagnostic predictions (intermediate-layer decoding success vs. failure; late-layer projection errors; steerability asymmetries).
  * However, much of the mechanistic support relies on preliminary or non-replicated findings (e.g., stronger scaling needed to steer non-English activations; specific layer ranges for stable calibration). To increase rigor, the paper should articulate precise, pre-registered falsification criteria (e.g., if mid-layer probes exceed 90% intent accuracy while final outputs fail across ≥2 architectures, classify as Translation Barrier) and report any contradictory cases that violate the dichotomy.
  * The BBM formalization and the move away from CoT toward counterfactual utterance sets and structured templates are technically thoughtful and align with concerns about explanation faithfulness. Clear guidance on entailment model selection, ε-thresholds, and inter-annotator protocols across languages would further strengthen practical adoption.
* Experimental evaluation assessment
  * The survey makes a commendable effort to collect and synthesize cross-lingual findings (e.g., IPD distributions, clembench, Spyfall, Hanabi/XToM), and it highlights a critical negative result (no language effect on human persuasion outcomes) that tempers stronger claims.
  * Nonetheless, many sourced studies lack uncertainty quantification or rely on imperfect evaluators; the review would benefit from a structured meta-analytic summary (e.g., hierarchical Bayesian pooling) that models between-study variance, evaluator noise, and model/language/task random effects. Even a partial attempt (forest plots with CIs when available) would make effect magnitudes and heterogeneity more transparent.
  * The code-switching red-teaming synthesis is useful but could more clearly discuss sensitivity to mixing rate, script boundaries, and tokenizer families. Including basic ablation summaries (e.g., ASR vs. LRL-token fraction curves, thresholds where defenses start to fail) would guide sandbox adversary design.
* Comparison with related work (using the summaries provided)
  * Multicultural Spyfall: The survey’s claims about degraded non-English deceptive reasoning and rule-follow robustness are supported by Koto et al.’s multilingual, culturally localized Spyfall, which shows performance degradation on localized entities and format-induced forfeits. Citing their JSON-format enforcement and leakage metrics would provide convergent operational definitions for “format vs. strategy” errors.
  * SPIN-Bench: The reported decoupling between planning and social intelligence aligns with SPIN-Bench findings (planning success not translating to negotiation dominance). A tighter linkage could clarify whether language effects disproportionately impact social vs. planning dimensions.
  * Cross-lingual activation/steering (CLAS) and CLaS-Bench: These works demonstrate measurable, controllable language subspaces and bridge-layer interventions. Incorporating them would nuance the Semantic Hub story with evidence that cross-lingual transfer can improve via selective neuron rescaling or residual directions, and that language specificity concentrates in later layers—consistent with the paper’s Translation Barrier narrative.
  * Werewolf Arena and Mafia deception: Recent human/LLM deception comparisons (Mafia) and multi-agent Werewolf arenas provide complementary evidence on deception difficulty and role-conditional strategies. Explicit connections would enrich the survey’s BBM segment and the discussion of judge reliability in high-verbosity, free-form dialogue.
  * Large-scale Hanabi evaluation: Findings on scaffolding sensitivity and multi-turn state tracking deficits resonate with the survey’s Theory-of-Mind and intent–action divergence themes. Explicitly contrasting Sherlock/Mycroft scaffolds with the proposed intermediate-layer diagnostics could sharpen recommendations for cooperative games.
* Discussion of broader impact and significance
  * The work is impactful: it identifies multilingual alignment gaps that matter for real deployments, especially where multi-agent negotiation, safety guardrails, or cross-cultural operation is required.
  * The ethics statement appropriately warns against cultural essentialism and re-frames divergences as model–language interactions under specific training distributions. Recommending standardized reporting templates (e.g., explicitly listing confounds considered, language coverage in RLHF, tokenizer facts) could serve the community.
  * The proposed sandbox is valuable and actionable. Ensuring bilingual human adjudication baselines to validate self-translation judging, disclosing annotation pay/fairness practices, and providing openly licensed scripts/prompts would further increase community uptake.
* Additional suggestions
  * Clarify metric definitions and recommended thresholds for: commitment reliability, consistency labels, and calibration metrics (ECE/InfoECE) across languages; include per-language κ for adjudication.
  * Provide example rubrics/checklists for ensemble judging and a small pilot showing κ gains from (i) self-translation, (ii) checklist rubrics, and (iii) multi-family judge panels.
  * Where possible, quantify effect sizes in the main text (not just appendices) and attach confidence intervals or variance estimates; explicitly flag where results are single-study findings pending replication.

### Questions for Authors

1. Can you specify concrete, pre-registered falsification criteria distinguishing Semantic Hub vs. Translation Barrier failures, and report any known counterexamples where intermediate-layer probes succeed but final outputs still align with English reasoning rather than the target language?
2. How sensitive are the code-switching ASR gains to the proportion and placement of LRL tokens, script boundaries (Latin vs. non-Latin), and tokenizer families (BPE vs. SentencePiece vs. char-level)?
3. For the proposed ensemble judging protocol, can you provide a small pilot (even synthetic) quantifying κ improvements from each component (self-translation, multi-family judges, checklist rubrics, abstentions)?
4. In the intent–action divergence proposal, how will you ensure cross-lingual comparability of commitment phrasing and annotator interpretations? Are there canonical templates or normalization schemes you recommend per language?
5. Several cited findings lack confidence intervals or rely on weak evaluators; do you plan to include a hierarchical meta-analysis in the final version, and if so, what priors and heterogeneity structure will you adopt?
6. How do your hypotheses interface with cross-lingual steering results (e.g., CLAS or CLaS-Bench)? Do these interventions reduce Translation Barrier failures by shifting realizations in late layers, and can they be integrated into the sandbox as controlled defenses?
7. The persuasion null result is compelling; do you hypothesize specific classes of interactive tasks (e.g., deception-heavy vs. coalition-formation) where language effects should vanish vs. persist, and how will the sandbox test these boundary conditions?

### Overall Assessment

This is a timely and thought-provoking position survey that consolidates emerging, disparate threads on multilingual LLM behavior in interactive games and links them to plausible mechanistic accounts and concrete evaluation infrastructure. Its strongest contributions are conceptual integration, careful attention to contradictory evidence and confounds, and a highly actionable benchmark proposal that directly addresses evaluator fragility. The main limitations stem from its reliance on preliminary or non-replicated mechanistic evidence, aggregation over studies with heterogeneous (and sometimes weak) evaluators, and some missing connections to recent cross-lingual steering literature. For an EMNLP survey/position track, I view this as a valuable contribution with high potential to shape a research agenda. I recommend acceptance contingent on tempering causal claims, expanding related-work coverage (CLAS, CLaS-Bench, recent multi-agent deception/cooperation studies), and adding clearer falsification criteria plus a small quantitative pilot for the proposed ensemble judging protocol.
