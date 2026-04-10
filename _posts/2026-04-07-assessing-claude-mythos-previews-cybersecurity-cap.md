---
author: AI Pulse Staff
date: '2026-04-07 20:01:47'
description: Explore Claude Mythos Preview and its advanced cybersecurity capabilities.
  See how Project Glasswing secures software and defends against cyber threats.
faq:
- a: Project Glasswing is an Anthropic initiative to use Claude Mythos Preview to
    help secure critical global software and prepare the industry for new cybersecurity
    practices, particularly by enabling defenders to secure important systems before
    similar AI models are broadly released.
  q: What is Project Glasswing?
- a: Mythos Preview represents a substantial leap, significantly outperforming Opus
    4.6. For example, in a Firefox JavaScript engine exploit benchmark, Mythos Preview
    achieved working exploits 181 times, compared to Opus 4.6's near-0% success rate
    (two times out of several hundred attempts).
  q: How does Mythos Preview compare to previous Anthropic models in cybersecurity?
- a: Anthropic is using SHA-3 hashes as a commitment scheme for unpatched vulnerabilities
    and exploits to hold themselves accountable while adhering to a coordinated vulnerability
    disclosure process that prevents premature public disclosure of live threats.
    Once vulnerabilities are patched, the hashes will be replaced with links to the
    full details.
  q: Why is Anthropic disclosing unpatched vulnerabilities using SHA-3 hashes?
image: /assets/images/posts/assessing-claude-mythos-previews-cybersecurity-cap.png
layout: post
sources:
- https://red.anthropic.com/2026/mythos-preview/
tags:
- AI
- Anthropic
- LLM
title: Assessing Claude Mythos Preview's cybersecurity capabilities
toc: true
---

Anthropic announced on April 7, 2026, the public preview of Claude Mythos Preview, a new general-purpose language model demonstrating strikingly advanced capabilities in computer security tasks. This release is accompanied by the launch of Project Glasswing, an initiative aimed at leveraging Mythos Preview to secure critical global software and prepare the industry for evolving cyber threats. Anthropic's technical post provides detailed insights into how the model was tested and the findings from the past month, signaling a "watershed moment for security" and urging coordinated defensive action.

## The Significance of Mythos Preview for Cybersecurity

Mythos Preview has shown an ability to identify and exploit zero-day vulnerabilities, previously undiscovered flaws, across major operating systems and web browsers when directed by a user. The model uncovers subtle or difficult-to-detect vulnerabilities, with some dating back decades, such as a 27-year-old patched bug in OpenBSD. The exploits it constructs are sophisticated, including a web browser exploit that chained four vulnerabilities using a complex JIT heap spray to escape renderer and OS sandboxes. It also autonomously developed local privilege escalation exploits on Linux by exploiting race conditions and KASLR-bypasses, and a remote code execution exploit on FreeBSD's NFS server providing root access via a 20-gadget ROP chain split over multiple packets.

Notably, individuals without formal security training have successfully used Mythos Preview to find remote code execution vulnerabilities, receiving complete, working exploits overnight. This represents a rapid advancement, as Anthropic's previous model, Opus 4.6, had a near-0% success rate in autonomous exploit development. For instance, in a benchmark re-run with Mozilla's Firefox 147 JavaScript engine, Opus 4.6 developed working exploits only twice out of several hundred attempts, while Mythos Preview achieved this 181 times, gaining register control in 29 additional instances.

Internal benchmarks against approximately a thousand open-source repositories from the OSS-Fuzz corpus further highlight this leap. Mythos Preview achieved full control flow hijack (tier 5) on ten separate, fully patched targets, whereas Opus 4.6 and Sonnet 4.6 each achieved only a single crash at tier 3. Anthropic states these capabilities emerged as a downstream consequence of general improvements in code, reasoning, and autonomy, rather than explicit security training.

Anthropic believes that, in the long term, powerful language models will ultimately benefit defenders more than attackers, improving overall software security. However, the transitional period may be turbulent. Project Glasswing aims to give defenders an early advantage by making the model available to critical industry partners and open-source developers before models with similar capabilities become broadly accessible.

## Evaluation Methodology and Key Discoveries

Due to Mythos Preview's ability to saturate existing benchmarks, Anthropic shifted its focus to novel, real-world security tasks, particularly the discovery of zero-day vulnerabilities to ensure genuine capability rather than memorization from training data. The research primarily concentrated on memory safety vulnerabilities in critical software systems written in languages like C and C++, which are challenging to find and easy to verify using tools like Address Sanitizer.

The evaluation used a simple agentic scaffold: Mythos Preview, invoked as Claude Code, ran in an isolated container with the project-under-test. It was prompted to find a security vulnerability, then agentically experimented, hypothesizing, confirming, and rejecting suspicions, adding debug logic, and eventually producing a bug report with a proof-of-concept exploit or reproduction steps. To optimize search and diversity, agents focused on different files, prioritizing those ranked higher in likelihood of containing bugs. A final Mythos Preview agent then filtered and confirmed the importance of found bugs.

Anthropic adheres to a coordinated vulnerability disclosure process, manually validating high-severity bugs before reporting them. As a result, fewer than 1% of the potential vulnerabilities discovered thus far have been fully patched. To maintain accountability while protecting unpatched vulnerabilities, Anthropic committed to the SHA-3 hash of various vulnerabilities and exploits, promising to replace them with links to underlying documents once disclosure processes are complete.

Among the specific zero-day findings, Mythos Preview identified:
*   **A 27-year-old OpenBSD bug:** This vulnerability in OpenBSD's SACK implementation allowed an attacker to crash any OpenBSD host responding over TCP. It involved a subtle interplay of a singly linked list of "holes" in TCP SACK state, an incomplete length check, and a signed integer overflow in sequence number comparison, leading to a null pointer dereference. The total cost for 1,000 runs to find this and dozens of other findings was under $20,000.
*   **A 16-year-old FFmpeg vulnerability:** An out-of-bounds write was found in the H.264 codec, stemming from a 16-bit table entry mismatch with a 32-bit slice counter and a `memset(..., -1, ...)` sentinel collision. While not a critical severity vulnerability, it had remained undetected by fuzzers and human reviewers for years, highlighting the qualitative difference of advanced language models. This and other FFmpeg bugs, including three patched in FFmpeg 8.1, were found after several hundred runs costing roughly ten thousand dollars.
*   **A guest-to-host memory corruption bug:** In a production memory-safe Virtual Machine Monitor (VMM), Mythos Preview identified a vulnerability allowing a malicious guest an out-of-bounds write to host process memory through an unsafe operation. This unpatched bug, for which Anthropic committed SHA-3 hash `b63304b28375c023abaa305e68f19f3f8ee14516dd463a72a2e30853`, could lead to a denial-of-service attack, though Mythos Preview could not produce a functional exploit for this specific instance.

Anthropic estimates thousands of additional high- and critical-severity vulnerabilities are undergoing responsible disclosure. Human validators confirmed the model's severity assessment for 89% of 198 reviewed reports, and 98% were within one severity level, suggesting a large backlog of significant findings.

## Exploiting Zero-Day Vulnerabilities

Mythos Preview has demonstrated the ability to write exploits in hours that expert penetration testers might take weeks to develop. All discussed exploits target fully hardened systems with all defenses enabled.

A fully autonomous remote code execution vulnerability was identified and exploited in FreeBSD, a 17-year-old bug in NFS, designated CVE-2026-4747. This allowed unauthenticated attackers to gain root access. The vulnerability stemmed from an unprotected stack buffer overflow, where standard stack canaries were absent and the kernel's load address was not randomized. Mythos Preview circumvented further obstacles by leveraging an unauthenticated NFSv4 EXCHANGE_ID call to obtain necessary system information. It then constructed a multi-packet ROP chain to write an attacker's public key to the `/root/.ssh/authorized_keys` file, achieving complete control. This case demonstrated the model's ability to overcome complex exploitation challenges without human guidance, contrasting with Opus 4.6 which required it. Anthropic also indicated other FreeBSD vulnerabilities and exploits are in disclosure, with SHA-3 commitments provided for future transparency.

While Mythos Preview found numerous remotely triggerable out-of-bounds vulnerabilities in the Linux kernel, it was unable to successfully exploit any for remote code execution due to the kernel’s robust defense-in-depth measures. However, it did succeed in developing local privilege escalation exploits. By independently identifying and chaining multiple vulnerabilities, Mythos Preview achieved complete root access on Linux, demonstrating its capacity to overcome layered security by combining different weaknesses.

## What to Watch

The cybersecurity landscape appears poised for significant shifts with advanced AI models. The industry will need to closely monitor how rapidly defenders can integrate and leverage these tools to proactively patch systems, especially as similar AI capabilities become more widely available.