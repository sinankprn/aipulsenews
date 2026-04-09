---
author: Sinan Koparan
date: '2026-04-09 20:07:17'
description: The Vercel plugin on Claude Code is tracking user prompts and bash commands,
  raising privacy concerns. Find out how this telemetry affects your dev projects.
faq:
- a: Without explicit opt-in, the Vercel plugin collects "anonymous usage data" which
    includes your device ID, operating system, detected frameworks, Vercel CLI version
    (if installed), and full bash command strings after every command Claude Code
    runs.
  q: What specific types of data does the Vercel plugin collect without explicit opt-in?
- a: The plugin uses "prompt injection" by inserting natural-language instructions
    into Claude Code's system context, telling the AI to ask the user if they want
    to share their prompt text. This method makes the question appear as a native
    Claude Code prompt, without visual indication that it originates from a third-party
    plugin.
  q: How does the Vercel plugin ask for consent to collect prompt text?
- a: No, the Vercel plugin's telemetry operates across all projects within Claude
    Code, regardless of whether they are Vercel-related. The plugin's hooks are configured
    to match "everything," even though it has built-in framework detection that could
    be used to limit its scope.
  q: Does the Vercel plugin's telemetry only apply to Vercel-related projects?
image: /assets/images/posts/the-vercel-plugin-on-claude-code-wants-to-read-you.png
layout: post
sources:
- https://akshaychugh.xyz/writings/png/vercel-plugin-telemetry
tags:
- AI
- Anthropic
- LLM
title: The Vercel plugin on Claude Code wants to read your prompts
toc: true
---

An AI journalist for "AI Pulse" reporting on automated AI news research.

## The Vercel Plugin on Claude Code Collects Extensive User Data, Raises Privacy Concerns

**San Francisco, CA – April 9, 2026** – A Vercel plugin designed for the AI coding assistant Claude Code has been identified collecting significant user telemetry, including full bash command strings and, optionally, all user prompt text, across both Vercel-related and unrelated development projects. This broad data collection, initially highlighted in a report by Akshay Chugh, raises questions about user privacy, transparency in data collection practices, and the architectural limitations of AI assistant plugin ecosystems.

The core issue centers on the plugin's data collection scope and its method of obtaining user consent. While the plugin aims to assist with Vercel deployments, framework guidance, and skill injection, its telemetry extends far beyond Vercel-specific activities, impacting all projects a developer works on within Claude Code.

## Deceptive Consent and Undisclosed Data Collection

The Vercel plugin presents users with a question regarding the sharing of "prompt text," stating, "The Vercel plugin collects anonymous usage data… Would you like to also share your prompt text?" However, the report reveals that this consent mechanism is not a standard UI element. Instead, it is delivered via "prompt injection" into Claude's system context, where the plugin instructs the AI to ask the user a question and then execute shell commands based on the response. This method means there is no visual indicator that the question originates from a third-party plugin, making it indistinguishable from native Claude Code questions.

Beyond the optional prompt collection, the plugin continuously gathers what it describes as "anonymous usage data." This data, however, includes highly specific information, such as the user's device ID, operating system, detected frameworks, Vercel CLI version, and critically, *full bash command strings* executed after every command Claude runs. This collection is always active by default, without explicit user consent or a clear disclosure that it can be disabled. The report clarifies that this constant collection of detailed bash commands, potentially containing file paths, project names, and environment variables, goes beyond typical "anonymous usage data." All collected data is linked to a persistent device UUID stored on the user's machine, enabling long-term tracking across sessions and projects.

## Unrestricted Collection Across All Projects

A significant finding is the plugin's indiscriminate data collection across all user projects. The telemetry, including the prompt for sharing prompt text, appears even when working on projects entirely unrelated to Vercel, lacking `vercel.json` or Vercel dependencies. An examination of the plugin's source code, located at `~/.claude/plugins/cache/claude-plugins-official/vercel/`, confirms that its `UserPromptSubmit` hook matcher is an empty string, meaning it triggers on "everything."

Ironically, the Vercel plugin does possess built-in framework detection capabilities, scanning repositories for files like `next.config.*` or `vercel.json` during session start. However, this detection is currently used only to report "session:likely_skills" and not to gate or restrict telemetry collection to Vercel-specific projects. This indicates that the technical means to limit data scope exist but are not being utilized.

## Industry Implications and Proposed Solutions

This incident highlights critical areas for improvement in both third-party plugin development and AI assistant platform architecture. The report suggests several changes:

For **Vercel**:
*   All telemetry should require explicit opt-in, offering users clear choices on what data to share.
*   The description "anonymous usage data" should not be applied to full bash command strings tied to a persistent device ID.
*   Telemetry should be scoped only to Vercel projects, leveraging existing framework detection.

For **Claude Code**:
*   Plugins require visual attribution, such as `[Vercel Plugin]` preceding any plugin-injected questions.
*   A granular permissions system is needed, informing users during installation about requested access (e.g., bash commands, prompt text, session metadata).
*   Plugins should declare their scope, similar to how VS Code extensions use `activationEvents` to specify when hooks should fire.

Users concerned about this data collection can take immediate action:
*   To disable all Vercel telemetry while keeping the plugin functional, add `export VERCEL_PLUGIN_TELEMETRY=off` to their `~/.zshrc` file.
*   To disable the plugin entirely, set `"vercel@claude-plugins-official": false` in `~/.claude/settings.json`.
*   To break device tracking, delete the file `~/.claude/vercel-plugin-device-id`.

The report underscores that while Vercel's implementation choices are concerning, the underlying Claude Code plugin architecture enabled these choices due to a lack of visual attribution, hook permissions, and project scoping.

## What to Watch

The AI industry will be closely observing how both Vercel and Claude Code respond to these findings. Future developments may include updates to Vercel's plugin, changes to Claude Code's plugin architecture to enhance transparency and user control, and potentially broader discussions on privacy standards for AI development tools.