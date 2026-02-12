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
image: "/assets/images/posts/gemini3deepthink.jpeg"
---

In the summer of 2025, Google's Gemini Deep Think achieved gold-medal standard at the International Mathematics Olympiad. A few months later, an updated version matched that performance at the International Collegiate Programming Contest. Those were impressive results, but they still fell within the domain of well-defined competition problems with clear answers. Now, Google is pushing Deep Think into far messier territory: open-ended research problems in mathematics, physics, computer science, and economics, where no answer key exists.

This week, Google DeepMind published two research papers and rolled out a major upgrade to Gemini 3 Deep Think, marking a significant expansion of the model's capabilities. The results suggest that AI reasoning systems are crossing a threshold, moving from solving textbook-style challenges to producing genuinely novel scientific contributions.

### Aletheia: A Math Research Agent

The centerpiece of the first paper is Aletheia, a math research agent powered by Gemini Deep Think mode. Unlike a standard language model that generates a single response, Aletheia operates through an iterative loop of generating candidate solutions, verifying them with a natural language checker, and revising flawed attempts. Critically, the agent can also admit failure, a feature Google says improved efficiency for the human researchers collaborating with it.

The agent also uses Google Search and web browsing to navigate published literature, which helps prevent the hallucinated citations and computational errors that plague standard models when they venture into advanced mathematical territory.

The performance gains since the IMO result have been substantial. Deep Think's January 2026 version scores up to 90% on IMO-ProofBench Advanced, significantly outperforming the July 2025 version that earned the gold medal. More importantly, Google demonstrated that inference-time scaling laws continue to hold as difficulty increases beyond Olympiad level into PhD-level exercises on their internal FutureMath Basic benchmark.

### Publishable Results, Not Just Benchmarks

What sets this work apart from typical AI benchmark announcements is that Aletheia has already contributed to actual research papers at varying levels of autonomy:

- A fully autonomous research paper (Feng26) that calculates structure constants in arithmetic geometry called eigenweights, generated without any human intervention.
- A human-AI collaboration paper (LeeSeo26) proving bounds on systems of interacting particles called independent sets.
- A semi-autonomous evaluation of 700 open problems on Bloom's Erdos Conjectures database, which produced autonomous solutions to four open questions, including Erdos-1051, where the model's solution helped lead to a broader generalization.

Google has proposed a taxonomy to classify these AI-assisted results by significance and degree of AI contribution. Several "Level 2" (publishable quality) works have been submitted to reputable journals. The team does not yet claim any Level 3 ("Major Advance") or Level 4 ("Landmark Breakthrough") results, a degree of restraint that lends credibility to the work.

### Crossing Into Physics and Computer Science

The second paper, "Accelerating Scientific Research with Gemini," extends the approach to 18 research problems across algorithms, machine learning, information theory, economics, and physics. The results are striking for the diversity of fields involved and the nature of the breakthroughs:

- **Network optimization**: Progress on classic problems like Max-Cut and the Steiner Tree had stalled for years. Deep Think broke both deadlocks by importing advanced tools from continuous mathematics, such as the Kirszbraun Theorem and measure theory, into these discrete algorithmic domains.
- **Disproving a decade-old conjecture**: A 2015 theory paper in online submodular optimization proposed a seemingly intuitive rule about data streams. Experts spent a decade trying to prove it. Deep Think engineered a precise three-item counterexample, rigorously demonstrating the conjecture was false.
- **ML optimization theory**: Researchers had developed a technique for automatically tuning regularization penalties but could not explain why it worked. Deep Think analyzed the equations and proved the method succeeds by implicitly generating its own adaptive penalty.
- **Economic theory for AI auctions**: A recent Revelation Principle for auctioning AI generation tokens only held when bids were restricted to rational numbers. Deep Think used advanced topology and order theory to extend the theorem to continuous real numbers, accommodating real-world auction dynamics.
- **Cosmic string physics**: Calculating gravitational radiation from cosmic strings requires solving integrals with singularities. Deep Think found a novel approach using Gegenbauer polynomials that naturally absorbed the singularities, collapsing an infinite series into a closed-form finite sum.

The paper identifies effective collaboration patterns, including an "Advisor" model where humans guide the AI through iterative cycles, and tactical techniques like "balanced prompting," where the model is asked to simultaneously prove or refute a claim to prevent confirmation bias.

### Gemini 3 Deep Think: The Upgrade

Alongside the research papers, Google released an upgraded version of Gemini 3 Deep Think that sets new records across multiple benchmarks:

- **48.4%** on Humanity's Last Exam (without tools), a benchmark designed to test the absolute limits of frontier models
- **84.6%** on ARC-AGI-2, verified by the ARC Prize Foundation
- **3455 Elo** on Codeforces competitive programming challenges
- **Gold-medal level** on the International Math Olympiad 2025
- **Gold-medal level** on the written sections of the 2025 International Physics and Chemistry Olympiads
- **50.5%** on CMT-Benchmark for advanced theoretical physics

The upgraded Deep Think is available to Google AI Ultra subscribers in the Gemini app. For the first time, Google is also making Deep Think available via the Gemini API through an early access program targeting researchers, engineers, and enterprises.

### What This Means for AI Research

The significance of this work is less about any single benchmark and more about a shift in what AI reasoning systems can do. Solving competition problems requires finding the correct answer to a well-defined question. Research requires navigating ambiguity, connecting disparate fields, admitting when an approach fails, and occasionally proving that widely held assumptions are wrong.

Google's results suggest that inference-time scaling, giving a model more compute to "think" at generation time, continues to yield returns even at the frontier of human knowledge. The Aletheia agent, in particular, demonstrates that pairing deep reasoning with verification loops and the ability to search real literature can push AI from a pattern-matching tool into something closer to a research collaborator.

Whether these results represent a fundamental shift or an impressive but narrow demonstration remains to be seen. But the fact that AI-generated proofs are being submitted to peer-reviewed journals, and that a model can autonomously solve open problems from a public conjecture database, suggests the relationship between AI and scientific research is entering a new phase.
