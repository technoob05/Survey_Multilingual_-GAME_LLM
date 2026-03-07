# Gemini Deep Research Prompt: Verify & Strengthen Reviewer-Requested Citations

## Context
I am revising a position survey paper titled **"Under the Shadow of Babel: A Position Survey on Linguistic Relativity and Strategic Deception in Multilingual LLM Games"** for EMNLP 2026. Reviewers have requested integration of several specific works and research directions. I need you to find and verify the exact papers, extract key findings, and provide proper BibTeX entries.

## Research Tasks (Priority Ordered)

### Task 1: Translation Barrier Hypothesis
Find the paper with arXiv ID **2506.22724** or closely related work on the "Translation Barrier Hypothesis" — the idea that multilingual LLM failures arise from late-layer language realization (internal translation) rather than upstream reasoning deficits. Key questions:
- What is the exact title, authors, and venue?
- What is the core empirical finding distinguishing upstream reasoning from late-layer translation?
- How does this complement vs. contradict the Semantic Hub Hypothesis (Wu et al., 2024)?
- Also find the paper by Wendler et al. (arXiv:2402.10588) "Do Llamas Work in English? On the Latent Language of Multilingual Transformers" — verify title, authors, key findings about internal language of computation.

### Task 2: Indic-TunedLens
Find the paper on **Indic-TunedLens** — a language-aware interpretability probing tool for Indic scripts in Transformers. Key questions:
- Exact title, authors, arXiv ID, year?
- What methodology does it use for layer-wise language-aware probing?
- Can it empirically distinguish "Semantic Hub" predictions from "Translation Barrier" predictions?

### Task 3: Red-Teaming Frameworks
Find the following four red-teaming/adversarial LLM evaluation papers and provide BibTeX entries and 2-3 sentence summaries of their relevance to multilingual multi-agent attacks:

1. **AutoRed** — automated red-teaming with reinforcement learning, persona-guided attacks at scale
2. **OpenRT** — open-source multi-turn red-teaming benchmark for LLMs
3. **Genesis** — evolving attack strategies against web agents (possibly multilingual)
4. **M2S** — multi-turn, multi-strategy jailbreak attacks on LLMs

For each: exact title, authors, arXiv ID, year, and whether they have any multilingual component or multi-agent dimension.

### Task 4: Anecdoctoring Pipeline
Find the paper on **"anecdoctoring"** — an LLM-driven pipeline for producing culturally grounded, localized disinformation at scale. Key questions:
- Exact citation (title, authors, arXiv ID)?
- Does it cover multilingual generation or cultural localization?
- How does it relate to persuasion and strategic deception in games?

### Task 5: ActAdd Cross-Lingual Steering Details
In the **Semantic Hub Hypothesis** paper (Wu et al., 2024, "The Semantic Hub Hypothesis: Language Models Share Semantic Representations Across Languages and Modalities"):
- What specific layers were used for Activation Addition (ActAdd)?
- How were steering vectors constructed (mean-difference, PCA, etc.)?
- Was the scaling coefficient α=5 for non-English vs α=2 for English reported explicitly, or was it more nuanced?
- Were confidence intervals or variance across prompts reported?
- What models were tested?

### Task 6: Meta-Analysis Effect Sizes
Search for any existing meta-analyses or systematic quantitative reviews of:
- Cross-lingual LLM behavioral divergence in game-theoretic or interactive settings
- Effect sizes for language as a variable in LLM strategy choice
- Statistical methodology for comparing strategy distributions across languages (bootstrap CIs, permutation tests, etc.)

## Output Format
For each task, provide:
1. **Verified citation** (exact title, authors, arXiv ID or DOI, year)
2. **BibTeX entry** (properly formatted)
3. **Key findings** (2-4 sentences summarizing what's relevant to our survey)
4. **Integration suggestion** (1-2 sentences on where/how to cite in the paper)
5. **Confidence level** (High/Medium/Low) on whether this is the correct paper the reviewer intended

If a paper cannot be found or doesn't exist, say so explicitly and suggest the closest alternative.
