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
This perspective advances the thesis that multilingual LLM agents exhibit language-dependent shifts in cooperative behavior, deception, and theory-of-mind (ToM), framing this “Algorithmic Sapir–Whorf Switch” through three lenses: (i) empirical behavioral signatures in interactive multi-agent environments (e.g., social dilemmas), (ii) architectural mechanisms via the Semantic Hub and Translation Barrier hypotheses, and (iii) evolutionary and cultural-evolutionary perspectives that reinterpret LLM cooperation as culturally inherited rather than evolved through interaction. The article synthesizes recent evidence, highlights counterexamples and confounds, and proposes four falsifiable predictions to convert the synthesis into a research agenda with alignment and societal relevance.

Strengths
Technical novelty and innovation
The explicit framing of language as a modulator of LLM agent behavior (“Algorithmic Sapir–Whorf Switch”) is conceptually original and timely for machine behaviour.
Unifying mechanistic interpretability accounts (Semantic Hub, Translation Barrier) with behavioral outcomes moves beyond cultural-essentialist explanations toward architectural ones.
Reframing the “nicer than human” cooperation as culturally inherited via pretraining/RLHF is a novel contribution that bridges evolutionary game theory and LLM alignment.
The four pre-registered-style, falsifiable predictions (P1–P4) are concrete and provide a clear next-step empirical agenda.
Experimental rigor and validation
Although a perspective piece, it assembles diverse empirical sources (social dilemmas, negotiation, social deduction, calibration, multilingual ToM) and explicitly acknowledges contradictory results, framing effect dominance, and methodological confounds.
The article avoids overclaiming by bounding language effects and identifying key confounds (tokenization, skewed RLHF, decoding hyperparameters).
Clarity of presentation
The narrative is well-structured, progressing from behavioral characterization to mechanisms, to ToM, and finally to evolutionary and societal implications.
Careful definitional work (e.g., distinguishing hub vs. realization failures, mapping machine cooperation to cultural inheritance) improves conceptual clarity.
The authors are explicit about limitations and provide precise predictions, which enhances interpretability and usefulness for the community.
Significance of contributions
The work squarely fits the machine behaviour theme, with direct implications for multilingual deployment, safety, calibration, and inequality across languages.
It provides a much-needed synthesis that connects agent-level behavior to pipeline-level causes and population-level evolutionary dynamics, likely to shape future empirical studies and evaluation standards.
Weaknesses
Technical limitations or concerns
Table 1 aggregates strategy distributions across models and languages using a classifier threshold, but methodological heterogeneity (prompts, horizons, opponents, payoff structures) across contributing studies can confound cross-language inferences.
The Semantic Hub and Translation Barrier hypotheses, while plausible, are primarily supported by suggestive interpretability results; stronger causal evidence linking specific intermediate-layer representations to behavioral differences is not yet established.
Reported calibration gaps (e.g., ECE rising fivefold) and cross-lingual ToM degradations would benefit from more explicit methodological details (models, datasets, binning schemes, parallel prompts) to contextualize magnitudes.
Experimental gaps or methodological issues
No new experiments are conducted to instantiate the predictions; some claims rely on unpublished or workshop/preprint results that may have variable methodological rigor.
Potential confounds (e.g., tokenization entropy, frequency of code-switch artifacts, decoding hyperparameters) are acknowledged but not systematically controlled in the evidentiary synthesis.
The corpus–cooperation correspondence prediction (P1) hinges on yet-to-be-specified “cooperative-discourse density” metrics; operationalization is non-trivial and under-specified.
Clarity or presentation issues
A few references appear incomplete or inconsistently formatted (e.g., bracketed placeholders for authors, missing years in-text), and some claims would benefit from tighter citation mapping.
The bridge from multilingual ToM erosion to downstream safety and commitment reliability is suggestive but could better parse correlation versus causation.
Missing related work or comparisons
Broader multilingual representation literature (e.g., mT5, XLM-R, language-specific modules vs. shared subspaces) could be more thoroughly integrated to contextualize the “English-dominant hub” claim.
Prior AI-specific examinations of Sapir–Whorf-like effects and “latent language”/translationese phenomena deserve fuller treatment in the mechanism discussion.
Fairness and global deployment literatures (e.g., on linguistic equity, resource disparity) could be engaged more deeply to bolster policy implications.
Detailed Comments
Technical soundness evaluation
The theoretical framing is coherent and well-motivated. However, causal claims about language shaping behavior via representational bottlenecks need stronger empirical triangulation (e.g., interventional probes, causal tracing across layers, controlled tokenization manipulations).
The two-mechanism account (hub vs. realization) is appealingly parsimonious but may oversimplify multilingual processing in large, diverse architectures; alternative explanations (e.g., language-specific microcircuits, subspace interference) should be discussed.
The “culturally inherited cooperation” argument is persuasive but would benefit from controls disentangling pretraining corpus effects from alignment/RLHF policy priors and decoding-time priors.
Experimental evaluation assessment
Aggregating strategy distributions (Table 1) across heterogeneous studies introduces comparability risks. Reporting confidence intervals, per-study normalization, or a meta-analytic approach would make the synthesis more statistically sound.
The calibration and ToM sections are well-curated but should document model families, data regimes, and task formats more explicitly to help readers assess external validity and replicate analyses.
The proposed predictions are appropriate and measurable; adding concrete analysis plans (e.g., corpus audit annotation schemes, probe training/validation splits, pre-registration templates) would strengthen their actionability.
Comparison with related work (using the summaries provided)
The synthesis aligns with emerging evidence that LLM cooperation varies by model and environment (RW 2406.13605) and that minimal cheap talk can boost coordination while curricula can induce negative transfer (RW 2510.05748); incorporating these as moderating factors would nuance the “nicer than human” claim.
Personality steering effects on cooperation (RW 2503.12722) provide a useful parallel: if activation additions reliably modulate cooperative tendencies, this supports the general thesis that internal representations (including language-linked ones) steer social behavior. Drawing this parallel explicitly would be valuable.
Findings that infrastructure factors (e.g., communication delay) shape cooperation (RW 2602.11754) complement the paper’s framing that non-linguistic contextual factors can dominate language effects, reinforcing the need for multi-factor experimental designs.
Human responses to perceived agent identity (RW 2503.07320) indicate that partner framing modulates cooperation; interfacing this with language effects (e.g., language as a moderator of perceived identity/trustworthiness) could further integrate human–AI co-behavioral dynamics.
The push for non-English-first LLMs (RW 2404.04167) and language-specific models (RW 2503.10995) should be discussed as natural tests or mitigations of the Semantic Hub bottleneck (e.g., does prioritizing a target language invert the hub asymmetry?).
Discussion of broader impact and significance
The societal implications are well argued: calibration gaps, uneven attack surfaces via code-switching, and normative drift through WEIRD-biased corpora are concrete and consequential for public-sector deployments.
The cultural-evolution frame is a strength, highlighting machine-to-machine inheritance (distillation/synthetic data) as a new axis of drift; however, clearer governance levers (benchmark diversification, multilingual RLHF, audit standards) would strengthen the prescriptive value.
The emphasis on falsifiability is commendable; successful or failed tests would both refine the field’s understanding and inform safe multilingual deployment practices.
Questions for Authors
How were the studies aggregated to produce Table 1’s strategy distributions, and what normalization or compatibility checks were applied across different games, horizons, prompts, and classifiers?
Can you specify the exact models, languages, datasets, and binning choices that underlie the reported calibration gaps (e.g., 4.6% to 23.1% ECE), and whether these results hold under alternative calibration metrics and parallel prompting?
For the Semantic Hub hypothesis, beyond activation steering transfer across languages, do you have causal tracing or ablation evidence that English-anchored subspaces are necessary for non-English reasoning? How would you distinguish hub centrality from general representation sharing?
For P1, how do you propose to operationalize “cooperative-discourse density” in multilingual corpora (annotation scheme, automated proxies, domain control), and how will you control for RLHF and decoding hyperparameters that may mediate behavior?
For P2, why are [L/3] and [2L/3] the probe depths of choice? Would you consider language-specific layer localization (e.g., per-language probe maxima) to avoid missing peak representational loci?
To what extent might tokenization entropy and subword fragmentation alone explain the language-dependent behavior? Would a shared, language-agnostic tokenizer (or byte-level decoding) reduce the observed divergences?
The paper argues that multilingual ToM erosion co-occurs with degraded cooperation and deception. Do you have evidence that ToM is the mediating variable rather than a correlated symptom (e.g., via mediation analysis or targeted ToM priming/impairment interventions)?
How might language-prioritized models (e.g., CT-LLM for Chinese or TigerLLM for Bangla) perform under your framework? Do their behaviors counter the Semantic Hub asymmetry, and have you identified case studies where prioritizing a non-English hub improves both calibration and cooperation?
Given evidence that framing and cheap talk can dominate behavior, how would you design experiments to isolate pure language effects from these strong contextual confounds?
Can you articulate governance recommendations (benchmarks, RLHF diversification, evaluation standards) that concretely follow from your predictions, to help practitioners mitigate language-induced behavioral gaps now?
Overall Assessment
This is a thoughtful and timely perspective that fits squarely within the machine behaviour programme and the theme issue’s remit. Its main contributions are conceptual synthesis and agenda-setting: it proposes a mechanistic, non-essentialist account of language-modulated behavior in LLM agents; reframes cooperation as culturally inherited; and advances four falsifiable predictions that could calibrate future empirical work. While some evidence cited is preliminary and aggregated across heterogeneous methodologies, the authors are transparent about limitations and confounds. The paper would benefit from tighter citation hygiene, clearer methodological context for key quantitative claims, and more precise operationalization of proposed tests. With moderate revisions along these lines, this perspective should be valuable to the community, stimulating rigorous multilingual, mechanistic, and evolutionary studies of LLM behavior. I recommend acceptance pending revisions focused on methodological specificity and expanded related-work context.