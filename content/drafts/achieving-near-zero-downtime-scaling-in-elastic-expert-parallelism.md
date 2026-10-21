---
title: "Achieving near-zero-downtime scaling in Elastic Expert Parallelism"
slug: "achieving-near-zero-downtime-scaling-in-elastic-expert-parallelism"
date: 2026-10-19
time: "02:00"
status: draft
tags: [inference, performance]
summary: "Traditionally, changing the number of GPUs in a vLLM service required adding or removing entire model replicas or restarting the engine with a different GPU count. As models grow larger, each replica needs more GPUs, so scaling by replica adds or removes GPUs in increasingly large increments. Restarting vLLM to scale DeepSeek V4 Pro from 16 to 20 GB200 GPUs stopped serving for 197 seconds (see the performance section for details), leaving those expensive GPUs allocated without generating toke..."
source_url: "https://vllm-project.github.io/2026/10/19/elastic-ep-near-zero-downtime.html"
source_name: "vLLM Blog"
lang: de
---

> Traditionally, changing the number of GPUs in a vLLM service required adding or removing entire model replicas or restarting the engine with a different GPU count. As models grow larger, each replica needs more GPUs, so scaling by replica adds or removes GPUs in increasingly large increments. Restarting vLLM to scale DeepSeek V4 Pro from 16 to 20 GB200 GPUs stopped serving for 197 seconds (see the performance section for details), leaving those expensive GPUs allocated without generating toke...

Quelle: https://vllm-project.github.io/2026/10/19/elastic-ep-near-zero-downtime.html
