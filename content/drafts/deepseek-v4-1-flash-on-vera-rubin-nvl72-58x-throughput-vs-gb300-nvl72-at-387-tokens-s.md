---
title: "DeepSeek-V4.1-Flash on Vera Rubin NVL72: 58x Throughput vs. GB300 NVL72 at 387 tokens/s"
slug: "deepseek-v4-1-flash-on-vera-rubin-nvl72-58x-throughput-vs-gb300-nvl72-at-387-tokens-s"
date: 2026-11-12
time: "10:00"
status: draft
tags: [inference, performance]
summary: "TL;DR: On one NVIDIA Vera Rubin NVL72 rack, vLLM serves DeepSeek-V4.1-Flash at 1.7M tokens/s per GPU while each user gets 387 tokens/s, 58× GB300 NVL72, and reaches 2.52M at peak throughput and 1,810 tokens/s for a single user. The gains come from building on what is new in Rubin: kernels tuned for its split memory and FP4 tensor cores, specialized decode kernels for low latency, and a rack-wide KV cache and Engram tables shared over NVLink. This is the third post in our DeepSeek-V4.1-Flash s..."
source_url: "https://vllm-project.github.io/2026/11/12/deepseek-v41-flash-vera-rubin.html"
source_name: "vLLM Blog"
lang: de
---

> TL;DR: On one NVIDIA Vera Rubin NVL72 rack, vLLM serves DeepSeek-V4.1-Flash at 1.7M tokens/s per GPU while each user gets 387 tokens/s, 58× GB300 NVL72, and reaches 2.52M at peak throughput and 1,810 tokens/s for a single user. The gains come from building on what is new in Rubin: kernels tuned for its split memory and FP4 tensor cores, specialized decode kernels for low latency, and a rack-wide KV cache and Engram tables shared over NVLink. This is the third post in our DeepSeek-V4.1-Flash s...

Quelle: https://vllm-project.github.io/2026/11/12/deepseek-v41-flash-vera-rubin.html
