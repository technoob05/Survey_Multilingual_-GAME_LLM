Game Theory Meets Large Language Models: A Systematic SurveyHaoran Sun1,Yusen Wu1,Yukun Cheng2∗andXu Chu1,3∗1Center on Frontiers of Computing Studies, School of Computer Science, Peking University2School of Business, Jiangnan University3Key Laboratory of High Confidence Software Technologies, Ministry of Education{sunhaoran0301, 2401112067}@stu.pku.edu.cn, ykcheng@amss.ac.cn, chuxu@pku.edu.cnAbstractGame theory establishes a fundamental frameworkfor analyzing strategic interactions among rationaldecision-makers.  The rapid advancement of largelanguage models (LLMs) has sparked extensive re-search exploring the intersection of these two fields.Specifically, game-theoretic methods are being ap-plied  to  evaluate  and  enhance  LLM  capabilities,while LLMs themselves are reshaping classic gamemodels. This paper presents a comprehensive surveyof the intersection of these fields, exploring a bidi-rectional relationship from three perspectives:  (1)Establishing standardized game-based benchmarksfor evaluating LLM behavior; (2) Leveraging game-theoretic methods to improve LLM performancethrough algorithmic innovations; (3) Characterizingthe societal impacts of LLMs through game model-ing. Among these three aspects, we also highlighthow the equilibrium analysis for traditional gamemodels is impacted by LLMs’ advanced languageunderstanding, which in turn extends the study ofgame theory. Finally, we identify key challenges andfuture research directions, assessing their feasibilitybased on the current state of the field. By bridgingtheoretical rigor with emerging AI capabilities, thissurvey aims to foster interdisciplinary collaborationand drive progress in this evolving research area.1    IntroductionGame  theory  provides  a  mathematical  framework  for  ana-lyzing strategic interactions among rational agents and hasevolved significantly since its seminal work[Von Neumannand  Morgenstern,  2007].   Over  the  decades,  it  has  estab-lished robust methodological foundations, including equilib-rium analysis[Nash Jr, 1950]and mechanism design[Vickrey,1961], which serve as essential analytical tools across disci-plines such as economics and computer science.With  the  rapid  advancement  of  large  language  models(LLMs), researchers have increasingly explored the intersec-tion of game theory and LLMs.  A growing body of work∗Corresponding Authors.investigates how game-theoretic principles can be used to eval-uate and enhance LLMs and how LLMs can contribute togame theory.  Specifically, existing studies apply game the-ory to develop theoretical frameworks for assessing LLMs’strategic reasoning.  This approach optimizes their trainingmethodologies and analyzes their societal implications. Keyresearch directions include:•Standardized Game-Based Evaluation: Researchers areconstructing benchmark environments, such as matrixgames[Akataet al.,  2023]and auctions[Chenet al.,2023], to evaluate the strategic reasoning capabilities ofLLMs systematically.•Game-Theoretic Algorithmic Innovation: Concepts fromcooperative and non-cooperative game theory, such asShapley Value[Enouenet al., 2024]and max-min equilib-ria[Munoset al., 2024], are inspiring novel approachesto model interpretability and training optimization.•Societal Impact Modeling: As LLMs transform informa-tion ecosystems, new theoretical frameworks are emerg-ing to predict the societal consequences of human-AIinteractions[Yaoet al., 2024], particularly in domainslike advertising markets[Duettinget al., 2024]and con-tent creation[Fishet al., 2024a].Beyond these applications, recent research suggests that LLMscan also contribute to game theory by facilitating equilibriumanalysis in complex text-based scenarios and extending classi-cal models to more realistic settings.Existing surveys[Zhanget al., 2024b; Fenget al., 2024;Huet al., 2024]primarily examine how game theory can beused to build evaluation environments and assess LLMs’ strate-gic performance. For instance,[Zhanget al., 2024b]classifiesstudies based on the game scenarios used to test LLM capabil-ities and methods for improving their reasoning. Meanwhile,[Fenget al., 2024]and[Huet al., 2024]categorize the corecompetencies required for LLM-based agents in games, suchas perception, memory, role-playing, and reasoning.  Whilethese surveys provide valuable insights, they primarily focuson the role of game theory in standardized evaluation frame-works, overlooking its broader potential for advancing LLMdevelopment. Moreover, they adopt a unidirectional perspec-tive, treating game theory as a tool for assessing LLMs ratherthan exploring the reciprocal influence between the two fields.Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10669

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.von2007theory)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.von2007theory)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.nash1950equilibrium)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.vickrey1961counterspeculation)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.vickrey1961counterspeculation)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.akata2023playing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2023put)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2023put)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.enouen2023textgenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.NLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.yaohuman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duetting2024mechanism)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2023generative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024llm)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.feng2024survey)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hu2024survey)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024llm)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.feng2024survey)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hu2024survey)

This paper aims tobridge this gap by examining the bidi-rectional relationship between game theory and LLMs.Wecategorize the work in the intersection between game theoryand LLMs into three key perspectives, as illustrated in Figure 1.To the best of our knowledge, this isthe first comprehensiveanalysis of the bidirectional relationship between these twofields.In Section 2, we review studies that apply game models toevaluate LLMs’ decision-making capabilities.  Experimentsconducted on both canonical matrix games and complex strate-gic scenarios reveal LLMs’ strengths and limitations as gameplayers. Beyond behavioral evaluations, we identify key strate-gies for enhancing LLMs’ strategic decision-making, such asrecursive reasoning frameworks and the integration of LLMswith auxiliary modules.  Moreover, LLMs demonstrate theability to formalize real-world scenarios into structured gamemodels,  extending  game-theoretic  analysis  to  broader  andmore complex contexts.Section 3 examines how game-theoretic principles addresskey challenges in LLM development. We categorize existingresearch into two main areas: (1) using game theory to under-stand LLMs’ text generation and training dynamics and (2)leveraging game-theoretic mechanisms to enhance LLM train-ing algorithms. The first category explores how the ShapleyValue improves model interpretability and how social choicetheory facilitates preference alignment in human-AI interac-tions. The second category introduces studies that incorporategame-theoretic objectives to tackle challenges like heterogene-ity  and  complexity  in  human  preferences.   The  objectivesinclude minimizing regret in multi-agent interactions and eval-uation metrics, including Nash equilibrium convergence,In Section 4, we discuss how game theory is used to predictand characterize the societal impact of LLMs. The human-AIinteraction game model predicts the impact of competitionbetween humans and AI. Emerging game models highlightthe growing business and economic implications where LLMsare treated as products or platforms. Meanwhile, classic gametheory models are also generalized to more realistic settingswith  LLMs’  unique  capabilities,  such  as  natural  languagemanipulation.Finally, we identify key research challenges and future di-rections across these dimensions. By systematically analyzingthe intersection of game theory and LLMs, we highlight theirmutual influence and how they drive progress in both fields,contributing to the advancement of this interdisciplinary do-main.2    Game Theory for LLM EvaluationIn this section, we explore the integration of LLMs within thecontext of game theory, focusing on their evaluation as gameplayers.  Behavioral evaluations reveal that LLMs face chal-lenges in identifying optimal actions in classic matrix games,yet they can demonstrate human-like strategies in more com-plex game scenarios. Several studies have explored methodsto enhance LLMs’ performance as game players, and two sig-nificant points can be identified from that: recursive thinkingand auxiliary modules.  Finally, we also discuss the role ofLLMs in games beyond their function as players.2.1    Evaluation of LLMs’ Behavioral PerformanceStruggles of LLM in Matrix Games.Matrix games area fundamental concept in game theory.   In a matrix game,two players make simultaneous decisions, and the outcomescan be represented by a finite payoff matrix.  Recent stud-ies have investigated how LLMs respond to these games byconverting them into natural language prompts. Despite sig-nificant advancements, their results show that LLMs such asGPT-4 struggle to consistently select the optimal strategy in2×2matrix games[Akataet al., 2023; Herret al., 2024;Lor `e and Heydari, 2024; Wanget al., 2024].For  instance,[Akataet  al.,  2023]states  that  LLMs  fre-quently fail to choose the optimal action in coordination games,like the Battle of the Sexes.  Similarly,[Lor`e and Heydari,2024]examines how contextual framing and utility matricesinfluence LLM decision-making, revealing significant biases.Furthermore,[Herret al., 2024]explores the impact of gamedescriptions, player positioning, and payoffs on LLM perfor-mance, highlighting consistent behavioral biases. In more dy-namic settings,[Fanet al., 2024]observes that LLMs struggleto predict optimal strategies in ring-network games.  Addi-tionally, the TMGBench benchmark, which evaluates LLMsacross 144 distinct2×2matrix games, further confirms theselimitations[Wanget al., 2024].The matrix game is a cornerstone of game theory and is thefoundation for more intricate strategic challenges. StudyingLLMs’ behaviors in such games provides valuable insightsinto their broader limitations in complex reasoning tasks.Human-like Strategies of LLM in Realistic Game Scenar-ios.Beyond classic matrix games, numerous studies haveanalyzed LLM performance in more realistic game settings.While these games feature greater contextual complexity, theyare not necessarily more challenging for LLMs.  This is be-cause strategic inference based on textual content can some-times replace explicit computation.Research indicates that LLMs can exhibit strategic behaviorin communication-based games. In deception and negotiationgames, including Werewolf[Xuet al., 2023; Du and Zhang,2024]and Avalon[Wanget al., 2023; Lanet al., 2024], LLMsdemonstrate behaviors such as deception, trust-building, andleadership—traits typically associated with human strategicthinking. These findings suggest that LLMs can function assophisticated communication agents in games.LLMs have also demonstrated strategic reasoning in eco-nomically significant scenarios such as bargaining and pricinggames.  For instance,[Denget al., 2024]finds that LLMspossess advanced negotiation skills, while[Fishet al., 2024b]shows that LLM-based pricing agents can autonomously en-gage in collusion to set prices above competitive levels.  Inauction contexts,[Guoet al., 2024]finds that LLMs can for-mulate rational bidding strategies based on historical data,often converging toward a Nash equilibrium. Similarly,[Chenet al., 2023]introduces AucArena, a platform where LLMseffectively manage budgets and optimize auction strategies.Comprehensive  Benchmarks   for   Game   Performance.Several benchmarks that cover a diverse range of game sce-narios have been developed to make a systematic assessmentof LLM. Notable examples include GTBench[Duanet al.,Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10670

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#figure.caption.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.3)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.4)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.akata2023playing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.herr2024large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lore2024strategic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.akata2023playing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lore2024strategic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lore2024strategic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.herr2024large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fan2024can)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xu2023exploring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.du2024helmsman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.du2024helmsman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2023avalon)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lan2023llm)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.llmbargaining)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2024algorithmic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.guo2024economics)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2023put)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2023put)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024gtbench)

Game TheoryMeets LLMGame-basedEvaluation §2PerformanceEvaluation §2.1Matrix Games[Akataet al., 2023],[Lor`e and Heydari, 2024],[Fanet al., 2024],[Wanget al., 2024],[Herret al., 2024],Communication GamesWerewolf[Xuet al., 2023],[Du and Zhang, 2024],Avalon[Wanget al., 2023],[Lanet al., 2024],Auction[Chenet al., 2023], Bargaining[Xiaet al., 2024],[Denget al., 2024], Collusion[Fishet al., 2024b]BenchmarksGTBench[Duanet al., 2024b],γ-bench[Huanget al., 2024],GameBench[Huaet al., 2024], TMGBench[Wanget al., 2024],GLEE[Shapiraet al., 2024], Economics Arena[Guoet al., 2024],PerformanceEnhancement §2.2[Wanget al., 2023],[Duanet al., 2024a],[Zhanget al., 2024a],[Gandhiet al., 2023],[Xuet al., 2023],[Xiaet al., 2024],[Huaet al., 2024]Beyond asA Player §2.3[Mensfeltetal., 2024],[Denget al., 2025],[Horton, 2023]AlgorithmicInnovation §3Understanding §3.1Generation[Liuet al., 2023], TextGenSHAP[Enouenet al., 2024],TokenSHAP[Goldshmidt and Horovicz, 2024],[Mohammadi, 2024],[Zhanget al., 2024c]Training andLimitations[Mishra, 2023],[Conitzeret al., 2024],[Geet al., 2024],[Qiu, 2024],[Zhanget al., 2024e], Decoding Game[Chenet al., 2025]Improvement §3.2General PreferenceNLHF[Munoset al., 2024], SPO[Swamyet al., 2024],SPPO[Wuet al., 2025], DNO[Rossetet al., 2024],INPO[Zhanget al., 2024d],[Zhi-Xuanet al., 2024]HeterogeneousPreferencesMaxmin-RLHF[Chakrabortyet al., 2024b],[Parket al., 2024],PAL[Chenet al., 2024a],[Fleisiget al., 2023],[Klingefjordet al., 2024],[Alamdariet al., 2024]Data Cost EfficiencySPIN[Chenet al., 2024b],[Zhenget al., 2024],VickeryFeedback[Zhang and Duan, 2024],[Chenget al., 2024b],Other Two-playerGame FormulationPARL[Chakrabortyet al., 2024a], APO[Chenget al., 2024b],STA-RLHF[Makar-Limanovet al., 2024],[Gempet al., 2024],Consensus Game[Jacobet al., 2023]LLM-relatedGame Scenarios §4Competition betweenLLM and Human §4.1[Yaoet al., 2024],[Esmaeiliet al., 2024],[Taitler and Ben-Porat, 2024]Game ScenariosArising with LLM §4.2Token Auction[Duettinget al., 2024],[Hajiaghayiet al., 2024],Segment Auction[Dubeyet al., 2024],[Feiziet al., 2023],Fine-tuning Game[Lauferet al., 2024],[Mahmood, 2024],RLHF Game[Sunet al., 2024a],[Soumaliaset al., 2024]LLM Extends ClassicGame Model §4.3[Luet al., 2024],[Fishet al., 2024a],[Sunet al., 2024b]Figure 1: A taxonomy of the intersection between game theory and Large Language Models.2024b],γ-bench[Huanget al., 2024], GameBench[Huaet al.,2024], GLEE[Shapiraet al., 2024], and TMGBench[Wanget al., 2024].  These benchmarks serve to identify both thestrengths and weaknesses of LLMs in different strategic en-vironments, offering valuable insights into their potential im-provements and real-world applications.2.2    Enhancing LLMs’ Game PerformanceBuilding on the evaluation of LLMs’ performance in variousgames, numerous studies have explored methods to enhancetheir strategic reasoning and decision-making. These worksaddress key challenges LLMs face in gameplay and proposegeneral frameworks for improving their capabilities. Below,we outline two significant approaches.Recursively  Thinking.In  games  requiring  long-term  ormulti-level reasoning, LLMs often struggle to retain and buildupon previous information, leading to suboptimal decision-making.  To mitigate this, researchers have developed tech-niques that encourage LLMs to engage in recursive thinking,enabling them to leverage past information better when formu-lating strategies.For instance,[Wanget al., 2023]introduces the RecursiveContemplation (ReCon) framework. The framework promptsLLMs to engage in first-order and second-order perspective-taking during Avalon gameplay. This helps them avoid com-mon pitfalls, such as deception. Similarly,[Duanet al., 2024a]proposes a method where LLMs predict future moves in multi-turn games, improving their ability to anticipate opponents’strategies. Additionally,[Zhanget al., 2024a]advances LLMreasoning through k-level rationality, which enhances multi-level thinking and significantly increases their win rates incompetitive settings. These findings suggest that recursive rea-soning can substantially improve LLMs’ strategic capabilities.Auxiliary Modules.As language models, LLMs often strug-gle in games that require complex mathematical calculationsor historical data retrieval. Several studies have proposed inte-grating auxiliary modules that assist LLMs during gameplayto overcome these limitations.For example,[Gandhiet al., 2023]introduces a “promptProceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10671

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024gtbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.2.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.akata2023playing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lore2024strategic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fan2024can)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.herr2024large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xu2023exploring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.du2024helmsman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2023avalon)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lan2023llm)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2023put)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xia2024measuring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.llmbargaining)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2024algorithmic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024gtbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.huang2024far)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.shapira2024glee)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.guo2024economics)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.2.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2023avalon)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024reta)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024k)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.gandhi2023strategic)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xu2023exploring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xia2024measuring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.2.3)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mensfelt2024autoformalizing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.deng2025natural)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.horton2023large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.3)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.3.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.liu2023prompt)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.enouen2023textgenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.goldshmidt2024tokenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mohammadi2024wait)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024investigating)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mishra2023ai)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.conitzerposition)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.ge2024axioms)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.qiu2024representative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024incentive)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2024decoding)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.3.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.NLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SelfPlayPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.DNO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.IiterativeNPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhi2024beyond)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024maxmin)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.park2024rlhf)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2024pal)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fleisig2023majority)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.klingefjord2024human)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alamdari2024policy)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SPIN)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alignmenttwoplayer)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024vickreyfeedback)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024adversarial)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024parl)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024adversarial)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.STARLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.gemp2024states)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.jacob2023consensus)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#section.4)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.4.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.yaohuman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.esmaeili2024strategize)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.taitler2024braess)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.4.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duetting2024mechanism)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.adRAG)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.adSummaries)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.feizi2023online)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.laufer2024fine)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mahmoodpricing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.sun2024mechanism)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.soumalias2024truthful)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.4.3)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lu2024eliciting)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2023generative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.sun2024large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024gtbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024gtbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.huang2024far)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.shapira2024glee)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2024tmgbench)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.wang2023avalon)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duan2024reta)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024k)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.gandhi2023strategic)

compiler”, which systematically guides LLMs in evaluatingactions and forming beliefs, enabling them to generalize tonew scenarios with minimal in-context learning. In the gameWerewolf,[Xuet al., 2023]integrates an additional BERTmodel to encode both historical and current game states, al-lowing LLMs to make more informed decisions.In bargaining games, the OG-Narrator framework[Xiaetal., 2024]generates external offers, allowing the LLM to focussolely on negotiation language.  More recently,[Huaet al.,2024]developed  a  structured  workflow  to  assist  LLMs  insolving game-theoretic problems, including computing Nashequilibria and optimizing strategies in complex negotiationtasks.These auxiliary modules significantly improve LLMs’ per-formance in various game settings, demonstrating that integrat-ing additional computational tools can enhance their strategicdecision-making.2.3    Beyond as a Game PlayerWhile much of the discussion has been centered on utilizinggame-based scenarios to evaluate LLMs, work has also shownthat LLM capability in games can, in turn, contribute to gametheory. This section explores alternative roles for LLMs withingame-theoretic contexts, broadening their applications.In section 2.1, we noted that LLMs often struggle to com-pute optimal strategies in classical matrix games.  However,some studies take an alternative approach by leveraging LLMs’natural language understanding instead of their ability to com-pute equilibria directly. For example,[Mensfeltet al., 2024]utilizes LLMs to formalize game descriptions into a GameDescription Language (GDL), allowing external solvers toprocess them. Similarly,[Denget al., 2025]introduces a two-stage framework for translating extensive-form games: first,the LLM identifies the information set, and then it constructsthe complete game tree using in-context learning. These stud-ies suggest that LLMs can act as intermediaries in convertingnatural language into formal game structures,  a capabilitybeyond traditional models.Additionally,[Horton,  2023]explores  the  use of  LLMsas substitutes for human participants in behavioral economicexperiments. Their findings indicate that LLMs can replicateclassic  behavioral  economics  results,  providing  a  scalableand cost-effective alternative for conducting social scienceresearch. This underscores the potential of LLMs as valuabletools in experimental economics and social science studies,facilitating large-scale simulations and deeper insights intohuman decision-making.3    Game Theory for Algorithmic InnovationThis section investigates how game-theoretic principles con-tribute to developing LLMs by informing algorithmic innova-tion. Game theory has proven instrumental in enhancing ourunderstanding of LLMs, mainly through the use of tools likethe Shapley Value and social choice models. These methodsoffer valuable insights into model interpretability, enablinga deeper understanding of how LLMs process and respondto input. Beyond interpretability, game theory also providesa framework for developing training objectives and evalua-tion metrics that address key challenges in LLM development,such as model heterogeneity and alignment with human pref-erences.3.1    Game Theory for PhenomenologicalUnderstanding LLMsThis line of research applies classical game theory concepts toexplain observable phenomena in LLMs, including patterns intext generation and the inherent limitations of training withinspecific frameworks.  Such studies are particularly valuablegiven that LLMs are often treated as “black boxes” due to theirproprietary nature and large-scale complexity.One approach connects cooperative game theory to LLMs,as these models perform parallel computations on input tokensand are structured around transformer layers.  The ShapleyValue[Shapley, 1953], a method for attributing contributionsto individual players in cooperative games, has been adaptedto assess the influence of specific tokens and layers on LLM-generated outputs. Several studies leverage the Shapley Valueto evaluate token significance in prompts[Goldshmidt andHorovicz, 2024; Mohammadi, 2024]. For example,[Moham-madi, 2024]demonstrates that LLMs often assign dispropor-tionately high weights to less informative input components, abehavior strongly correlated with incorrect responses. Token-SHAP[Goldshmidt and Horovicz, 2024]enhances ShapleyValue computation using Monte Carlo sampling for efficiency,while TextGenSHAP[Enouenet al., 2024]extends the ap-proach to longer, structured input-output scenarios.[Liuetal., 2023]applies the Shapley Value to multi-prompt learning,identifying the most impactful prompts for ensemble gener-ation.  Similarly,[Zhanget al., 2024c]analyzes LLM layercontributions, finding that earlier layers exert a more signifi-cant influence on output generation.Another research direction models LLM alignment withdiverse human preferences using social choice theory.  Thisframework helps address challenges aligning LLMs with hu-man values and decision-making processes[Mishra, 2023].For instance,[Conitzeret al., 2024]analyzes the role of Rein-forcement Learning from Human Feedback (RLHF) in express-ing human preferences, identifying fundamental issues arisingfrom preference conflicts, and advocating for social choiceprinciples in LLM alignment.[Geet al.,  2024]examinesRLHF reward modeling as a social choice process, demonstrat-ing that Bradley-Terry-based approaches suffer from intrinsiclimitations that violate key axioms.[Qiu, 2024]proposes arepresentative social choice framework, which extracts a smallbut representative subset of opinions to manage large-scalepreference aggregation effectively.Additionally,  some studies apply game theory to modelalignment and decoding strategies.[Zhanget al., 2024e]ex-amine sociotechnical implications of real-world LLM appli-cations, advocating for incentive compatibility to ensure AIsystems align with societal goals while maintaining technicalrobustness.[Chenet al., 2025]models the LLM decodingprocess as a Stackelberg game, where the decoder moves first,and an adversarial entity follows. By analyzing optimal strate-gies for both players, their study provides a theoretical basisfor why heuristic sampling strategies perform well in practice.Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10672

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xu2023exploring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xia2024measuring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.xia2024measuring)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.hua2024game)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.2.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mensfelt2024autoformalizing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.deng2025natural)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.horton2023large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.shapley1953value)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.goldshmidt2024tokenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.goldshmidt2024tokenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mohammadi2024wait)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mohammadi2024wait)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mohammadi2024wait)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.goldshmidt2024tokenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.enouen2023textgenshap)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.liu2023prompt)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.liu2023prompt)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024investigating)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mishra2023ai)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.conitzerposition)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.ge2024axioms)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.qiu2024representative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024incentive)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2024decoding)

3.2Game Theory for Stimulating LLM AlgorithmsIn addition to enhancing our understanding of LLMs, gametheory plays a crucial role in designing algorithms that im-prove their capabilities.  This section highlights several keychallenges in LLM training and illustrates how game theoryhas been applied to address these issues.General Human Preference.Standard reward-based RLHFis limited to capturing only transitive preferences[Munosetal., 2024].  Preference models, however, can express moregeneral preferences by comparing two policies rather thanassigning a reward for each response.  This introduces newchallenges in optimizing an LLM based on preference mod-els. Nash Learning from Human Feedback (NLHF) aims tooptimize the von Neumann winner of a game defined by thepreference model, offering a feasible and robust direction forpolicy optimization.Based  on  NLHF,  SPO[Swamyet  al.,  2024]introducesmethods  to  express  more  complex  preferences,  such  asnon-transitive,  stochastic,  and  non-Markovian  preferences.SPPO[Wuet al., 2025]designs an algorithm that efficientlyimplements SPO-like algorithms in large-scale language mod-els. DNO[Rossetet al., 2024]improves LLM optimizationusing a regression-based objective for more efficient and di-rect training.  INPO[Zhanget al., 2024d]introduces a lossfunction that can be directly minimized on preference datasets,further reducing the time overhead associated with calculatingwin rates in NLHF.However, recent work by[Zhi-Xuanet al., 2024]pointsout that preference-based approaches oversimplify human val-ues,  neglecting  their  complexity,  incommensurability,  anddynamic nature. As a result, designing more robust methodsfor aligning human preferences remains an ongoing scientificchallenge.Heterogeneity in Human Preferences.Capturing hetero-geneity  in  human-annotated  datasets  remains  a  significantchallenge in LLM alignment. Ignoring this heterogeneity of-ten results in models that reflect only the preferences of themajority[Fleisiget al., 2023]. Several studies have developedmore inclusive training and alignment algorithms using socialchoice theory[Chakrabortyet al., 2024b; Parket al., 2024;Alamdariet al., 2024; Chenet al., 2024a].[Chakrabortyetal., 2024b]demonstrates the impracticality of using a singlereward model and proposes the Egalitarian principle to learnpreference distributions.[Parket al., 2024]suggests cluster-ing preferences and proposes a scalable, incentive-compatibleframework for preference alignment.[Alamdariet al., 2024]employs  Borda  count  and  quantile  fairness  for  preferenceaggregation, ensuring fairness and computational feasibility.[Chenet al., 2024a]introduces a mixture modeling frame-work for aggregating heterogeneous preferences. Additionally,[Klingefjordet al., 2024]takes a macro perspective to examinethe gap between human preferences and training objectives,offering solutions from a philosophical standpoint.Data Cost Efficiency.Game theory has also been appliedto enhance the cost efficiency of LLM training.  Collectinga dataset with guaranteed quality and coverage is often chal-lenging, so several works have used the self-play frameworkto improve data utilization, reducing the amount of data re-quired while maintaining performance.[Chenet al., 2024b]addresses the problem of fine-tuning a model with only atiny amount of gold-standard data.  Drawing from Genera-tive Adversarial Networks[Goodfellowet al., 2020], it al-lows the LLM to improve the quality of its answers whilelearning to distinguish between its responses and those ofthe gold-standard answers, ultimately converging to the dis-tribution  of  the  gold-standard  data.[Chenget  al.,  2024a;Zhenget al., 2024]models a game between an attacker and adefender, both of which are LLMs.[Zhenget al., 2024]em-ploys the attacker to propose prompts that the defender is lessskilled at while the defender continuously improves.[Chenget al., 2024a]considers a classic game, Adversarial Taboo,to enhance model knowledge acquisition without introducingnew data, leading to better performance in experiments. Fur-thermore,[Zhang and Duan, 2024]improves the efficiency ofpreference data collection by incorporating an auction modelinto the LLM fine-tuning process, demonstrating how this ap-proach can enhance fine-tuning efficiency while maintainingstrong performance.Other Two-Player Game Formulations.In addition to theliterature discussed above, several studies have formulatedother two-player game models in specific phases of LLMs toenhance particular capabilities.[Chakrabortyet al., 2024a;Makar-Limanovet  al.,  2024;  Chenget  al.,  2024b]modelthe interaction between the reward model and the LLM as atwo-player game. They aim to address the problem where astatic reward model cannot handle the distribution shift of theevolving LLM policy.  Their game-theoretic modeling cap-tures the co-evolution of the reward model and the LLM, andequilibrium-solving algorithms are used to provide theoreti-cally guaranteed LLM training methods.[Jacobet al., 2023]observes that generative and discrim-inative answers to a question by the same LLM are ofteninconsistent. It models the Consensus Game, where these twotypes of answers act as players seeking a consensus answer.Using equilibrium-solving algorithms, this approach signifi-cantly improves the LLM’s accuracy across various datasets.Furthermore,[Gempet al., 2024]models the process of LLMsgenerating long-text conversations as a sequential game, us-ing game-theoretic tools to enhance the model’s ability tounderstand conversations and develop appropriate responses.Remark.Game theory is essential in addressing the chal-lenges in LLM development by offering clear principles foroptimization and well-defined metrics for evaluating models’performance. Through its systematic approach, game theoryhelps refine LLM policies by aligning model behaviors withcomplex human preferences while providing a framework tomeasure and track model effectiveness improvements.  Thismakes game theory a powerful tool for optimizing LLMs, en-suring training processes are both theoretically grounded andpractically applicable.4    Game Theory for LLM-Related ModelingThis  section  provides  an  overview  of  research  on  game-theoretic models that involve LLMs. The theoretical analysisof these models provides evidence of LLMs’ impact on humanProceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10673

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.NLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.NLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SelfPlayPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.DNO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.IiterativeNPO)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhi2024beyond)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fleisig2023majority)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024maxmin)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.park2024rlhf)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alamdari2024policy)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2024pal)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024maxmin)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024maxmin)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.park2024rlhf)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alamdari2024policy)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chen2024pal)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.klingefjord2024human)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.SPIN)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.goodfellow2020generative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024self)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alignmenttwoplayer)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.alignmenttwoplayer)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024self)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024self)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.zhang2024vickreyfeedback)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.chakraborty2024parl)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.STARLHF)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.cheng2024adversarial)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.jacob2023consensus)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.gemp2024states)

society. We categorize the literature into three main areas. Thefirst area explores game-theoretic models that include bothLLMs and humans, aiming to explain or predict the phenom-ena resulting from the development of LLMs.  The secondarea examines scenarios where LLMs function as products orplatforms. This creates competitive environments that exhibitgame-theoretic dynamics like ad auctions. The third area ex-tends classical game theory models, investigating how LLMs’unique capabilities can generalize and refine these models formore complex and realistic settings.4.1    Competitions between LLM and HumanThis body of work introduces several competition models,treating  LLMs  as  players  in  the  game[Yaoet  al.,  2024;Esmaeiliet al., 2024; Taitler and Ben-Porat, 2024].  Thesemodels generally arise from a recognition: modern LLMs pos-sess powerful content generation capabilities and, comparedto human creators, are characterized by lower costs and fasterevolutionary rates.[Yaoet al., 2024]investigates the impact of LLMs on hu-man  creators  by  proposing  a  competition  model  based  onthe Tullock contest.  This model explores the dynamics be-tween human-generated and LLM-generated content, model-ing LLMs as cost-free players whose output quality improvesas human content quality increases. Through equilibrium anal-ysis, the study concludes that LLMs do not fundamentallyconflict with or replace human creators but instead reducethe volume of human-generated content, ultimately pushingout less efficient creators.[Esmaeiliet al., 2024]extends thismodel into a repeated game setting, focusing on how humanscan optimize their utility in dynamic competition with AIacross various content domains. The study highlights the com-putational complexity of determining optimal strategies andproposes practical algorithms that offer near-optimal solutions.[Taitler and Ben-Porat,  2024]examines the competitivedynamics  between  LLM-based  generative  AI  and  human-operated  platforms,  such  as  Stack  Overflow,  and  their  im-plications for social welfare. The study models the revenue-maximization problem of LLMs and uncovers phenomenaakin to Braess’s paradox:  as human users increasingly relyon LLMs, the original platforms suffer from a lack of quality-enhancing data.  Furthermore, generative AI models rarelyundergo training aimed at quality improvement due to cost-saving incentives. The study also suggests theoretical regula-tory frameworks to address these issues.The development of LLMs has led to diverse societal effects,and game theory provides a robust theoretical framework forstudying  these  effects.   By  employing  appropriate  modelsdepicting optimal behaviors and equilibrium strategies, wecan derive properties with theoretical guarantees.4.2    Game Scenarios Emerging with LLMsThis section explores game-theoretic scenarios that arise fromLLMs as products or platforms.  In these scenarios, LLMsdo not participate in the games; instead, they revolve aroundthem.As LLMs gain global attention, industries related to LLMsare creating substantial commercial value.[Lauferet al., 2024]explores the feasibility of fine-tuning general-purpose modelsas a market service.  The study models the bargaining pro-cess between generalists developing the model and domainspecialists adapting it. By analyzing the sub-game perfect equi-libria, the paper demonstrates that a profit-sharing outcome ispossible and offers methods for determining Pareto-optimalequilibria.[Sunet al., 2024a]investigates potential economicscenarios in which a platform offers fine-tuning services forLLMs through an auction-like process for multiple groupswith different preferences. The study proposes an incentive-compatible payment scheme that guarantees social welfaremaximization.[Mahmood, 2024]analyzes the competitive dy-namics of LLM deployment, highlighting the value of marketinformation and demonstrating that a first-to-market strategymay  be  cost-ineffective  for  all  tasks  when  those  tasks  aresufficiently similar.[Saiget al., 2024]proposes a pay-for-preference payment with a contract design model to addressthe potential moral hazard in the current pay-per-token pricingscheme.In addition to their role as commodities, LLMs also offer po-tential commercial value through advertising revenue, similarto search engines.  The emergence of LLMs has made tradi-tional fixed-slot advertisements obsolete, prompting severalstudies on integrating LLMs into advertising auctions[Feiziet al., 2023].[Duettinget al., 2024]models a scenario whereeach advertiser owns an agent LLM and bids to influencethe probability distribution of the next token generated. Thestudy derives an auction mechanism that ensures incentivecompatibility by modifying the second-price auction.[Dubeyet al., 2024]assumes each advertiser provides a fixed adver-tisement copy, influencing LLM summaries through bidding.Their auction mechanism determines the prominence of eachadvertiser in the summary and the price they pay, ensuringincentive  compatibility.[Hajiaghayiet  al.,  2024]also  as-sumes each advertiser possesses a document representing theircontent  but  models  the  advertisement  insertion  process  ina Retrieval-Augmented Generation (RAG) framework.  Themechanism probabilistically retrieves and allocates ads withineach discourse segment of LLM-generated content, optimiz-ing for logarithmic social welfare based on bids and relevance.[Soumaliaset al., 2024]investigates a scenario where each ad-vertiser bids via a reward function for LLM-generated content.Their mechanism incentivizes truthful reporting of rewardfunctions and demonstrates operational viability in a tuning-free setting.4.3    LLM Extending Classic Game ModelsIn addition to these two areas, this section examines worksthat enhance  traditional  game  theory models  using LLMs,extending their applicability to more realistic scenarios.LLMs’  text  comprehension  and  generation  capabilitiesmake them valuable tools for aggregating and eliciting opin-ions.[Luet al., 2024]explores using LLMs to assist peerreview, noting that traditional peer prediction mechanisms arelimited to simple reports, such as multiple-choice or scalarnumbers.  The study proposes peer prediction mechanismsthat  leverage  LLMs’  powerful  text-processing  capabilitiesto incentivize high-quality, truthful feedback. These mecha-nisms are shown to distinguish between human-written andLLM-generated reviews in empirical experiments.[FishetProceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10674

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.yaohuman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.esmaeili2024strategize)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.taitler2024braess)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.yaohuman)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.esmaeili2024strategize)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.taitler2024braess)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.laufer2024fine)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.sun2024mechanism)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.mahmoodpricing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.saig2024incentivizing)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.feizi2023online)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.feizi2023online)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.duetting2024mechanism)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.adSummaries)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.adSummaries)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.adRAG)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.soumalias2024truthful)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.lu2024eliciting)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2023generative)

al., 2024a]uses LLMs to address the limitations of traditionalsocial choice theory, which is constrained to choices among afew predetermined alternatives. The study employs LLMs togenerate text and extrapolate preferences, providing a methodfor designing AI-augmented democratic processes with rigor-ous representation guarantees.[Sunet al., 2024b]investigateshow LLMs can provide richer information in traditional auc-tions.  The study introduces the Semantic-enhanced Person-alized Valuation in the Auction framework, which leveragesLLMs to incorporate bidders’ preferences and semantic iteminformation into the valuation process. The framework inte-grates fine-tuned LLMs with the Vickrey auction mechanismto improve valuation accuracy and bidding strategies.5    Conclusion and Future DirectionsThis survey provides a comprehensive overview of the re-search progress at the intersection of LLMs and game theory.We summarized the role that game theory has been playingin developing LLMs from three key perspectives: providingstandardized game-based evaluation, driving game-theoreticalgorithmic innovations, and modeling the societal impact ofLLMs. Furthermore, we highlighted the bidirectional relation-ship between LLMs and game theory, exploring how LLMsinfluence traditional game models.  Building on this review,we have identified several promising future directions.LLM-based Agents with Comprehensive Game Abilities.Existing research has explored the evaluation of LLM agentsacross various game scenarios and developed methods to en-hance their reasoning capabilities.  However, while some ofthese methods demonstrate general applicability, their valida-tion remains highly scenario-specific. A key future direction isto develop LLM agents proficient in game-theoretic reasoning,capable of applying their knowledge across diverse game set-tings without explicit customization. Achieving this requiresadvancements in rule comprehension, external environmentmodeling, and multi-agent reasoning. Key technical aspectsinclude constructing a game-theoretic corpus, refining fine-tuning strategies, and incorporating tool-learning techniques.Moving Beyond Human-Oriented Evaluation Frameworks.Game theory provides well-established evaluation criteria forrationality and strategic reasoning, such as K-level rationality,which has been widely adopted to assess LLM intelligence.However, these evaluation methods were originally designedfor human cognition and may not fully capture the reasoningprocesses of next-token prediction models. To assess LLMscomprehensively from a game-theoretic perspective, it is cru-cial to move beyond existing human-oriented metrics and de-velop evaluation frameworks tailored to neural network-basedmodels. This remains an underexplored area with the poten-tial to improve our understanding of LLMs’ decision-makingsignificantly.Theoretical Understanding of LLMs’ Strategic Behavior.The application of game-theoretic concepts, such as the Shap-ley Value, to understanding LLMs’ text generation behavioris still in its early stages. Most studies on LLMs’ strategic be-havior in real-world scenarios rely on empirical observationsrather than systematic theoretical interpretations. For example,[Parket al., 2025]has introduced hypothetical models to ex-plain why LLMs struggle to achieve the performance level ofno-regret learners in repeated games. Extending such theoreti-cal investigations to more complex scenarios, including gameslike Werewolf, Avalon, or bargaining games, is essential. Adeeper theoretical understanding of LLM strategic behaviorwill help to define their capability boundaries and provideinsights for further improving their reasoning abilities.Capturing  Cooperative  Games  in  LLM  Optimization.Many studies leveraging game theory for optimizing LLMtraining, as discussed in Section 3.2, primarily focus on non-cooperative game settings. While non-cooperative approachesare a natural fit,  cooperative game-theoretic methods offeradditional insights into LLM optimization. For instance, dif-ferent expert networks can be seen as participants in a coopera-tive game in the Mixture of Expert models. Adopting suitablepayoff allocation mechanisms, such as the Shapley Value orthe core concept, could optimize expert selection and task al-location, reducing redundancy while enhancing computationalefficiency.  Similarly, in ensemble learning and knowledgedistillation, different sub-models can be treated as coopera-tive agents working together to refine decision boundaries ortransfer knowledge.  Effective reward allocation and weightadjustment strategies could enhance collaboration among sub-models, reducing redundant computation while improving gen-eralization. Integrating cooperative game-theoretic methodsinto LLM training and optimization could offer new theoreticalinsights and practical solutions.Modeling Cooperation Between Multi-LLMs and Humans.As discussed in Section 4.1, previous studies have primarilybeen focused on modeling competitive interactions betweenLLMs and humans, yielding valuable insights into their so-cietal  implications.   However,  beyond  competition,  under-standing cooperative dynamics between multiple LLMs andhumans remains an important research direction.  One keychallenge is to design mechanisms that incentivize LLMs tocollaborate in fulfilling human-assigned tasks while consid-ering their objectives. A theoretical characterization of LLMagents’ goals and behaviors is essential for bridging the gapbetween game-theoretic mechanism design and real-world de-ployment. Advancing this line of research could facilitate thedevelopment of LLMs that align more effectively with humanobjectives and contribute positively to society.Leveraging LLMs as Oracles to Extend Theoretical GameModels.As discussed in Section 4.3, several studies haveexplored how LLMs can be used to extend classical game-theoretic models. The key insight behind these works is thatLLMs, with their strong language understanding and genera-tive capabilities, can serve as oracles with specific functionali-ties in game-theoretic frameworks. This perspective opens upnew opportunities to relax idealized assumptions or replacetheoretical oracles in various game models using LLMs. Bydoing so, models that previously remained purely theoreticalcan now be practically implemented while preserving approx-imate theoretical properties.  Systematic exploration of howLLMs can function as adaptable oracles in different theoreticalmodels could bridge the gap between abstract game-theoreticconcepts and real-world applications.Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10675

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.fish2023generative)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.sun2024large)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#cite.park2024llm)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.3.2)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.4.1)

[](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/DELL%203450/.antigravity/extensions/cweijan.vscode-office-3.5.4-universal/resource/pdf/#subsection.4.3)

AcknowledgmentsSupported  by  the  National  Natural  Science  Foundation  ofChina (Grant No. 62172012, No. 12471339).References[Akataet al., 2023]Elif Akata, Lion Schulz, et al. Playing repeatedgames with large language models.arXiv preprint, 2023.[Alamdariet al., 2024]Parand A Alamdari, Soroush Ebadian, andAriel D Procaccia. Policy aggregation.arXiv preprint, 2024.[Chakrabortyet al., 2024a]Souradip Chakraborty, Amrit Bedi, et al.Parl: A unified framework for policy alignment in reinforcementlearning from human feedback. InICLR, 2024.[Chakrabortyet al., 2024b]Souradip Chakraborty, Jiahao Qiu, et al.Maxmin-rlhf:  Towards  equitable  alignment  of  large  languagemodels with diverse human preferences. InICML, 2024.[Chenet al., 2023]Jiangjie Chen, Siyu Yuan, et al. Put your moneywhere your mouth is: Evaluating strategic planning and executionof llm agents in an auction arena.arXiv preprint, 2023.[Chenet al., 2024a]Daiwei  Chen,  Yi  Chen,  Aniket  Rege,  andRamya Korlakai Vinayak. Pal: Pluralistic alignment frameworkfor learning from heterogeneous preferences.arXiv preprint, 2024.[Chenet al., 2024b]Zixiang Chen, Yihe Deng, et al. Self-play fine-tuning converts weak language models to strong language models.InICML, 2024.[Chenet al., 2025]Sijin Chen, Omar Hagrass, and Jason M Klu-sowski. Decoding game: On minimax optimality of heuristic textgeneration strategies. InICLR, 2025.[Chenget al., 2024a]Pengyu Cheng, Tianhao Hu, et al. Self-playingadversarial language game enhances llm reasoning. InNeurIPS,2024.[Chenget al., 2024b]Pengyu Cheng, Yifan Yang, et al. Adversarialpreference optimization: Enhancing your alignment via rm-llmgame. InACL 2024 Findings, 2024.[Conitzeret al., 2024]Vincent  Conitzer,  Rachel  Freedman,  et  al.Position: Social choice should guide ai alignment in dealing withdiverse human feedback. InICML, 2024.[Denget al., 2024]Yuan Deng, Vahab Mirrokni, et al. Llms at thebargaining table. InICML Workshop, volume 2024, 2024.[Denget al., 2025]Shilong Deng, Yongzhao Wang, and Rahul Sa-vani. From natural language to extensive-form game representa-tions.arXiv preprint, 2025.[Du and Zhang, 2024]Silin Du and Xiaowei Zhang. Helmsman ofthe masses?  evaluate the opinion leadership of large languagemodels in the werewolf game.arXiv preprint, 2024.[Duanet al., 2024a]Jinhao Duan, Shiqi Wang, et al.  Reta: Recur-sively thinking ahead to improve the strategic reasoning of largelanguage models. InNAACL, 2024.[Duanet al., 2024b]Jinhao Duan, Renming Zhang, et al. Gtbench:Uncovering the strategic reasoning limitations of llms via game-theoretic evaluations. InNeurIPS, 2024.[Dubeyet al., 2024]Avinava Dubey, Zhe Feng, et al. Auctions withllm summaries. InKDD, 2024.[Duettinget al., 2024]Paul Duetting, Vahab Mirrokni, et al. Mech-anism design for large language models. InWWW, 2024.[Enouenet al., 2024]James   Enouen,   Hootan   Nakhost,   et   al.Textgenshap: Scalable post-hoc explanations in text generationwith long documents. InACL Findings, 2024.[Esmaeiliet al., 2024]Seyed A Esmaeili, Kshipra Bhawalkar, et al.How to strategize human content creation in the era of genai?arXiv preprint, 2024.[Fanet al., 2024]Caoyun Fan, Jindou Chen, Yaohui Jin, and HaoHe. Can large language models serve as rational players in gametheory? a systematic analysis. InAAAI, 2024.[Feiziet al., 2023]Soheil   Feizi,   MohammadTaghi   Hajiaghayi,Keivan Rezaei, and Suho Shin. Online advertisements with llms:Opportunities and challenges.arXiv preprint, 2023.[Fenget al., 2024]Xiachong Feng, Longxu Dou, et al.  A surveyon large language model-based social agents in game-theoreticscenarios.arXiv preprint, 2024.[Fishet al., 2024a]Sara Fish, Paul G ̈olz, et al.  Generative socialchoice. InEC, 2024.[Fishet al., 2024b]Sara Fish, Yannai A Gonczarowski, and Ran IShorrer. Algorithmic collusion by large language models.arXivpreprint, 2024.[Fleisiget al., 2023]Eve  Fleisig,  Rediet  Abebe,  and  Dan  Klein.When the majority is wrong: Modeling annotator disagreementfor subjective tasks. InEMNLP, 2023.[Gandhiet al., 2023]Kanishk Gandhi, Dorsa Sadigh, and Noah DGoodman. Strategic reasoning with language models. InNeurIPS,2023.[Geet al., 2024]Luise Ge, Daniel Halpern, et al.   Axioms for aialignment from human feedback. InNeurIPS, 2024.[Gempet al., 2024]Ian  Gemp,  Yoram  Bachrach,  et  al.Statesas strings as strategies:  Steering language models with game-theoretic solvers.arXiv preprint, 2024.[Goldshmidt and Horovicz, 2024]Roni  Goldshmidt  and  MiriamHorovicz.Tokenshap:   Interpreting  large  language  modelswith monte carlo shapley value estimation.  InACL WorkshopNLP4Science, 2024.[Goodfellowet al., 2020]Ian  Goodfellow,   Jean  Pouget-Abadie,et al.  Generative adversarial networks.Communications of theACM, 2020.[Guoet al., 2024]Shangmin Guo,  Haoran Bu,  et al.   Economicsarena for large language models.arXiv preprint, 2024.[Hajiaghayiet al., 2024]MohammadTaghi  Hajiaghayi,  S ́ebastienLahaie, et al. Ad auctions for llms via retrieval augmented genera-tion. InNeurIPS, 2024.[Herret al., 2024]Nathan Herr, Fernando Acero, et al. Are large lan-guage models strategic decision makers? a study of performanceand bias in two-player non-zero-sum games.arXiv preprint, 2024.[Horton, 2023]John J Horton. Large language models as simulatedeconomic agents: What can we learn from homo silicus?  Techni-cal report, National Bureau of Economic Research, 2023.[Huet al., 2024]Sihao Hu, Tiansheng Huang, et al.  A survey onlarge language model-based game agents.arXiv preprint, 2024.[Huaet al., 2024]Wenyue Hua, Ollie Liu, et al. Game-theoretic llm:Agent workflow for negotiation games.arXiv preprint, 2024.[Huanget al., 2024]Jen-tse Huang, Eric John Li, et al.   How farare we on the decision-making of llms? evaluating llms’ gamingability in multi-agent environments.arXiv preprint, 2024.[Jacobet al., 2023]Athul Paul Jacob, Yikang Shen, et al. The con-sensus game: Language model generation via equilibrium search.InICLR, 2023.Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10676

[Klingefjordet al., 2024]Oliver Klingefjord, Ryan Lowe, and JoeEdelman.  What are human values, and how do we align ai tothem?arXiv preprint, 2024.[Lanet al., 2024]Yihuai Lan, Zhiqiang Hu, et al. Llm-based agentsociety investigation: Collaboration and confrontation in avalongameplay. InEMNLP, 2024.[Lauferet al., 2024]Benjamin Laufer, Jon Kleinberg, and Hoda Hei-dari. Fine-tuning games: Bargaining and adaptation for general-purpose models. InWWW, 2024.[Liuet al., 2023]Hanxi Liu, Xiaokai Mao, et al. Prompt valuationbased on shapley values.arXiv preprint, 2023.[Lor `e and Heydari, 2024]Nunzio Lor`e and Babak Heydari. Strate-gic behavior of large language models and the role of game struc-ture versus contextual framing.Scientific Reports, 2024.[Luet al., 2024]Yuxuan Lu, Shengwei Xu, et al. Eliciting informa-tive text evaluations with large language models. InEC, 2024.[Mahmood, 2024]Rafid Mahmood.   Pricing and competition forgenerative ai. InNeurIPS, 2024.[Makar-Limanovet al., 2024]JacobMakar-Limanov,ArjunPrakash,  et  al.Sta-rlhf:   Stackelberg  aligned  reinforcementlearning with human feedback. InCoCoMARL, 2024.[Mensfeltet al., 2024]Agnieszka  Mensfelt,  Kostas  Stathis,  andVince Trencsenyi. Autoformalizing and simulating game-theoreticscenarios using llm-augmented agents.arXiv preprint, 2024.[Mishra, 2023]Abhilash Mishra.  Ai alignment and social choice:Fundamental limitations and policy implications.arXiv preprint,2023.[Mohammadi, 2024]Behnam  Mohammadi.    Wait,  it’s  all  tokennoise?  always has been:  interpreting llm behavior using shap-ley value.Available at SSRN 4759713, 2024.[Munoset al., 2024]Remi Munos, Michal Valko, et al. Nash learn-ing from human feedback. InICML, 2024.[Nash Jr, 1950]John  F Nash  Jr.   Equilibrium points  in n-persongames.Proceedings of the national academy of sciences, 1950.[Parket al., 2024]Chanwoo Park, Mingyang Liu, et al. Rlhf fromheterogeneous feedback via personalization and preference aggre-gation. InICML Workshop, 2024.[Parket al., 2025]Chanwoo Park, Xiangyu Liu, et al. Do llm agentshave regret? a case study in online learning and games. InICLR,2025.[Qiu, 2024]Tianyi Qiu. Representative social choice: From learningtheory to ai alignment.NeurIPS 2024 Workshop, 2024.[Rossetet al., 2024]Corby Rosset, Ching-An Cheng, et al. Directnash optimization:  Teaching language models to self-improvewith general preferences.arXiv preprint, 2024.[Saiget al., 2024]Eden Saig, Ohad Einav, and Inbal Talgam-Cohen.Incentivizing quality text generation via statistical contracts.  InNeurIPS, 2024.[Shapiraet al., 2024]Eilam Shapira, Omer Madmon, et al. Glee: Aunified framework and benchmark for language-based economicenvironments.arXiv preprint, 2024.[Shapley, 1953]Lloyd S Shapley. A value for n-person games.Con-tribution to the Theory of Games, 2, 1953.[Soumaliaset al., 2024]Ermis  Soumalias,  Michael  J  Curry,  andSven Seuken. Truthful aggregation of llms with an application toonline advertising.arXiv preprint, 2024.[Sunet al., 2024a]Haoran Sun, Yurong Chen, et al.   Mechanismdesign for llm fine-tuning with multiple reward models.NeurIPS2024 Workshop, 2024.[Sunet al., 2024b]Jie Sun, Tianyu Zhang, et al.  Large languagemodels empower personalized valuation in auction.arXiv preprint,2024.[Swamyet al., 2024]Gokul Swamy, Christoph Dann, et al. A mini-maximalist approach to reinforcement learning from human feed-back. InICML, 2024.[Taitler and Ben-Porat, 2024]Boaz  Taitler  and  Omer  Ben-Porat.Braess’s paradox of generative ai.arXiv preprint, 2024.[Vickrey, 1961]William Vickrey. Counterspeculation, auctions, andcompetitive sealed tenders.The Journal of finance, 1961.[Von Neumann and Morgenstern, 2007]John  Von  Neumann  andOskar Morgenstern.  Theory of games and economic behavior:60th anniversary commemorative edition. InTheory of games andeconomic behavior. Princeton university press, 2007.[Wanget al., 2023]Shenzhi Wang, Chang Liu, et al. Avalon’s gameof thoughts: Battle against deception through recursive contem-plation.arXiv preprint, 2023.[Wanget al., 2024]Haochuan Wang, Xiachong Feng, et al.  Tmg-bench:  A systematic game benchmark for evaluating strategicreasoning abilities of llms.arXiv preprint, 2024.[Wuet al., 2025]Yue Wu, Zhiqing Sun, et al. Self-play preferenceoptimization for language model alignment. InICLR, 2025.[Xiaet al., 2024]Tian Xia, Zhiwei He, et al. Measuring bargainingabilities of llms: A benchmark and a buyer-enhancement method.InACL Findings, 2024.[Xuet al., 2023]Yuzhuang Xu, Shuo Wang, et al. Exploring largelanguage models for communication games: An empirical studyon werewolf.arXiv preprint, 2023.[Yaoet al., 2024]Fan Yao, Chuanhao Li, et al. Human vs. genera-tive ai in content creation competition: Symbiosis or conflict?  InICML, 2024.[Zhang and Duan, 2024]Guoxi  Zhang  and  Jiuding  Duan.   Vick-reyfeedback: Cost-efficient data construction for reinforcementlearning from human feedback. InPRIMA. Springer, 2024.[Zhanget al., 2024a]Yadong Zhang, Shaoguang Mao, et al. K-levelreasoning with large language models.arXiv preprint, 2024.[Zhanget al., 2024b]Yadong Zhang, Shaoguang Mao, et al. Llm asa mastermind: A survey of strategic reasoning with large languagemodels. InCOLM, 2024.[Zhanget al., 2024c]Yang   Zhang,    Yanfei   Dong,    and   KenjiKawaguchi.   Investigating layer importance in large languagemodels. InACL Workshop BlackboxNLP, 2024.[Zhanget al., 2024d]Yuheng Zhang, Dian Yu, et al. Iterative nashpolicy optimization: Aligning llms with general preferences viano-regret learning.arXiv preprint, 2024.[Zhanget al., 2024e]Zhaowei Zhang, Fengshuo Bai, et al. Incentivecompatibility for ai alignment in sociotechnical systems: Positionsand prospects.arXiv preprint, 2024.[Zhenget al., 2024]Rui Zheng, Hongyi Guo, et al. Toward optimalllm alignments using two-player games.arXiv preprint, 2024.[Zhi-Xuanet al., 2024]Tan   Zhi-Xuan,   Micah   Carroll,   MatijaFranklin, and Hal Ashton.  Beyond preferences in ai alignment.Philosophical Studies, 2024.Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25)Survey Track10677
