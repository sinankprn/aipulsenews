---
author: Sinan Koparan
date: '2026-04-05 19:40:03'
description: Run Google Gemma 4 locally with LM Studio's new lms headless CLI. See
  how to integrate this powerful model with Claude Code for a faster local AI workflow.
faq:
- a: Running AI models locally offers several benefits, including zero API usage costs,
    enhanced data privacy as information does not leave your machine, consistent availability,
    and avoidance of rate limits and network latency associated with cloud services.
  q: What is the primary benefit of running AI models locally rather than through
    cloud APIs?
- a: The Gemma 4 26B model utilizes a Mixture-of-Experts (MoE) architecture, which
    means it only activates a small subset of its total parameters, specifically 4
    billion, per forward pass. This design allows it to run efficiently on hardware
    that would typically struggle with a dense model of its full 26 billion parameter
    size, such as a laptop with 48 GB of unified memory.
  q: Why is Google Gemma 4 26B particularly well-suited for local inference on consumer
    hardware?
- a: The Gemma 4 26B-A4B model provides a 256K maximum context window, vision support
    for image and diagram analysis, native function and tool calling capabilities,
    and configurable thinking modes for enhanced reasoning, all while maintaining
    competitive performance with significantly larger cloud models.
  q: What specific features does the Gemma 4 26B-A4B model offer for local use?
image: /assets/images/posts/running-google-gemma-4-locally-with-lm-studios-new.png
layout: post
sources:
- https://ai.georgeliu.com/p/running-google-gemma-4-locally-with
tags:
- AI
- Google
- Anthropic
- LLM
title: Running Google Gemma 4 Locally with LM Studio's New Headless CLI and Claude
  Code
toc: true
---

## Running Google Gemma 4 Locally with LM Studio's New Headless CLI and Claude Code

**April 4, 2026** – LM Studio, a popular tool for local large language model (LLM) inference, has released version 0.4.0, introducing the `llmster` framework and a new headless command line interface (CLI) named `lms`. This development streamlines the process for running advanced models like Google's Gemma 4 26B locally, enabling integration with coding environments such as Claude Code, as demonstrated by tech enthusiast George Liu. The update addresses common challenges associated with cloud-based AI services, offering a robust solution for developers and researchers seeking greater control, privacy, and cost efficiency.

### The Growing Case for Local AI Inference

Cloud AI APIs, while powerful, often come with limitations such as rate limits, accumulating usage costs, potential privacy concerns, and network latency. These factors can hinder rapid iteration for tasks like code review, drafting documents, or testing prompts. Local inference, running models entirely on personal hardware, bypasses these issues by offering zero API costs, ensuring data remains on the user's machine, and providing consistent availability regardless of internet connectivity.

Google's Gemma 4 model family is particularly noteworthy for local deployment due to its innovative Mixture-of-Experts (MoE) architecture. Unlike dense models where all parameters are engaged in every computation, MoE models selectively activate a subset of "expert" sub-networks for each forward pass. This design dramatically reduces the computational load and memory footprint required for inference. For instance, the Gemma 4 26B parameter model only activates 4 billion parameters per forward pass, making it feasible to run on hardware that would struggle with a conventionally dense 26B model. George Liu reported achieving 51 tokens per second on a 14-inch MacBook Pro M4 Pro with 48 GB of unified memory, although some slowdowns were observed when integrated with Claude Code.

### Google Gemma 4: A Family of Models, with a Local Star

Google introduced Gemma 4 as a family of four distinct models, each tailored for different hardware capabilities and use cases. The "E" models, specifically E2B and E4B, utilize Per-Layer Embeddings, optimizing them for on-device deployment and providing unique support for audio input, including speech recognition and translation. The largest and most capable variant is the 31B dense model, which scores 85.2% on MMLU Pro and 89.2% on AIME 2026, two benchmarks for evaluating LLM capabilities.

However, for local inference on consumer-grade hardware, the Gemma 4 26B-A4B variant emerges as a "sweet spot." This model leverages its MoE architecture, featuring 128 experts plus one shared expert, but activates only 8 experts, totaling 3.8 billion parameters, per token. This design results in an inference cost comparable to a 4 billion dense model while delivering quality significantly above that class. Benchmarks show the 26B-A4B scoring 82.6% on MMLU Pro and 88.3% on AIME 2026, scores remarkably close to the more resource-intensive 31B dense model. Its Elo score, a rating system for model performance, is approximately 1441. For context, models like Qwen 3.5 397B-A17B (around 1450 Elo) and GLM-5 (around 1457 Elo) often require total parameters ranging from 100 to 600 billion to achieve similar performance levels. Kimi-K2.5, with an Elo of approximately 1457, demands over 1,000 billion parameters. The 26B-A4B's ability to compete at this level with a fraction of the parameters translates directly into lower memory requirements and faster local inference, making high-performance AI accessible on personal devices such as a laptop with 48 GB of unified memory.

The 26B-A4B further enhances its appeal with a 256K maximum context window, vision support for analyzing visual data like screenshots and diagrams, native function and tool calling capabilities, and configurable thinking modes for advanced reasoning. This combination of efficiency and capability makes MoE models, and specifically Gemma 4 26B-A4B, transformative for enabling powerful AI applications on local hardware.

### What to Watch

The continued development of headless CLIs for local inference platforms and the proliferation of efficient MoE models like Gemma 4 suggest a future where advanced AI capabilities are increasingly decentralized. Observers will be keen to see how these tools further reduce barriers to entry for AI development and deployment on personal devices, potentially fostering more privacy-conscious and custom AI solutions.