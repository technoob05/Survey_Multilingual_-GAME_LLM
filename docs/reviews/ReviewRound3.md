
## Under the Shadow of Babel: A Position Survey on Linguistic Relativity and Strategic Deception in Multilingual LLM Games

EMNLPSubmitted: March 5, 2026

### Contents

* [Summary](https://paperreview.ai/review#summarySection)
* [Strengths](https://paperreview.ai/review#strengthsSection)
* [Weaknesses](https://paperreview.ai/review#weaknessesSection)
* [Detailed Comments](https://paperreview.ai/review#detailedSection)
* [Questions](https://paperreview.ai/review#questionsSection)
* [Overall Assessment](https://paperreview.ai/review#assessmentSection)

### Summary

This position survey argues that language is an active moderator of LLM agents’ strategic behavior in interactive, multi-agent games. Synthesizing evidence across seven game categories and languages, it advances the “Algorithmic Sapir–Whorf Switch” view, situates mixed and contradictory findings via the Semantic Hub Hypothesis, and highlights practical risks such as code-switching red-teaming and multilingual judge unreliability. The paper culminates in a concrete proposal for a Cross-Cultural Agentic Sandbox Benchmark with controls for tokenization, RLHF coverage, decoding, code-switching adversaries, collusion detection, intent–action metrics, and ensemble judging.

### Strengths

* Technical novelty and innovation
  * Positions language as a primary experimental variable for interactive, multi-agent evaluation, rather than a mere surface form.
  * Connects behavioral divergences to a mechanistic account (Semantic Hub Hypothesis), offering a unifying explanation for asymmetric multilingual failures in ToM, deception, and format adherence.
  * Proposes a comprehensive benchmark design that operationalizes confound control (tokenization, decoding), intent–action consistency metrics, adversarial code-switching agents, and ensemble judging.
* Experimental rigor and validation
  * Actively incorporates contradictory/null evidence (e.g., persuasion null effect; volatile Arabic strategy priors; Vietnamese subverting collectivist expectations), tempering overgeneralization.
  * Disentangles potential confounds (tokenization, RLHF coverage, payoff comprehension, decoding hyperparameters), and calls for pre-registration and per-language calibration/annotation reliability.
* Clarity of presentation
  * Clear taxonomy of game settings, with consistent framing of what each category probes (ToM, deception, coalition-building, cooperative communication, etc.).
  * Tables concisely summarize cross-linguistic distributions, judge reliability results, and red-teaming attack rates, while the text openly acknowledges limitations.
* Significance of contributions
  * Elevates a critical and underexplored safety/evaluation gap: English-only assessments can misestimate behavior in agentic, multilingual deployments.
  * Highlights practical threats (code-switching red-teaming, steganographic collusion) and the evaluative fragility of multilingual LLM-as-judge, providing actionable guidance for benchmark design and defenses.

### Weaknesses

* Technical limitations or concerns
  * Some mechanistic claims (e.g., specific ActAdd scaling coefficients needed to steer non-English outputs) are asserted without sufficient methodological detail or independent replication across models/layers.
  * The “Algorithmic Sapir–Whorf Switch” risks overreach; causality is not established and confounds remain substantial even as the paper acknowledges them.
* Experimental gaps or methodological issues
  * As a survey/position, the work does not deliver new empirical experiments, meta-analyses, or re-analyses that would more rigorously adjudicate among competing explanations.
  * Several cited results rely on LLM-as-judge scoring, which the paper itself shows to be unreliable across languages (κ ≈ 0.3), raising questions about the evidential weight of parts of the synthesis.
  * Strategy classification in social dilemmas (LSTM with 0.6 threshold) lacks reported calibration/CI in the underlying literature; the survey flags this but still leans on such aggregates.
* Clarity or presentation issues
  * Some terminological constructs (e.g., Bayesian Belief Manipulation) are introduced without a formal operational definition; this could encourage conceptual drift.
  * Minor inconsistencies/typos in tables and references (e.g., “GPT-40”), and occasional overloading of claims in dense paragraphs.
* Missing related work or comparisons
  * Red-teaming ecosystems (beyond CSRT) and agentic adversaries are under-cited relative to their relevance; recent frameworks like AutoRed, OpenRT, Genesis, and M2S offer complementary insights into multi-turn, multilingual, or structure-based jailbreaks and could contextualize the code-switching threat more fully.
  * Mechanistic alternatives and complements to the Semantic Hub, such as the Translation Barrier Hypothesis and language-aware lenses (Indic-TunedLens), could be more explicitly integrated to separate “task-solving” from “late-layer translation” failures in multilingual generation.

### Detailed Comments

* Technical soundness evaluation
  * The central hypothesis—that language can modulate strategic intent, ToM, and deception via representational differences—is plausible and consistent with reported divergences, but causality remains unproven. The Semantic Hub Hypothesis provides a coherent mechanistic narrative and is well-aligned with prior findings showing English-anchored intermediate representations and cross-lingual steering via activation editing. However, specific claims like the required ActAdd scaling “5 vs 2” for non-English steering need fuller methodological detail (layer selection, steering vector construction, variance across prompts/models) to avoid over-specification from isolated cases.
  * The paper rightly emphasizes confounds (tokenization, RLHF asymmetry, data distribution, decoding); the proposed benchmark controls address these well. Integrating the Translation Barrier Hypothesis could sharpen the mechanism: many multilingual failures may be late-layer “internal translation” failures rather than upstream task-solving deficits, especially in cooperative/format-adherence tasks where final realization matters. Language-aware interpretability tools (e.g., Indic-TunedLens) could help ground layer-wise evidence.
* Experimental evaluation assessment
  * As a survey/position piece, it does not contribute new experiments; instead, it synthesizes. That synthesis is careful in surfacing contradictions (Arabic bimodality, Vietnamese behavior, null persuasion effect) and in pointing out judge unreliability. Still, the field would benefit from even a small re-analysis/meta-analysis (e.g., standardizing strategy distributions with CIs across studies; quantifying effect sizes for code-switching attacks by model family and language resource level; re-scoring a subset with human judges to calibrate κ).
  * The benchmark proposal is a strong practical contribution. The decomposition into formatting vs strategic components (clembench principle), pre-registration, per-language annotation reliability, and embedded adversaries (code-switching and collusion) are all sound. Explicit guidance on sample sizes, languages/dialects, and costed evaluation protocols would increase feasibility.
* Comparison with related work (using the summaries provided)
  * CSRT is appropriately highlighted; integrating broader red-teaming frameworks would strengthen coverage. AutoRed and OpenRT show how persona-guided/multi-agent strategies can induce failures at scale; Genesis demonstrates evolving attack strategies against web agents, with hints of multilingual payloads. These works support the paper’s thesis that interactive/multi-agent settings expose new failure modes and that adversaries can exploit multilingual/presentation mismatches.
  * The Semantic Hub Hypothesis (2411.04986) is well-aligned with the paper’s mechanistic account; citing translation-barrier evidence (2506.22724) would help separate representational hub effects from late-stage realization failures. Language-aware lenses (Indic-TunedLens) offer tooling to test hub vs translation-barrier predictions in low-resource scripts.
  * The anecdoctoring pipeline for localized disinformation further illustrates how culturally/linguistically grounded attacks can scale and might intersect with the paper’s persuasion section (even given the reported null effect in one controlled setting).
* Discussion of broader impact and significance
  * The work addresses an important and timely question: whether English-centric evaluation overestimates agent alignment and safety in multilingual, interactive deployments. Exposing judge unreliability, code-switching vulnerabilities, and intent–action divergences has clear implications for safety evaluation, red-teaming, and policy. The proposed benchmark could become a community asset if realized with open artifacts and strong governance.
  * Communication risks are handled responsibly; the paper warns against cultural essentialism and frames divergences as model–language interaction effects. This is good practice and should be kept central in any benchmark narrative and public artifacts.

### Questions for Authors

1. Can you provide methodological specifics for the claimed activation-addition scaling differences across languages (layers targeted, steering vector construction, effect variability across prompts/models), and whether these results replicate beyond a single model family?
2. How will the proposed benchmark operationalize and report per-language inter-annotator agreement for intent–action consistency, and what sample sizes do you consider sufficient to achieve stable κ/α estimates per language/dialect?
3. Given κ ≈ 0.3 for multilingual LLM judges, what concrete ensemble judging protocol (number/types of judges, self-translation to English, checklist rubrics) do you recommend as a default, and what empirical evidence supports its reliability gains?
4. How will you incorporate the Translation Barrier Hypothesis into benchmark design to diagnose whether failures are due to upstream reasoning vs late-layer language realization (e.g., intermediate decoding checks, dual-pass translation pipelines)?
5. For code-switching red-teaming, how will you ensure linguistic ecological validity (e.g., realistic two-language switches, tag-switching patterns) rather than artificial multi-language mixes that might overstate risk?
6. Will you release a pilot dataset and evaluation scripts for the Cross-Cultural Agentic Sandbox to enable community validation, and what languages/dialects will be prioritized initially?

### Overall Assessment

This is a timely, well-argued position survey that foregrounds an underappreciated axis in agentic LLM evaluation: language as a moderator of strategic behavior, safety, and evaluation reliability. Its strengths are the breadth of coverage across interactive game types, the willingness to include contradictory/null results, the mechanistic bridge via the Semantic Hub, and a practical, thoughtfully specified benchmark proposal that addresses confounds, adversaries, and judge unreliability. Its main limitations are inherent to its genre: limited new empirical evidence, some over-specific mechanistic claims that need more methodological grounding, and reliance on studies that themselves may be judge-limited or lack calibration. The paper would be stronger with explicit integration of complementary red-teaming frameworks and mechanistic alternatives (translation barrier), plus at least a small-scale re-analysis or pilot release demonstrating the proposed evaluation principles. Overall, I view this as a valuable and constructive contribution that would benefit the EMNLP community, especially if the authors can tighten mechanistic claims and expand related work connections. I recommend acceptance in Findings or a borderline accept for the main track contingent on addressing the questions and clarifying methodological details.
