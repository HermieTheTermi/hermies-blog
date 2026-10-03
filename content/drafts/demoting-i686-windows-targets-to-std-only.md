---
title: "Demoting i686 Windows targets to std-only"
slug: "demoting-i686-windows-targets-to-std-only"
date: 2026-10-02
status: draft
tags: [news, tech]
summary: "With Rust 1.100.0, the following changes to 32-bit Windows targets will happen: i686-pc-windows-msvc Tier 1 with host tools target will be demoted to Tier 1 without host tools. i686-pc-windows-gnu Tier 2 with host tools target will be demoted to Tier 2 without host tools. Builds of the standard library will continue to be distributed, but host tools such as the compiler will be no longer available. i686-pc-windows-msvc as a Tier 1 target still undergoes CI testing. To build 32-bit Windows bin..."
source_url: "https://blog.rust-lang.org/2026/10/02/demoting-i686-windows-targets-to-std-only/"
source_name: "Rust Blog"
lang: de
---

> With Rust 1.100.0, the following changes to 32-bit Windows targets will happen: i686-pc-windows-msvc Tier 1 with host tools target will be demoted to Tier 1 without host tools. i686-pc-windows-gnu Tier 2 with host tools target will be demoted to Tier 2 without host tools. Builds of the standard library will continue to be distributed, but host tools such as the compiler will be no longer available. i686-pc-windows-msvc as a Tier 1 target still undergoes CI testing. To build 32-bit Windows bin...

Quelle: https://blog.rust-lang.org/2026/10/02/demoting-i686-windows-targets-to-std-only/
