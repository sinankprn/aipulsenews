---
author: Sinan Koparan
date: '2026-04-08 20:03:47'
description: Discover how we fingerprinted 178 AI models to reveal unique writing
  styles and 15 similarity clusters. See how GPT-4 and Gemini Pro compare in this
  study.
image: /assets/images/posts/show-hn-we-fingerprinted-178-ai-models-writing-sty.png
layout: post
sources:
- https://rival.tips/research/model-similarity
tags:
- AI
title: 'Show HN: We fingerprinted 178 AI models'' writing styles and similarity clusters'
toc: true
---

Rival.tips researchers have unveiled a new methodology for "fingerprinting" the writing styles of large language models (LLMs), analyzing 178 different AI models and identifying 15 distinct stylistic clusters. The research, which introduces a "Model Fingerprint Index," reveals both expected groupings of models from the same developer and surprising stylistic similarities across models from different creators, such as Google's Gemini Pro and OpenAI's GPT-4 Turbo. This exploratory study offers novel insights into AI model differentiation, potential convergence, and the future of AI content attribution.

## Unpacking the Methodology

The core of the research lies in a novel "semantic content fingerprinting technique" designed to capture the unique stylistic essence of each AI model. To achieve this, researchers employed a "zero-shot prompt" strategy, meaning the models were given instructions without any prior examples or context. Each of the 178 models was prompted to generate 10,000 words across 10 distinct topics, ensuring a broad and varied corpus for analysis.

These generated texts were then processed using a specialized "novel feature extraction algorithm." This algorithm converted the textual data into "numerical style embeddings," which are essentially vectors representing the distinct stylistic features of each model's output. These embeddings capture subtle nuances in vocabulary, sentence structure, tone, and overall rhetorical patterns.

To identify clusters of similar writing styles, the researchers applied a two-stage clustering process. First, Uniform Manifold Approximation and Projection (UMAP) was used for dimensionality reduction. UMAP is a non-linear technique that helps visualize and process high-dimensional data in a lower-dimensional space while preserving the local and global structure of the data. Following this, Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) was utilized for robust clustering. HDBSCAN is a density-based algorithm that can identify clusters of varying shapes and sizes, and is particularly effective at detecting outliers, which in this context could represent models with truly unique styles. This entire methodology is noted as being "model-agnostic," meaning it can be applied to any large language model regardless of its underlying architecture or training data.

## Key Insights and Implications for the AI Industry

The analysis of 178 models yielded 15 distinct stylistic clusters. As anticipated, models from the same developer often grouped together; for instance, various OpenAI models tended to form their own cluster, as did Google's offerings. Similarly, several open-source models, including variants of Mistral, Llama, and Gemma, also clustered together, indicating shared stylistic characteristics potentially arising from common architectural foundations or training data influences.

One of the most significant findings was the "cross-developer similarity." The research specifically highlights that Google's Gemini Pro and OpenAI's GPT-4 Turbo, despite originating from different development teams, were observed to cluster together in Cluster 1. This suggests a potential convergence in writing styles across leading AI models, possibly due to a shared understanding of "optimal styles" for generating coherent and natural language, or perhaps even unacknowledged influences in training data or architectural design. The researchers theorize that these models might be independently arriving at similar solutions for effective language generation.

The developed "Model Fingerprint Index" provides a framework for classifying AI models based on their writing style. It can identify new models and assign them to existing stylistic clusters, or conversely, pinpoint them as outliers if their style is sufficiently unique. This capability has profound implications for "AI provenance," offering a potential method to trace the origin or lineage of AI-generated content. Beyond simply identifying content as "AI-generated," this technique could eventually attribute it to a specific model family or even a particular developer.

For the broader AI industry, this research opens new avenues for "content detection, attribution, and synthetic media identification." It could lead to more nuanced tools for identifying the source of AI-generated text, moving beyond binary detection to a more granular understanding of which models, or types of models, are producing certain content. The findings also raise questions about "model differentiation" in an increasingly crowded market, and the "risk of homogenization" if models continue to converge towards similar stylistic outputs. This could challenge developers to cultivate and emphasize unique stylistic identities for their models.

## What to Watch

Future research will likely expand the dataset to include an even greater number of models and explore temporal shifts in model styles. Further investigation into the causal factors behind stylistic similarities, such as training data composition or architectural choices, will be crucial for understanding model evolution and differentiation.