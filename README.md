<div align="center">

<img src="assets/logo.png" alt="Nano Banana Logo" width="180" />

# Nano Banana 2

**Google Gemini 3.1 image generation plugin for Claude Code**

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-blue?style=flat-square)](https://claude.ai/claude-code)
[![Gemini API](https://img.shields.io/badge/Powered_by-Gemini_3.1-4285F4?style=flat-square&logo=google)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.3.0-orange?style=flat-square)](CHANGELOG.md)

*One command. The full power of Gemini 3.1.*

</div>

---

<img src="assets/banner.png" alt="Nano Banana Banner" width="100%" />

---

## What is Nano Banana 2?

**Nano Banana 2** is powered by Gemini 3.1 Flash Image — Google's latest high-efficiency image generation model. This plugin wires those capabilities directly into Claude Code, providing a smart slash command, an autonomous agent, and a suite of Python scripts for every generation and editing mode.

Type `/genimage` and describe what you want. The agent handles script selection, prompt enhancement, and execution.

```
/genimage a photorealistic cyberpunk street in Cairo, neon palm trees, 16:9
```

---

## Setup

Before first use, run the setup command to configure your Gemini API key:

```bash
/nano-banana:setup
```

You can get a free API key at [Google AI Studio](https://aistudio.google.com/apikey).

---

## Capabilities

### Generation
- **Nano Banana 2** — High-speed, high-volume generation (Gemini 3.1 Flash)
- **Nano Banana Pro** — Professional asset production, up to 4K (Gemini 3 Pro)
- **Search-Grounded** — Imagery based on real-time Google Search data
- **14-Image Reference** — Mix up to 14 images for character and object consistency

### Editing (Text-Guided)
- **Zero-UI Editing** — Describe changes in plain text; Gemini identifies regions semantically.
- **Inpainting** — "Replace the sky with a sunset"
- **Object Manipulation** — "Remove the car" or "Add a cat on the sofa"
- **Style Transfer** — Apply the artistic style of one image to another

---

## Installation

### Option 1: Marketplace (Recommended)

```bash
/plugin marketplace add Ibrahim-3d/nano-banana-claude-plugin
/plugin install nano-banana@nano-banana-marketplace
```

### Option 2: Direct Install

```bash
/plugin install Ibrahim-3d/nano-banana-claude-plugin
```

### Option 3: Manual Clone

```bash
git clone https://github.com/Ibrahim-3d/nano-banana-claude-plugin.git ~/.claude/plugins/nano-banana
pip install google-genai python-dotenv Pillow
```

---

## Models

| Model | Codename | Purpose |
|-------|----------|---------|
| `gemini-3.1-flash-image-preview` | **Nano Banana 2** | Fast, Grounding, 14-Refs, Chat |
| `gemini-3-pro-image-preview` | **Nano Banana Pro** | 4K, Thinking Mode, Pro Assets |

---

## Requirements

- **Claude Code** (latest)
- **Python 3.9+**
- **Gemini API key** — [Get one free](https://aistudio.google.dev/)
- Python packages: `google-genai`, `python-dotenv`, `Pillow`

---

<div align="center">

**Built for Claude Code** | Powered by **Google Gemini 3.1**

**Nano Banana 2** 🍌 & **Nano Banana Pro** ✨

</div>
