---
name: Gemini Image Generation
description: Knowledge for generating and editing images using the Gemini 3.1 API. Nano Banana 2 (Flash) and Nano Banana Pro (Pro). Use for artwork, style transfer, 4K generation, or any visual content creation.
version: 1.3.0
---

# Gemini Image Generation Skill

Knowledge for the Gemini API image generation suite (Nano Banana 2 and Pro).

## Models

- **Nano Banana 2** (`gemini-3.1-flash-image-preview`): Fast, high-efficiency, supports grounding, chat, and 14 reference images.
- **Nano Banana Pro** (`gemini-3-pro-image-preview`): Professional asset production, advanced reasoning, high-fidelity text, up to 4K.

## Setup

If the API key is not configured, run `/nano-banana:setup`.

## Available Modes

### Text-to-Image
- **Standard** (`texttoimage.py`): Nano Banana 2
- **High-res** (`hires.py`): Nano Banana Pro (2K/4K)
- **Search-grounded** (`searchground.py`): Nano Banana 2 (Real-time data)

### Editing
- **General edit** (`imageedit.py`): Text-guided inpainting, add/remove, background swap, etc.
- **Style transfer** (`styletransfer.py`): Apply style from one image to another.

### Multi-Image & Interactive
- **Compose** (`compose.py`): Combine elements from multiple images.
- **Multi-reference** (`multiref.py`): Mix up to 14 reference images.
- **Multi-turn** (`multiturn.py`): Chat-based iterative refinement.

## Resolutions

- `512` - Small (0.5K)
- `1K` - Default (1024px)
- `2K` - High resolution (2048px)
- `4K` - Ultra resolution (4096px)

Must use uppercase K.

## Prompting Template
"A photorealistic [shot type] of [subject], [action], set in [environment]. [Lighting], [mood]. Captured with [camera/lens]. [aspect ratio]."
