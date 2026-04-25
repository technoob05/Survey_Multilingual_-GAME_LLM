# Gemini Deep Research Prompts for EMNLP 2026 Revision

Use the following prompts in Gemini Advanced (with Deep Research enabled) to gather the empirical data and literature needed to strengthen the claims in the paper:

## Prompt 1: "Nicer than Human" & Cooperative Biases in Multilingual LLMs
> "Conduct a deep literature review on the 'Nicer than Human' bias in Large Language Models, specifically focusing on how this cooperative bias or sycophancy manifests in multi-agent game theory settings (like the Iterated Prisoner's Dilemma, Public Goods games, or Ultimatum games). Crucially, find research that evaluates whether this 'Nicer than Human' bias varies across different languages (e.g., does it hold in English but break down in Arabic, Vietnamese, or Chinese?). Look for recent papers (2023-2026) that quantify this bias and its cross-lingual degradation."

## Prompt 2: FAIRGAME Framework & Matrix Game Evaluations
> "Search for recent literature (2024-2026) involving the 'FAIRGAME' framework (or similar multilingual matrix game frameworks for LLMs) authored by researchers like Huynh or Buscemi. I need detailed empirical findings on how language framing, personality priming, and payoff multipliers ($k$ values) affect LLM strategy distributions in games like the Iterated Prisoner's Dilemma. Specifically, find papers that report exact confidence intervals, calibration curves for strategy classifiers (like LSTMs detecting Tit-for-Tat), and any human-validated error analyses of these classifiers."

## Prompt 3: Cross-Lingual Calibration & Expected Calibration Error (ECE)
> "Find recent research evaluating the Expected Calibration Error (ECE) and metacognitive confidence of Large Language Models in non-English evaluation settings, particularly in complex strategic or reasoning tasks. I am looking for quantitative data showing how ECE degrades (e.g., from ~5% in English to >20% in low-resource languages). How does this cross-lingual overconfidence correlate with hallucinations or failure to adhere to constraints in interactive settings?"

## Prompt 4: Diagnostic Protocols: Semantic Hub vs. Translation Barrier
> "Search for research in Mechanistic Interpretability (2024-2026) that provides explicit diagnostic protocols for distinguishing between the 'Semantic Hub' hypothesis (where non-English reasoning is lossily compressed to English in intermediate layers) and the 'Translation Barrier' hypothesis (where internal reasoning is correct but fails during final target language decoding). Look for methodologies involving layer-wise probing, Activation Addition (ActAdd), Sparse Representation Steering (SRS), and cross-lingual logit lens techniques. What pre-registered decision rules are proposed to confirm one hypothesis over the other?"

## Prompt 5: Multilingual Evaluation: XTREME vs. Interactive Agentic Benchmarks
> "Compare static multilingual benchmarks like XTREME and XTREME-R with emerging interactive, multi-agent frameworks (like clembench, SPIN-Bench, or MultiAgentBench). Find literature that explicitly critiques the limitations of static NLI/QA cross-lingual benchmarks when attempting to capture dynamic strategic misalignment, formatting compliance failures, and intent-action divergence in conversational or game-theoretic environments."
