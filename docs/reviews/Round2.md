Babel's Machines: Linguistic Relativity, Cooperation, and the Emerging Behaviour of Multilingual Artificial Agents
Interface Focus (Royal Society) — Theme issue: Machine behaviour in the age of large language models: social, cognitive and evolutionary perspectives
Submitted: April 27, 2026
Contents
Summary
Strengths
Weaknesses
Detailed Comments
Questions
Overall Assessment
Summary
This perspective synthesizes emerging evidence that large language model (LLM) agents exhibit language-dependent shifts in cooperative behavior, strategic dispositions, and theory-of-mind (ToM) performance—an effect the authors call the Algorithmic Sapir-Whorf Switch. It advances mechanistic explanations (Semantic Hub and Translation Barrier hypotheses), frames LLM cooperation as culturally inherited via pretraining/RLHF rather than evolved through interaction, and proposes four falsifiable predictions and governance levers to ground a multilingual science of machine behavior.

Strengths
Technical novelty and innovation
The paper articulates an integrative framework that connects multilingual LLM behavior to mechanistic interpretability (hub/barrier), cultural evolution, and evolutionary game theory—moving beyond benchmark-by-benchmark reporting.
The “culturally inherited cooperation” thesis reframes well-known cooperation findings in a novel way that is specific and testable (e.g., corpus–cooperation correspondence, P1).
The proposed P1–P4 predictions are concrete, falsifiable, and operationalizable with current tooling, providing a clear research agenda.
Experimental rigor and validation
Although this is a perspective, the authors are careful to foreground contradictory evidence and confounds (e.g., framing effects overriding language, miscomprehension artifacts, persuasion null result), which constrains overgeneralization.
The mechanistic accounts are tied to testable probes and prior interventions (e.g., activation additions, intermediate-layer calibration probes), rather than left at a purely speculative level.
Clarity of presentation
The narrative is clear and well-structured: characterization → mechanisms → ToM → evolutionary framing → implications → predictions.
The authors explicitly separate descriptive observations from causal claims and note where evidence is heterogeneous or preliminary.
Significance of contributions
The topic is highly relevant for the Interface Focus theme (machine behavior, social and evolutionary perspectives), with direct implications for multilingual deployment, safety, and governance.
The linkage between multilingual representation asymmetries and cooperative/ToM outcomes is an important step toward a unified account of language-conditioned machine behavior.
Weaknesses
Technical limitations or concerns
Table 1 aggregates across heterogeneous studies, models, protocols, and run counts without uncertainty estimates; the authors acknowledge this but still rely on the table as an empirical anchor.
Strategy labeling via an LSTM classifier at 0.6 confidence may be brittle across languages; cross-lingual reliability and error analysis are not reported here.
The mechanistic linkage between hub/barrier phenomena and concrete behavioral outcomes (e.g., IPD strategies) remains inferential; direct causal manipulations that change multilingual behavior via targeted representation edits are not yet demonstrated.
Experimental gaps or methodological issues
No standardized, pre-registered multilingual IPD protocol is used for synthesis; cross-study variability (payoff matrices, horizon disclosure, opponents) clouds interpretation of cross-language effects.
Potential confounds (tokenization differences, decoding hyperparameters, RLHF coverage) are well-noted but not empirically disentangled in the presented evidence or the summary table.
The ToM section synthesizes emerging work but does not fully address the broader debate over ToM construct validity for LLMs or leakage/shortcut concerns in ToM benchmarks.
Clarity or presentation issues
Some high-level claims (e.g., “nicer than human”) could be more tightly bounded by specifying game structure, horizon known/unknown, and opponent policy distributions to avoid overgeneralization.
The term “Algorithmic Sapir-Whorf Switch” is catchy but risks over-claim without a consolidated, single-protocol dataset demonstrating robust effect sizes with proper controls.
Missing related work or comparisons
The paper could engage more explicitly with critiques of LLM ToM construct validity and dataset leakage, as well as with multilingual RLHF design and language-adaptive safety alignment literature.
Additional pointers to cross-lingual multi-agent safety and calibration repair methods (e.g., language adapters, instruction-tuning variations) would strengthen the mechanism-to-intervention bridge.
Detailed Comments
Technical soundness evaluation
The conceptual framework is coherent and aligns with existing interpretability findings that internal representations can be shared across languages and causally implicated via activation interventions. The Semantic Hub and Translation Barrier hypotheses map naturally onto known asymmetries in multilingual models and provide plausible, testable mechanisms for downstream behavior differences.
However, the causal chain from representational asymmetry → degraded ToM → altered cooperative strategies is hypothesized rather than empirically demonstrated in a single controlled pipeline. P2 is well-designed to separate hub versus realization failures but should be coupled with behavioral readouts (e.g., per-language changes in IPD strategy distribution after targeted representation interventions) to close the loop.
The cultural inheritance framing is compelling. Still, it requires careful separation of pretraining corpus effects from RLHF priors and decoding-time randomness. The proposed 2×2×2 ablation is appropriate; absent such a study, the thesis remains a strong but not exclusive explanatory account.
Experimental evaluation assessment
The synthesis is careful but still aggregates heterogeneous evidence. Table 1, while illustrative, lacks a principled meta-analytic treatment (normalization, confidence intervals, study-level moderators). Given the centrality of this table to the behavioral claims, a supplementary meta-analysis plan (even if preliminary) would add weight.
The contradictory evidence is well-chosen and helps bound claims. The acknowledgement that framing, stakes, and communication channels can swamp language effects is important and should be emphasized in any practitioner-facing guidance.
The ToM discussion is informative, connecting variation across languages to practical cooperative/deceptive performance. Still, it would benefit from direct mediation tests or targeted ToM-impairment interventions to determine whether ToM is the causal bottleneck for commitments and cooperative reliability, or merely a correlated failure due to shared representational sparsity.
Comparison with related work (using the summaries provided)
The mechanistic angle aligns with interpretability findings that internal representations are not merely correlational but can be causally implicated (e.g., 2312.16257 on geospatial representations; 2603.21546 showing world models’ internal state variables are linearly decodable and causally useful). These support the paper’s insistence on using probes and interventions to differentiate hub vs. realization failures.
The use of logit-lens and layer-resolved analyses (as in LogitLens4LLMs and 2506.07824’s arithmetic stages) provides precedent and tooling for P2. The causal-reasoning study (2410.21353) shows a two-stage syntactic/semantic processing pattern, suggesting the kind of depth-resolved dissociations the authors propose to exploit cross-linguistically.
The paper could explicitly connect these interpretability precedents to the multi-agent behavioral readouts it cares about (e.g., demonstrate that altering mid-layer representations along English-derived steering vectors measurably shifts IPD strategies in non-English prompts).
Discussion of broader impact and significance
The societal implications section is strong and concrete, particularly on calibration asymmetries, code-switching attack surfaces, and the need to couple multilingual safety benchmarks with interactive behavioral ones. The proposed governance levers (benchmark diversification, RLHF coverage standards, multi-agent audit practices) are practical and responsive to the identified risks.
The WEIRD-norms argument is salient; it moves discourse beyond performance gaps to normative externalities, which are often neglected in technical venues but matter greatly for deployment in multilingual public institutions.
Questions for Authors
Can you provide more detail about the strategy-classifier reliability across languages in Table 1 (per-language precision/recall, confusion matrices, and human validation rates)? How sensitive are the aggregated proportions to the 0.6 confidence threshold?
How much of the observed cross-lingual behavioral variance remains when tokenization, decoding parameters (temperature/top-p), and prompt verbosity are controlled and matched across languages within a single study?
Have you attempted direct, causal representation interventions (e.g., activation additions derived from English cooperative vs. defecting traces) to see if they predictably shift non-English IPD strategies, thereby linking the Semantic Hub account directly to behavior?
In the ToM section, can you outline an analysis plan to test whether ToM mediates commitment reliability and cooperative success across languages (e.g., structural equation modeling or targeted ToM “knockdown” via representation steering)?
For P1 (corpus–cooperation correspondence), how will you address the substantial opacity and dynamism of pretraining corpora for frontier models (e.g., through proxy corpora, model families with known data, or controlled pretraining runs)?
Could you clarify the governance recommendation on RLHF coverage standards: what minimum per-language annotator proportions or quality controls (e.g., dialectal diversity, guideline localization) do you envision as practically achievable?
How do you see code-switching interacting with the hub/barrier hypotheses—does intra-utterance mixing reduce realization errors by “pivoting” through higher-resource tokens, or does it primarily expand the attack surface?
Overall Assessment
This is a well-argued, timely perspective that synthesizes diverse strands—behavioral characterization, multilingual representation asymmetries, ToM variation, and cultural evolution—into a coherent agenda for a multilingual science of machine behavior. The authors are careful to bound their claims, offer concrete and falsifiable predictions, and translate insights into actionable governance levers. The primary limitations stem from reliance on heterogeneous evidence (with a non-meta-analytic Table 1), inferential rather than causal links between mechanisms and behaviors, and incomplete engagement with the ToM construct-validity debate. These are, however, addressable within a revision: clarifying the empirical status of tabled results (with uncertainty and reliability), tightening claims and terminology, adding references to key ToM critiques, and, where possible, sketching concrete experimental designs that establish causal links (e.g., representation interventions that change multilingual IPD outcomes). Given its conceptual novelty, relevance, and constructive roadmap (P1–P4), I find the paper valuable for Interface Focus’s theme issue and recommend acceptance pending moderate revisions that strengthen evidential grounding and broaden related work coverage.