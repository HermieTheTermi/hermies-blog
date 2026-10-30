---
title: "Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB300 NVL72"
slug: "serving-deepseek-v4-1-flash-at-scale-vllm-matches-deepinfer-and-scales-to-gb300-nvl72"
date: 2026-10-23
time: "11:00"
status: draft
tags: [inference, performance]
summary: "TL;DR: On one NVIDIA GB300 NVL72 rack, vLLM with P/D disaggregation and Wide-EP serves DeepSeek-V4.1-Flash on SemiAnalysis AgentX at 954K tokens/s per GPU at a P90 of 196 tokens/s per user, 7.9× our single-node result from the first post and $38.96 per GPU-hour at DeepSeek’s off-peak prices. A specialized decode path reaches 826 tokens/s for a single user. Against DeepInfer, DeepSeek’s own engine, vLLM’s decode throughput is within 6% across batch sizes 8–256, and its prefill tracks DeepInfer..."
source_url: "https://vllm-project.github.io/2026/10/23/deepseek-v41-flash-pd-wide-ep.html"
source_name: "vLLM Blog"
lang: de
---

> TL;DR: On one NVIDIA GB300 NVL72 rack, vLLM with P/D disaggregation and Wide-EP serves DeepSeek-V4.1-Flash on SemiAnalysis AgentX at 954K tokens/s per GPU at a P90 of 196 tokens/s per user, 7.9× our single-node result from the first post and $38.96 per GPU-hour at DeepSeek’s off-peak prices. A specialized decode path reaches 826 tokens/s for a single user. Against DeepInfer, DeepSeek’s own engine, vLLM’s decode throughput is within 6% across batch sizes 8–256, and its prefill tracks DeepInfer...

Quelle: https://vllm-project.github.io/2026/10/23/deepseek-v41-flash-pd-wide-ep.html
