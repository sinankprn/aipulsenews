---
title: "Google Gemini Deep Think Goes Beyond Math: Solving Real Research Problems in Physics, CS and Engineering"
author: Sinan Koparan
date: "2026-02-13 09:00:00"
layout: post
description: Google's Gemini Deep Think mode has evolved from solving math olympiad problems to tackling real research challenges across mathematics, physics, and computer science, producing publishable results and settling decade-old conjectures.
sources:
  - https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/
tags:
  - Google
  - Gemini
  - Deep Think
  - AI Research
  - Reasoning
image: "/assets/images/posts/google-deepthink.jpg"
---

In the summer of 2025, an advanced version of Gemini Deep Think achieved Gold-medal standard at the International Mathematics Olympiad (IMO) and later, an updated version, obtained similar results at the International Collegiate Programming Contest. These results demonstrated the model could reason through some of the most challenging math and programming problems designed for students. Since then, Gemini Deep Think mode has moved into science, engineering and enterprise workflows to tackle more complex, open-ended challenges.

In the last week, our teams published two papers (1, 2) detailing a cross-disciplinary effort to solve professional research problems using Gemini Deep Think mode. These results stem from deep collaboration between mathematicians, physicists, and computer scientists.

The Frontier of Pure Mathematics
Unlike IMO problems, research-level mathematics requires advanced techniques from vast literature. While foundation models have large knowledge bases, data scarcity often leads to superficial understanding and hallucinations in advanced subjects.

To solve this, we built a math research agent (internally codenamed Aletheia), powered by Gemini Deep Think mode. It features a natural language verifier to identify flaws in candidate solutions and enable an iterative process of generating and revising solutions. Crucially, this agent can admit failure to solve a problem, a key feature that improved the efficiency for researchers.

Additionally, the research agent uses Google Search and web browsing to navigate complex research, preventing spurious citations and computational inaccuracies when synthesizing published literature.

Flowchart titled "Aletheia: Powered by Gemini Deep Think" illustrating a multi-step solution verification process. A central linear path moves from "Problem" to "Generator," then "Candidate solution," then "Verifier," and finally "Final output." The Verifier acts as a decision point with three feedback loops: Correct: Moves directly to "Final output." Minor fixes needed: Routes back through a "Reviser" to update the "Candidate solution." Critically flawed: Triggers a red dashed line back to the "Generator" to restart the process.
Overview of Aletheia, a math research agent powered by Deep Think that can iteratively generate, verify, and revise for research-level math problems.

Since achieving IMO Gold-medal standard in July 2025, Gemini Deep Think has progressed rapidly, scoring up to 90% on the IMO-ProofBench Advanced test as inference-time compute scales. We demonstrated that the scaling law continues to hold as we progress beyond Olympiad level into PhD-level exercises (per our internal FutureMath Basic benchmark). Notably, Aletheia demonstrated that higher reasoning quality can be achieved at a lower inference-time compute.

Line graph titled "IMO-ProofBench Advanced (Olympiad level)" comparing the performance of two versions of Gemini Deep Think against a benchmark named Aletheia. The y-axis shows Score percentage (30% to 90%), and the x-axis shows Inference-Time Compute on a logarithmic scale .The January 2026 version (light blue) consistently outperforms the July 2025 version (dark blue), with both showing a steady upward trend as compute increases. The January 2026 version peaks at approximately 90% nearly reaching the Aletheia benchmark (green star) positioned just above 90%.
The latest advanced version of Deep Think, as of Jan 2026, has significantly outperformed the IMO-Gold version (Jul 2025) on Olympiad-level problems. Aletheia makes further leaps in terms of reasoning quality with lower inference-time compute. All results were graded by human experts.

Line graph titled "(b) FutureMath Basic (Ph.D level exercises)" plotting the score of Gemini Deep Think (Jan 2026) against increasing Inference-Time Compute on a logarithmic scale. The y-axis represents Score percentage (0% to 45%). The performance starts at 0% and shows a volatile upward trend, hitting an early peak of 30% before fluctuating and eventually climbing to a final high of approximately 38%. A green star representing "Aletheia" is marked as a benchmark at roughly 46%, remaining significantly above the model's highest performance reached.
The inference-time scaling law also transfers to PhD-level exercises.

For research-level math, Aletheia has already enabled several advancements, produced via varying levels of autonomous research:

Reliable autonomous research. A research paper (Feng26) generated by AI without any human intervention, which calculates certain structure constants in arithmetic geometry called eigenweights.
AI-guided collaboration. A research paper (LeeSeo26) demonstrating human-AI collaboration in proving bounds on systems of interacting particles called independent sets.
An extensive semi-autonomous evaluation (Feng et al., 2026b) of 700 open problems on Bloom’s Erdős Conjectures database, including autonomous solutions to four open questions listed there. On Erdős-1051, our model autonomously solved and helped lead to a generalization reported in a research paper (BKKKZ26).
The agent also contributed intermediate propositions on two further papers, (FYZ26) and (ACGKMP26). It is also of note that there has been prior work using Gemini for research-level math at a smaller scale in terms of collaborations and the number of problems tackled.

Following extensive discussions with the mathematical community, we suggest a taxonomy to classify AI-assisted mathematics research by significance and degree of AI contribution - contributing to the wider discussion on responsible documentation, evaluation and communication of AI-generated results. Level 2 (“publishable quality”) works have been submitted to reputable journals. Currently, we do not claim any Level 3 (“Major Advance”) and Level 4 (“Landmark Breakthrough”) results.

A table titled "Classification of all AI-assisted mathematics results encompassed in this work" categorizes research by novelty and collaboration type.Level 0 (Autonomous): Erdős-652, 654, 1040 (Feng et al., 2026b).Level 1 (Autonomous): Erdős-1051 (Feng et al., 2026b).Level 2 (Human + AI): Complexity Bounds (ACGKMP26) and Arithmetic Volumes (FYZ26).Level 2 (Collaboration): Independence Polynomials (LeeSeo26) and Generalized Erdős-1051 (BKKKZ26).Level 2 (Autonomous): Eigenweights (Feng26).Levels 3 and 4 are currently empty.
Classification of all AI-assisted mathematics results encompassed in this work. \*Works listed as Level 2 in this table have been submitted for publications.

Prompts and model outputs are available here. For discussions on AI contributions, our “Human-AI Interaction card”, and community impact, see our paper.

Expanding to Physics and Computer Science
Gemini Deep Think mode has also demonstrated promise in computer science and physics. The second paper builds on similar agentic reasoning ideas, and identifies effective "recipes" for collaboration, specifically the "Advisor" model, where humans guide AI through iterative "Vibe-Proving" cycles to validate intuition and refine proofs. We also detail tactical techniques like “balanced prompting” —requesting simultaneous proof or refutation to prevent confirmation bias—and code-assisted verification. These methods, combined with the model's ability to bridge disparate scientific fields through deep structural connections, are transforming how theoretical research is conducted. This work builds upon our successful deployment of an advanced version of Gemini Deep Think to assist in reviewing CS theory papers for STOC’26 conference.

A flow diagram titled "Network layer" illustrating a process for deep reasoning. At the top, a bracket labeled "Extensive exploration of solution space" funnels into a filter icon. This leads into a central "Deep reasoning" section represented by a series of interconnected nodes and wave patterns. The process concludes with a human icon pointing to "Output." A final label at the bottom describes the process as a "Long tail of automated + human verification."
A schematic overview of the AI reasoning pipeline, illustrating how extensive solution space exploration at the network layer is funneled into structured reasoning and validated by automated and human verification.

Collaborating with experts on 18 research problems, an advanced version of Gemini Deep Think helped resolve long-standing bottlenecks across algorithms, ML and combinatorial optimization, information theory, and economics. Highlights from our “Accelerating Research with Gemini” paper include (corresponding section numbers in paper):

Crossing mathematical borders for network puzzles: Progress on classic computer science problems like "Max-Cut" (efficiently splitting networks) and the "Steiner Tree" (connecting high-dimensional points) had slowed down. Gemini broke both deadlocks by thinking outside the box. It solved these discrete algorithmic puzzles by pulling advanced tools—like the Kirszbraun Theorem, measure theory, and the Stone-Weierstrass theorem—from entirely unrelated branches of continuous mathematics. See Sections 4.1 and 4.2.
Settling a decade-old conjecture in online submodular optimization: A 2015 theory paper proposed a seemingly obvious rule for data streams: making a copy of an arriving item is always less valuable than simply moving the original. Experts struggled for a decade to prove this. Gemini engineered a highly specific three-item combinatorial counterexample, rigorously proving the long-standing human intuition false. See Section 3.1.
Machine learning optimization: Training AI to filter out noise usually requires engineers to manually tune a mathematical "penalty." Researchers created a new technique that did this automatically, but couldn't mathematically explain why. Gemini analyzed the equations and proved the method succeeds by secretly generating its own "adaptive penalty" on the fly. See Section 8.3.
Upgrading economic theory for AI: A recent 'Revelation Principle' for auctioning AI generation tokens only worked mathematically when bids were restricted to rational numbers. Extending the domain to continuous real numbers invalidated the original proof. Gemini employed advanced topology and order theory to extend the theorem, accommodating real-world, continuous auction dynamics. See Section 8.4.
Physics of cosmic strings: Calculating gravitational radiation from cosmic strings requires finding analytical solutions to tricky integrals containing "singularities." Gemini found a novel solution using Gegenbauer polynomials. This naturally absorbed the singularities, collapsing an infinite series into a closed form, finite sum. See Section 6.1.
Spanning diverse fields—from information and complexity theory to cryptography and mechanism design—the results demonstrate how AI is fundamentally shifting research. For details, see our paper.

Given computer science's fluid, conference-driven publication pipeline, we describe these results by academic trajectory rather than a rigid taxonomy. About half target strong conferences—including an ICLR ’26 acceptance—while most remaining findings will form future journal submissions. Even when course-correcting the field by identifying errors (Section 3.2) or refuting conjectures (Section 3.1), these outcomes highlight AI’s value as a high-level scientific collaborator.

The Future of Human-AI Collaboration
Building on Google’s previous breakthroughs (1, 2, 3, 4, 5), this work demonstrates that general foundation models - leveraged with agentic reasoning workflows - can act as a powerful scientific companion.

Under direction from expert mathematicians, physicists, and computer scientists, Gemini Deep Think mode is proving its utility across fields where complex math, logic and reasoning are core.

We are witnessing a fundamental shift in the scientific workflow. As Gemini evolves, it acts as "force multiplier" for human intellect, handling knowledge retrieval and rigorous verification so scientists can focus on conceptual depth and creative direction. Whether refining proofs, hunting for counterexamples, or linking disconnected fields, AI is becoming a valuable collaborator in the next chapter of scientific progress.

Acknowledgements
We thank the community of expert mathematicians, physicists, and computer scientists for their help and advice on this project

This project was a large-scale collaboration across Google and its success is due to the combined efforts of many individuals and teams. Thang Luong and Vahab Mirrokni led the overall research directions with deep technical expertises from Tony Feng and David Woodruff.

Authors of the first paper “Towards Autonomous Mathematics Research” include: Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk Jung, Joonkyung Lee, Carlo Pagano, Sang-hyun Kim, Federico Pasqualotto, Sergei Gukov, Jonathan N. Lee, Junsu Kim, Kaiying Hou, Golnaz Ghiasi, Yi Tay, YaGuang Li, Chenkai Kuang, Yuan Liu, Hanzhao (Maggie) Lin, Evan Zheran Liu, Nigamaa Nayakanti, Xiaomeng Yang, Heng-Tze Cheng, Demis Hassabis, Koray Kavukcuoglu, Quoc V. Le, Thang Luong. We thank the following experts for feedback and discussions on the work: ​​Jarod Alper, Kevin Barreto, Thomas Bloom, Sourav Chatterjee, Otis Chodosh, Michael Hutchings, Seongbin Jeon, Youngbeom Jin, Aiden Yuchan Jung, Jiwon Kang, Jimin Kim, Vjekoslav Kovač, Daniel Litt, Ciprian Manolescu, Mona Merling, Agustin Moreno, Carl Schildkraut, Johannes Schmitt, Insuk Seo, Jaehyeon Seo, Terence Tao, Cheng-Chiang Tsai, Ravi Vakil, Zhiwei Yun, Shengtong Zhang, Wei Zhang, Yufei Zhao.

Authors of the second paper “Accelerating Scientific Research with Gemini: Case Studies and Common Techniques” include David P. Woodruff, Vincent Cohen-Addad, Lalit Jain, Jieming Mao, Song Zuo, MohammadHossein Bateni, Simina Branzei, Michael P. Brenner, Lin Chen, Ying Feng, Lance Fortnow, Gang Fu, Ziyi Guan, Zahra Hadizadeh, Mohammad T. Hajiaghayi, Mahdi JafariRaviz, Adel Javanmard, Karthik C. S., Ken-ichi Kawarabayashi, Ravi Kumar, Silvio Lattanzi, Euiwoong Lee, Yi Li, Ioannis Panageas, Dimitris Paparas, Benjamin Przybocki, Bernardo Subercaseaux, Ola Svensson, Shayan Taherijam, Xuan Wu, Eylon Yogev, Morteza Zadimoghaddam, Samson Zhou, Yossi Matias, Jeff Dean, James Manyika, Vahab Mirrokni. This list includes Google researchers building the agentic reasoning on top of Gemini, and our academic expert collaborators verifying and collaborating with Gemini. We also thank Corinna Cortes for her careful review of the paper.

We are grateful for the foundational support from the rest of the DeepThink team: Anirudh Baddepudi, Michael Brenner, Irene Cai, Kristen Chiafullo, Paul Covington, Rumen Dangovski, Chenjie Gu, Huan Gui, Vihan Jain, Rajesh Jayaram, Melvin Johnson, Rosemary Ke, Maciej Kula, Nate Kushman, Jane Labanowski, Steve Li, Pol Moreno, Sidharth Mudgal, William Nelson, ​​Ada Maksutaj Oflazer, Sahitya Potluri, Navneet Potti, Shubha Raghvendra, Siamak Shakeri, Archit Sharma, Xinying Song, Mukund Sundararajan, Qijun Tan, Zak Tsai, Theophane Weber, Winnie Xu, Zicheng Xu, Junwen Yao, Shunyu Yao, Adams Yu, Lijun Yu, and Honglei Zhuang.

We thank Quoc Le, Koray Kavukcuoglu, Demis Hassabis, James Manyika, Yossi Matias, and Jeff Dean for sponsoring this project.

Last but not least, we thank Divy Thakkar, Adam Brown, Vinay Ramasesh, Alex Davies, Thomas Hubert, Eugénie Rives, Pushmeet Kohli, Benoit Schillings for feedback and support of the project

Today, we’re releasing a major upgrade to Gemini 3 Deep Think, our specialized reasoning mode, built to push the frontier of intelligence and solve modern challenges across science, research, and engineering.

We updated Gemini 3 Deep Think in close partnership with scientists and researchers to tackle tough research challenges — where problems often lack clear guardrails or a single correct solution and data is often messy or incomplete. By blending deep scientific knowledge with everyday engineering utility, Deep Think moves beyond abstract theory to drive practical applications.

The new Deep Think is now available in the Gemini app for Google AI Ultra subscribers and, for the first time, we’re also making Deep Think available via the Gemini API to select researchers, engineers and enterprises. Express interest in early access here.

Here is how our early testers are already using the latest Deep Think:

Lisa Carbone, a mathematician at Rutgers University, works on the mathematical structures required by the high-energy physics community to bridge the gap between Einstein’s theory of gravity and quantum mechanics. In a field with very little existing training data, she used Deep Think to review a highly technical mathematics paper. Deep Think successfully identified a subtle logical flaw that had previously passed through human peer review unnoticed.

Jump to position 1
Jump to position 2
Jump to position 3
Elevating reasoning with mathematical and algorithmic rigor
Last year, we showed that specialized versions of Deep Think could successfully navigate some of the toughest challenges in reasoning, achieving gold-medal standards at math and programming world championships. More recently, Deep Think has enabled specialized agents to conduct research-level mathematics exploration.

The updated Deep Think mode continues to push the frontiers of intelligence, reaching new heights across the most rigorous academic benchmarks, including:

Setting a new standard (48.4%, without tools) on Humanity’s Last Exam, a benchmark designed to test the limits of modern frontier models
Achieving an unprecedented 84.6% on ARC-AGI-2, verified by the ARC Prize Foundation
Attaining a staggering Elo of 3455 on Codeforces, a benchmark consisting of competitive programming challenges
Reaching gold-medal level performance on the International Math Olympiad 2025
Gemini 3 Deep Think evaluations charts
Navigating complex scientific domains
Beyond mathematics and competitive coding, Gemini 3 Deep Think now also excels across broad scientific domains such as chemistry and physics. Our updated Deep Think mode demonstrates gold medal-level results on the written sections of the 2025 International Physics Olympiad and Chemistry Olympiad. It also demonstrates proficiency in advanced theoretical physics, achieving a score of 50.5% on CMT-Benchmark.

Gemini 3 Deep Think evaluation table
Accelerating real-world engineering
In addition to its state-of-the-art performance, Deep Think is built to drive practical applications, enabling researchers to interpret complex data, and engineers to model physical systems through code. Most importantly, we are working to bring Deep Think to researchers and practitioners where they need it most — beginning with surfaces such as the Gemini API.

With the updated Deep Think, you can turn a sketch into a 3D-printable reality. Deep Think analyzes the drawing, models the complex shape and generates a file to create the physical object with 3D printing.

Available to Google AI Ultra Subscribers and the Gemini API via our Early Access Program
Google AI Ultra subscribers will be able to access the updated Deep Think mode starting today in the Gemini app. Scientists, engineers and enterprises can also now express interest in our early access program to test Deep Think via the Gemini API.

We can’t wait to see what you discover.
