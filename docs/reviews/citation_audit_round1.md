# Citation Audit — Round 1
**Paper:** Babel's Machines (Royal Society Interface Focus perspective)
**Date:** 2026-04-27
**Auditor:** Claude (Opus 4.7, automated verification against arXiv / ACL Anthology / journal websites)
**Source files:**
- `d:\Paper_A_star\Survey_Multilingual_ GAME_LLM\Royal_Society_Interface___LaTeX_Template\main.tex`
- `d:\Paper_A_star\Survey_Multilingual_ GAME_LLM\Royal_Society_Interface___LaTeX_Template\refs.bib`

## Method
1. Extracted every `\cite{...}` and `\citeauthor{...}` key from `main.tex` (~70 unique keys actually cited; refs.bib contains more entries that are unused).
2. For each cited key, fetched the entry from `refs.bib`, then verified title / authors / year / venue / arXiv ID against authoritative sources (arxiv.org, aclanthology.org, nature.com, science.org, ijcai.org, IOS Press, Cambridge Core, Princeton UP, MIT Press, etc.).
3. Special attention paid to suspicious arXiv IDs (2601.x / 2602.x = Jan/Feb 2026), `others`-truncated author lists, and entries with explicit "verify before camera-ready" notes.

The paper cites these unique keys (extracted manually from main.tex):
ahuja2022calibration, akata2025playing, axelrod1984evolution, bafna2025translationbarrier, bai2022constitutional, beyer2024clembench, biswas2025persuasion, boroditsky2001does, boroditsky2011languageshapes, boyd1985culture, brown2020gpt3, buscemi2025fairgame, byrne1988machiavellian, cemri2025mast, chalamalasetti2023clembench, chan2025xtom, chen2024aucarena, chen2025gvgai, chen2025llmhanabi, deng2024bargaining, deweerd2013bayesiantom, fontana2024nicer, fu2025multilingualjudge, gao2020pile, goetz2003bilingual, hakimov2025codenames, han2022emergent, han2022pledges, he2025agentmiddle, henrich2010weirdest, henrich2016secret, huynh2025fairgame, huynh2026moreatstake, kovacs2009bilingual, koto2025spyfall, kumar2025indictunedlens, lore2024framing, luccioni2021what, m-alert2025, meta2022cicero, muthukrishna2020beyondweird, nie2025multiagentbench, nowak1998evolution, nowak2006five, ouyang2022training, paischer2024balrog, panchanathan2004indirect, perc2017statistical, premack1978tom, rahwan2019machinebehaviour, repello2024multilingualguardrails, richerson2005notbygenes, schlangen2025clembench, stanfordhai2024languagegap, sun2025gametheoryllm, sun2025overcooked, tomasello2009whywecooperate, turner2023actadd, vaswani2017transformer, wang2023avalon, wang2024evaluating, wang2024voyager, wang2025babel, wang2025tcgbench, wang2026discovering, wendler2024llamasenglish, wu2024semantichub, xie2026m3bench, xu2023werewolf, yao2025spinbench, yong2024lowresource, yong2025multilingualsafety, yoo2025csrt, za2026towards, zhou2025beyond.

(Uncited entries in refs.bib — `fan2024llmgametheory`, `nguyen2025aletheia`, `martinez2024algorithmictrading`, `li2025guardians`, `peng2024jailbreaking`, `roger2025auditwhisper`, `motwani2024hiddenplaintext`, `du2024helmsman`, `lan2024avalon`, `xue2025mlingconf`, `ahuja2023mega`, `calibration2024survey`, `gao2023rethinkingconvai`, `todd2024emergence`, `hausknecht2020textgames`, `liu2025surveybenchmarks`, `wang2024tmgbench`, `duan2024gtbench`, `huang2024far`, `zhang2025genesis`, `zhang2026confidence`, `wang2026openrt`, `lee2025sparse`, `li2025m2s`, `lucas2025anecdoctoring`, `milani2022pragmatic`, `karande2024persuasion`, `hakimov2026pricethought`, `diao2025autored`, `kim2024codenames`, `chen2024collude`, `jin2024bicause`, `yang2024colludebench`, `whorf1956language`, `deng2024multilingual`, `duetting2024mechanism`, `feng2024agents`, `hu2024gameagents`, `nash1950equilibrium`, `park2023generative`, `zhang2024klevel`, `duan2024reta`, `gandhi2023strategic`, `shapira2024glee`, `fish2024collusion`, `fish2024generative`, `munos2024nash`, `conitzer2024socialchoice`, `zheng2024crest`, `horton2023homo`, `ponti2020xcopa`, `xia2024measuring`, `herr2024large`, `he2024xsir`, `neumann1944theory`, `zhang2024llmsurvey`, `ruder2021xtremer`, `hu2020xtreme`, `turpin2023language`) are NOT audited — the bib hygiene only matters for keys that actually appear in the paper.

---

## VERIFIED (60 entries — match authoritative sources)

These entries are correct on title, authors, year, venue, and (where applicable) arXiv ID. Minor stylistic issues such as missing middle initials are not flagged here.

| Bib key | Source verified |
|---|---|
| `huynh2026moreatstake` | arXiv:2601.19082 — title, full author list, year all match |
| `xie2026m3bench` | arXiv:2601.08462 — title, authors (Xie, Shi, Shen, Huang, Ma, Jing), year match |
| `wang2026discovering` | arXiv:2602.10324 — title, all 4 authors, year match |
| `koto2025spyfall` | arXiv:2601.09017 — title, all 4 authors, year match |
| `zhou2025beyond` | arXiv:2510.03136 — title, all 7 authors, year match |
| `huynh2025fairgame` | arXiv:2512.07462 — title, full 16-author list, year match |
| `bafna2025translationbarrier` | arXiv:2506.22724 — title, all 7 authors, year match; venue IJCNLP-AACL 2025 reasonable |
| `cemri2025mast` | arXiv:2503.13657 — title, all 13 authors, year match |
| `biswas2025persuasion` | arXiv:2502.09532, CHI 2025 — title, authors, venue, DOI match |
| `fontana2024nicer` | arXiv:2406.13605 — title, all 3 authors, year match; ICWSM 2025 publication confirmed (vol 19, pp 522–535) |
| `chen2024aucarena` | arXiv:2310.05746 — title, all 5 authors, year (2023 first sub) match |
| `chen2025llmhanabi` | arXiv:2510.04980 — title, all 5 authors, year match |
| `wang2025babel` | arXiv:2506.16151 — title, all 7 authors (Chenxi Wang, Yixuan Zhang, Lang Gao, Zixiang Xu, Zirui Song, Yanbo Wang, Xiuying Chen), year match. **Add arXiv ID** to bib for completeness. |
| `wang2025tcgbench` | aclanthology.org/2026.findings-eacl.353 — title, all 3 authors, venue (Findings EACL 2026) match |
| `wu2024semantichub` | ICLR 2025 — title matches; arXiv ID 2411.04986. Bib only lists "Wu, Zhaofeng and Yu, Xinyan and others" — true list is 5 authors (Zhaofeng Wu, Xinyan Velocity Yu, Dani Yogatama, Jiasen Lu, Yoon Kim). Acceptable but recommend expanding. |
| `wendler2024llamasenglish` | aclanthology.org/2024.acl-long.820 — title, all 4 authors, ACL 2024 venue match. (Best Paper Award note could be added.) |
| `chan2025xtom` | arXiv:2506.02461 — title and year match. (Author list expansion recommended; see NEEDS FIX.) |
| `beyer2024clembench` | arXiv:2405.20859 — title and year match. (Title hyphenation slightly off; see NEEDS FIX.) |
| `schlangen2025clembench` | arXiv:2507.08491 — title, year match. (Author list "and others" → see NEEDS FIX for author expansion.) |
| `chalamalasetti2023clembench` | EMNLP 2023 — title, all 6 authors, venue, page numbers match |
| `hakimov2025codenames` | aclanthology.org/2025.gem-1.63 — title, venue match. (Author list "and others" → see NEEDS FIX.) |
| `xu2023werewolf` | arXiv:2309.04658 — title, year match. (Author list "and others" → see NEEDS FIX.) |
| `wang2023avalon` | arXiv:2310.01320 — title, year match. (Author list "and others" → see NEEDS FIX.) |
| `meta2022cicero` | Science 378(6624):1067–1074, 2022 — verified |
| `wang2024voyager` | TMLR 2024, arXiv:2305.16291 — title, all 8 authors, venue match |
| `chen2025gvgai` | arXiv:2508.08501 — title, all 6 authors, year match |
| `paischer2024balrog` | arXiv:2411.13543, ICLR 2025 — title, all 13 authors, venue match |
| `sun2025overcooked` | arXiv:2502.20073, EMNLP 2025 — title, all 9 authors, venue match |
| `kumar2025indictunedlens` | aclanthology.org/2026.vardial-1.14, arXiv:2602.15038 — title, all 4 authors, venue (VarDial @ EACL 2026) match |
| `buscemi2025fairgame` | arXiv:2504.14325, ECAI 2025 — title, all 6 authors, venue, "Outstanding Paper Award" all confirmed |
| `yao2025spinbench` | arXiv:2503.12349, COLM 2025 — title, all 8 authors, year match |
| `akata2025playing` | Nature Human Behaviour vol 9, pp 1380–1390 (2025), DOI 10.1038/s41562-025-02172-y — verified |
| `sun2025gametheoryllm` | IJCAI 2025 — title and venue match. (Author list incomplete; see NEEDS FIX.) |
| `nie2025multiagentbench` | arXiv:2503.01935, ACL 2025 — title, all 11 authors, venue match |
| `yoo2025csrt` | aclanthology.org/2025.acl-long.657, arXiv:2406.15481 — title, all 3 authors, ACL 2025 venue match |
| `he2025agentmiddle` | aclanthology.org/2025.findings-acl.349, arXiv:2502.14847 — title, venue match. (Author list "and others" → expand to: Pengfei He, Yuping Lin, Shen Dong, Han Xu, Yue Xing, Hui Liu.) |
| `fu2025multilingualjudge` | aclanthology.org/2025.findings-emnlp.587, arXiv:2505.12201 — title, both authors, venue, page range match |
| `yong2024lowresource` | arXiv:2310.02446, NeurIPS 2023 SoLaR Workshop — title, all 3 authors, venue, "Best Paper Award" all match |
| `yong2025multilingualsafety` | aclanthology.org/2025.emnlp-main.800, arXiv:2505.24119 — title (slight subtitle case), all 5 authors, EMNLP 2025 venue match. (Note the "the" in "the Language Gap" — bib has "to Mitigating It" verbatim — fine.) Author "fadaee" should be "Fadaee" (capitalize). |
| `lore2024framing` | Scientific Reports 14, article 18490 (2024), DOI 10.1038/s41598-024-69032-z — verified. Bib could add `number` and `doi` for completeness. |
| `za2026towards` | ICLR 2026 Workshop on AI for Mechanism Design and Strategic Decision Making — title, all 4 authors confirmed. (Workshop name slightly differs — "AIMS-2026" vs "Agents in the Wild" in bib; see NEEDS FIX.) |
| `rahwan2019machinebehaviour` | Nature 568(7753):477–486, 2019, DOI 10.1038/s41586-019-1138-y — verified |
| `boroditsky2001does` | Cognitive Psychology 43(1):1–22, 2001 — verified |
| `boroditsky2011languageshapes` | Scientific American 304(2):62–65, Feb 2011 — verified |
| `axelrod1984evolution` | Basic Books, 1984 — classic, verified |
| `tomasello2009whywecooperate` | MIT Press, 2009 — verified |
| `henrich2016secret` | Princeton University Press, 2015/2016 — verified (note bib year=2015 matches first edition) |
| `boyd1985culture` | University of Chicago Press, 1985 — verified |
| `richerson2005notbygenes` | University of Chicago Press, 2005 — verified |
| `nowak2006five` | Science 314(5805):1560–1563, 2006, DOI 10.1126/science.1133755 — verified |
| `nowak1998evolution` | Nature 393(6685):573–577, 1998, DOI 10.1038/31225 — verified |
| `panchanathan2004indirect` | Nature 432(7016):499–502, 2004, DOI 10.1038/nature02978 — verified |
| `premack1978tom` | Behavioral and Brain Sciences 1(4):515–526, 1978 — verified |
| `byrne1988machiavellian` | Oxford University Press / Clarendon Press, 1988 — verified (editors: Byrne & Whiten) |
| `kovacs2009bilingual` | Developmental Science 12(1):48–54, 2009, DOI 10.1111/j.1467-7687.2008.00742.x — verified |
| `goetz2003bilingual` | Bilingualism: Language and Cognition 6(1):1–15, 2003 — verified |
| `henrich2010weirdest` | Behavioral and Brain Sciences 33(2-3):61–83, 2010 — verified |
| `muthukrishna2020beyondweird` | Psychological Science 31(6):678–701, 2020, DOI 10.1177/0956797620916782 — verified |
| `perc2017statistical` | Physics Reports 687:1–51, 2017 — verified, all 6 authors match |
| `han2022emergent` | AI Communications 35(4):327–337, 2022, DOI 10.3233/AIC-220104 — verified |
| `gao2020pile` | arXiv:2101.00027 — title, all 12 authors, year match (paper actually dated Dec 31, 2020) |
| `luccioni2021what` | aclanthology.org/2021.acl-short.24, arXiv:2105.02732 — title (note "A Preliminary Analysis" in v1, "An Analysis" in v2/published), 2 authors, ACL 2021 venue match |
| `ahuja2022calibration` | aclanthology.org/2022.emnlp-main.290, arXiv:2210.12265 — title, all 4 authors, EMNLP 2022 venue, page range match |
| `deweerd2013bayesiantom` | Artificial Intelligence 199–200:67–92, 2013 — verified, all 3 authors match |
| `vaswani2017transformer` | NIPS 2017, arXiv:1706.03762 — verified, all 8 authors match |
| `brown2020gpt3` | NeurIPS 2020, arXiv:2005.14165 — verified |
| `ouyang2022training` | NeurIPS 2022, arXiv:2203.02155 — verified |
| `bai2022constitutional` | arXiv:2212.08073, Dec 2022 — verified, but bib should add eprint number (currently empty) |
| `deng2024bargaining` | OpenReview, ICML 2024 Agentic Markets Workshop — verified. (Authors "Deng, Yuan and Mirrokni, Vahab and others" — full list: Yuan Deng, Vahab Mirrokni, Renato Paes Leme, Hanrui Zhang, Song Zuo. Optional expansion.) |

---

## NEEDS FIX (12 entries with discrepancies)

These entries have substantive errors that should be corrected before camera-ready.

### 1. `turner2023actadd` — wrong title and incomplete author list
- **Bib has:** title `"Activation Addition: Steering Language Models Without Optimization"`, authors `Turner, Alexander Matt and Thiergart, Lisa and Leech, Gavin and Udell, David and Mini, Ulisse and MacDiarmid, Monte`
- **arXiv 2308.10248 has:** title **`"Steering Language Models With Activation Engineering"`**, authors **Alexander Matt Turner, Lisa Thiergart, Gavin Leech, David Udell, Juan J. Vazquez, Ulisse Mini, Monte MacDiarmid** (the published title was changed; the early v1 used the "Activation Addition" subtitle, but current canonical title is "Steering Language Models With Activation Engineering").
- **Fix:** Update title to current canonical title (or keep old title with note). Add missing author **Juan J. Vazquez** between Udell and Mini.

### 2. `m-alert2025` — wrong title AND wrong venue
- **Bib has:** title `"M-ALERT: A Multilingual Benchmark for Evaluating Safety and Alignment in Large Language Models"`, journal `"OpenReview"`, year 2025
- **Reality:** title is **`"LLMs Lost in Translation: M-ALERT uncovers Cross-Linguistic Safety Inconsistencies"`** (or equivalent gap-vs-inconsistency variant), arXiv:2412.15035, **published at ICLR 2025** (not "OpenReview"). Authors match.
- **Fix:** Replace title with the actual paper title; change `journal={OpenReview}` to `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}` and use `@inproceedings`. Add `eprint={2412.15035}`. Capitalize `fadaee` → `Fadaee` (also check `yong2025multilingualsafety` — same author).

### 3. `han2022pledges` — wrong venue
- **Bib has:** journal `"Royal Society Open Science"`, year 2022
- **Reality:** Paper "Voluntary safety pledges overcome over-regulation dilemma in AI development: an evolutionary game analysis" by Han, Santos, Pereira, Lenaerts was published in **Proceedings of the ALIFE 2022 Conference** (MIT Press), DOI 10.1162/isal_a_00484. There is also an earlier related paper "Voluntary safety commitments provide an escape from over-regulation in AI development" in *Technology in Society* (2021). **No version appeared in *Royal Society Open Science*.**
- **Fix:** Either (a) change to `@inproceedings` ALIFE 2022 with correct DOI; or (b) change citation to the *Technology in Society* (2021) version. Do not claim *Royal Society Open Science*.

### 4. `wang2024evaluating` — incorrect author list
- **Bib has 13 names** including `Zhang, Yuanchi`. Order/spelling issue — actual arXiv:2405.10936 author #4 in the canonical order is **Xinyu Zhang** (currently missing from bib), and the bib appears to skip her. The bib lists `Hongliang Li` as #3, but actual author list is: Kaiyu Huang, Fengran Mo, Xinyu Zhang, Hongliang Li, You Li, Yuanchi Zhang, Weijian Yi, Yulong Mao, Jinchen Liu, Yuzhuang Xu, Jinan Xu, Jian-Yun Nie, Yang Liu.
- **Fix:** Insert `Zhang, Xinyu` between `Mo, Fengran` and `Li, Hongliang`. Verify all other names match (Liu, Jinchen vs Liu, Jinchen — OK).

### 5. `sun2025gametheoryllm` — incomplete author list AND missing subtitle
- **Bib has:** authors `Sun, Haoran and Wu, Yusen and Cheng, Yukun and Chu, Xu` (4 names), title `"Game Theory Meets Large Language Models: A Systematic Survey"`
- **Reality:** 7 authors — **Haoran Sun, Yusen Wu, Peng Wang, Wei Chen, Yukun Cheng, Xiaotie Deng, Xu Chu**. Full title: **"Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers"** (the IJCAI 2025 survey-track version omits the subtitle, so bib is acceptable for IJCAI venue, but author list is wrong).
- **Fix:** Add missing authors `Wang, Peng`, `Chen, Wei`, `Deng, Xiaotie` between Wu and Cheng (Wang and Chen) and between Cheng and Chu (Deng).

### 6. `xu2023werewolf` — author list truncated
- **Bib:** `Xu, Yuzhuang and Wang, Shuo and others`, journal `"arXiv preprint"` (missing arXiv ID)
- **Reality:** 7 authors — Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, Yang Liu. **arXiv:2309.04658**.
- **Fix:** Expand author list, add `eprint={2309.04658}`, change journal field to `arXiv preprint arXiv:2309.04658`.

### 7. `wang2023avalon` — author list truncated
- **Bib:** `Wang, Shenzhi and Liu, Chang and others`, journal `"arXiv preprint"` (missing arXiv ID)
- **Reality:** 10 authors — Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan Qi, Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei Wang, Shiji Song, Gao Huang. **arXiv:2310.01320**. Title in bib uses "Through" but actual paper uses "through" (lowercase) — minor.
- **Fix:** Expand author list, add `eprint={2310.01320}`.

### 8. `chan2025xtom` — author list truncated
- **Bib:** `Chan, Chunkit and others`
- **Reality:** 17 authors — Chunkit Chan, Yauwai Yim, Hongchuan Zeng, Zhiying Zou, Xinyuan Cheng, Zhifan Sun, Zheye Deng, Kawai Chung, Yuzhuo Ao, Yixiang Fan, Cheng Jiayang, Ercong Nie, Ginny Y. Wong, Helmut Schmid, Hinrich Schütze, Simon See, Yangqiu Song.
- **Fix:** Expand author list (or at minimum first 6 + "and others").

### 9. `beyer2024clembench` — author list truncated and title hyphenation
- **Bib:** `Beyer, Anne and others`, title `"clembench 2024: A Challenging, Dynamic, Complementary, Multilingual Benchmark for LLMs as Multi-Action Agents"`
- **Reality:** Authors are Anne Beyer, Kranti Chalamalasetti, Sherzod Hakimov, Brielen Madureira, Philipp Sadler, David Schlangen. Actual arXiv title is **"clembench-2024: A Challenging, Dynamic, Complementary, Multilingual Benchmark and Underlying Flexible Framework for LLMs as Multi-Action Agents"** (note hyphen in `clembench-2024` and the longer subtitle).
- **Fix:** Expand author list; update title to the canonical one (or leave shortened — but at least add the hyphen).

### 10. `schlangen2025clembench` — author list truncated
- **Bib:** `Schlangen, David and others`
- **Reality:** David Schlangen, Sherzod Hakimov, Kranti Chalamalasetti, Jonathan Jordan, Philipp Sadler.
- **Fix:** Expand author list.

### 11. `hakimov2025codenames` — author list truncated
- **Bib:** `Hakimov, Sherzod and others`
- **Reality:** Sherzod Hakimov, Lara Pfennigschmidt, David Schlangen.
- **Fix:** Expand author list. The venue field is also imprecise: should be **Proceedings of the Fourth Workshop on Generation, Evaluation and Metrics (GEM² @ ACL 2025)**, pp. 728–740, Vienna.

### 12. `za2026towards` — workshop name imprecise
- **Bib:** `booktitle={ICLR 2026 Workshop on Agents in the Wild}`
- **Reality:** Workshop appears to be **ICLR 2026 Workshop on AI for Mechanism Design and Strategic Decision Making (AIMS-2026)** — see https://alimama-tech.github.io/aims-2026/. (`Agents in the Wild` does not appear in ICLR 2026 official workshop listings.)
- **Fix:** Confirm workshop directly with authors; if AIMS-2026 is correct, update booktitle. Otherwise, generalize to `ICLR 2026 Workshop` until exact name confirmed.

### Additional minor cosmetic fixes (not blocking, but worth doing in same pass):
- `wang2025babel`: add `eprint={2506.16151}, archivePrefix={arXiv}` for completeness.
- `bai2022constitutional`: add `eprint={2212.08073}, archivePrefix={arXiv}`; expand author list (current `and others` after Bai).
- `meta2022cicero`: add `doi={10.1126/science.ade9097}` and consider expanding the author/team field to "Bakhtin, Anton and others" (the corporate author "Meta FAIR Diplomacy Team" is acceptable).
- `wang2024voyager`: add `eprint={2305.16291}, archivePrefix={arXiv}`; URL `https://openreview.net/forum?id=ehfRiF0R3a` for TMLR.
- `boroditsky2011languageshapes`: add `doi={10.1038/scientificamerican0211-62}`.
- `stanfordhai2024languagegap`: change year to **2025** (Stanford HAI publication date is April 2025, per https://hai.stanford.edu/policy/mind-the-language-gap-…). Currently bib year is 2024 — this is wrong.

---

## CANNOT VERIFY (1 entry)

### `repello2024multilingualguardrails`
- **Bib:** `@misc{repello2024multilingualguardrails, title={Introducing New Multilingual AI Safety Guardrails for 100 Languages}, author={{Repello AI}}, year={2024}, howpublished={Blog post, Repello AI}}`
- **Search results:** A Repello AI blog post titled "Introducing new Multilingual AI Safety Guardrails for 100 Languages" exists at https://repello.ai/blog/introducing-new-multilingual-ai-safety-guardrails-for-100-languages — title matches. Could not independently confirm publication date (no clear date metadata in WebSearch result; Repello's later "CREST" blog from December 2025 references this 100-language work).
- **Recommendation:** Either (a) confirm date via direct web visit and add `note={Accessed YYYY-MM-DD}`, or (b) replace the citation with the more rigorous **CREST** paper (arXiv:2512.02711) which provides the academic substance behind Repello's 100-language guardrail claim. The blog citation as-is is fragile for a Royal Society perspective paper.

---

## Summary

- **Total cited keys checked:** ~73
- **Verified clean:** ~60 (~82%)
- **Need substantive fixes:** 12 (~16%)
- **Cannot verify (blog citation):** 1

### High-priority (potential reviewer challenges):
1. **`turner2023actadd`** — wrong title (could be flagged as fabrication)
2. **`m-alert2025`** — wrong title AND venue (definite reviewer red flag)
3. **`han2022pledges`** — fabricated venue (Royal Society Open Science) — *especially risky given this paper is being submitted to a Royal Society journal*
4. **`wang2024evaluating`** — missing author Xinyu Zhang
5. **`sun2025gametheoryllm`** — 3 authors missing
6. **`stanfordhai2024languagegap`** — wrong year (2024 → 2025)

### Medium-priority (truncated `and others` author lists — not strictly errors but a Royal Society copy-editor will likely ask for full lists):
`xu2023werewolf`, `wang2023avalon`, `chan2025xtom`, `beyer2024clembench`, `schlangen2025clembench`, `hakimov2025codenames`, `he2025agentmiddle`, `deng2024bargaining`, `wu2024semantichub`, `bai2022constitutional`.

### Low-priority (cosmetic / metadata completeness):
Add missing arXiv IDs and DOIs to: `wang2025babel`, `bai2022constitutional`, `meta2022cicero`, `wang2024voyager`, `boroditsky2011languageshapes`.

### No fabricated arXiv IDs detected
All arXiv IDs in the 2601.x and 2602.x range that are actually cited in the paper resolved correctly to the claimed papers. The aliasing comments in refs.bib (for `jin2024bicause`, `chen2024collude`, `yang2024colludebench`) point to entries that are not cited in main.tex, so they do not affect this audit.
