---
author: Sinan Koparan
date: '2026-04-06 14:14:29'
description: Does coding with LLMs lead to more microservices? Ben Borgers examines
  how AI tools are driving a shift toward smaller, more modular software architecture.
faq:
- a: Ben Borgers observed that LLM-assisted coding naturally tends to lead to a proliferation
    of small microservices, which are used by larger backend systems for specific
    tasks.
  q: What is the main observation regarding LLM-assisted coding and microservices?
- a: Microservices have a clearly defined interface, allowing LLMs to perform extensive
    internal refactoring without affecting external services, provided the contract
    with the outside world remains unchanged.
  q: Why do microservices facilitate LLM-assisted coding and refactoring?
- a: A large number of microservices can become difficult to maintain due to separate
    billing, hosting, and resources, increasing the risk of overlooking critical tasks
    like API account renewals.
  q: What are the potential long-term drawbacks of a microservice proliferation driven
    by LLMs?
image: /assets/images/posts/does-coding-with-llms-mean-more-microservices.png
layout: post
sources:
- https://ben.page/microservices
tags:
- AI
- LLM
title: Does coding with LLMs mean more microservices?
toc: true
---

# AI-Assisted Coding Leads to Microservice Proliferation, Says Ben Borgers

Ben Borgers has observed a growing trend where Large Language Model, LLM, assisted coding naturally fosters a proliferation of small microservices. This observation, published on April 5, 2026, suggests that a significant shift is underway in how software is architected and developed, particularly within the context of AI-driven tools. The core finding indicates that larger backend systems increasingly leverage these specialized microservices for distinct tasks, such as handling AI models for image and video generation.

## The LLM Affinity for Microservices

The inclination of LLMs toward microservice architecture stems from the inherent characteristics of microservices. A microservice is defined by its well-delineated surface area, with all inputs, such as requests, and outputs, like responses and webhooks, explicitly specified. This clear contract with the external world is crucial because it allows an LLM to perform extensive refactoring internally without affecting the broader system. As long as the external interface remains consistent, the internal workings, which might include the microservice's own database, caches, and object storage, are irrelevant to the calling services. Borgers likens this to a "bomb shelter" where an LLM, referred to as a "Claude-shaped bomb," can operate freely without causing wider system disruptions.

This architectural style stands in contrast to monolithic applications, or monoliths, where different parts of the application are often implicitly coupled. In a monolith, subtle dependencies, such as the order of operations or the naming of a cache key, can be relied upon by other, seemingly unrelated, components. This interconnectedness makes it easier to inadvertently entangle different parts of the application, increasing the risk of unintended side effects during modifications. Microservices, by design, significantly reduce this risk of implicit coupling, offering a more isolated environment for development and modification.

## Organizational Incentives and Long-Term Challenges

Beyond the technical advantages for LLM-assisted development, organizational factors also contribute to the adoption of microservices. Borgers points out two primary reasons why microservices often represent the "path of least resistance" for development teams. Firstly, being housed in a separate GitHub repository, a microservice project may undergo less scrutiny during pull request, PR, review processes, or even allow direct commits to the `main` branch. This reduced oversight can lead to faster iteration cycles and quicker deployment of new features or updates.

Secondly, access to production data and infrastructure can be significantly easier for microservices. Often, the main production database of a larger system is heavily secured and difficult for everyday engineers to access. However, the infrastructure supporting a standalone microservice may not be deemed as critically sensitive, thus providing developers with more straightforward access to necessary resources.

Despite these immediate benefits and organizational conveniences, Borgers acknowledges that a broad proliferation of microservices could lead to more significant challenges and maintenance overhead in the long term. Managing dozens of separate applications, each with its own billing accounts, hosting setups, and dedicated resources, can become complex. This fragmentation increases the likelihood of overlooking essential maintenance tasks, such as renewing an OpenAI API account for a specific image-generation microservice hosted on Vercel. Such oversights highlight the potential for increased operational burden and financial liabilities as the number of independent services grows.

## Implications for the AI Industry and Path Forward

The trend identified by Borgers suggests a future where AI's role in coding might not just accelerate development, but fundamentally reshape software architecture towards a highly distributed model. While LLMs excel at manipulating code within well-defined boundaries, the ease with which they can generate or modify components might inadvertently push organizations towards an architecture that, while expedient in the short term, could become difficult to manage at scale.

For the AI industry, this implies a need for tools and practices that not only facilitate LLM-assisted development but also guide it towards sustainable architectural patterns. If the aim is to foster better software development practices, those practices must be made easier to adopt and implement than the current "path of least resistance" offered by the rapid deployment of isolated microservices. This presents a challenge to balance the agility provided by AI coding assistants with the need for long-term maintainability and operational efficiency.

## What to Watch

Moving forward, the AI industry should monitor how development teams balance the immediate productivity gains from LLM-assisted microservice creation against the long-term operational complexities. Expect to see innovations in tooling and governance models designed to manage distributed architectures effectively, or perhaps shifts in LLM capabilities to better understand and manage implicit dependencies within larger codebases.