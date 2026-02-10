# Nano Banana - Gemini Image Generation Plugin for Claude Code

> The most complete Google Gemini image generation plugin for Claude Code. 13 generation modes, text-to-image, image editing, style transfer, inpainting, 4K output, and more - all from a single `/genimage` command.

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-blue)](https://claude.ai/claude-code)
[![Gemini API](https://img.shields.io/badge/Powered_by-Gemini_API-4285F4)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange)](CHANGELOG.md)

---

## What is Nano Banana?

**Nano Banana** is Google's name for Gemini's native image generation capabilities. This plugin brings all of those capabilities directly into Claude Code through 13 specialized Python scripts, a smart slash command, and an AI agent that automatically picks the right tool for your task.

**One command. Every Gemini image mode.**

```
/genimage a photorealistic close-up of a coffee cup on a rainy window ledge, warm lighting
```

---

## Capabilities

### Generation
- **Text-to-Image** - Describe any scene and get a generated image
- **4K Ultra Resolution** - Output up to 4096x4096 pixels with Gemini 3 Pro
- **Search Grounded Generation** - Create images using real-time data from Google Search (weather, news, stock charts, live events)
- **Batch Aspect Ratios** - 10 ratios from square 1:1 to ultrawide 21:9

### Editing
- **Image Editing** - Modify any image with natural language instructions
- **Inpainting** - Semantically replace or fill regions of an image
- **Add/Remove Elements** - Add objects, remove unwanted elements, fill naturally
- **High-Fidelity Detail Preservation** - Edit images while keeping fine details intact (logos, textures, text)
- **Style Transfer** - Apply the artistic style of one image onto another

### Advanced
- **Multi-turn Editing** - Chat-based iterative refinement with full conversation memory
- **Multi-Reference Composition** - Combine up to 14 reference images (6 objects + 5 humans) into a single output
- **Character Consistency** - Generate 360-degree views and maintain character identity across angles
- **Bring to Life** - Transform static objects, drawings, or sketches into photorealistic versions
- **Advanced Composition** - Merge elements from multiple source images into one cohesive result

### Prompting Intelligence
- **Smart Script Selection** - The AI agent automatically picks the right generation mode based on your request
- **Prompt Enhancement** - Helps you craft effective prompts using photography terms, art direction, and composition language
- **Prompt Templates** - Built-in templates for photorealistic, illustration, product, and text-heavy images

---

## All 13 Generation Modes

| Mode | What it does | Gemini Model |
|------|-------------|--------------|
| **Text-to-Image** | Generate images from text prompts | Gemini 2.5 Flash Image |
| **Image Editing** | Edit existing images with text instructions | Gemini 2.5 Flash Image |
| **Multi-turn Editing** | Iterative chat-based image refinement with memory | Gemini 3 Pro Image |
| **Style Transfer** | Apply the artistic style of one image to another | Gemini 2.5 Flash Image |
| **Inpainting** | Semantic region replacement and fill | Gemini 2.5 Flash Image |
| **Add/Remove Elements** | Add or remove objects from images | Gemini 2.5 Flash Image |
| **High-Fidelity Preservation** | Edit images while preserving fine details | Gemini 2.5 Flash Image |
| **4K Generation** | Generate images up to 4096x4096 resolution | Gemini 3 Pro Image |
| **Search Grounding** | Generate images based on real-time Google Search data | Gemini 3 Pro Image |
| **Multi-Reference** | Combine up to 14 reference images into one output | Gemini 3 Pro Image |
| **Character Consistency** | 360-degree views and consistent character angles | Gemini 2.5 Flash Image |
| **Advanced Composition** | Combine elements from multiple source images | Gemini 2.5 Flash Image |
| **Bring to Life** | Animate static objects into realistic versions | Gemini 2.5 Flash Image |

---

## Quick Start

### 1. Install the plugin

```
/install-plugin https://github.com/Ibrahim-3d/nano-banana-claude-plugin
```

### 2. Install Python dependencies

```bash
pip install google-genai python-dotenv Pillow
```

### 3. Get a Gemini API key

Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 4. Configure your key

```bash
cp scripts/.env.example scripts/.env
# Edit scripts/.env and add your key:
# GEMINI_API_KEY=your_key_here
```

### 5. Generate images

```
/genimage a futuristic Tokyo streetscape at golden hour, neon signs, 16:9
```

---

## Usage Examples

### Text-to-Image
```
/genimage a watercolor painting of a lighthouse during a storm
```

### Image Editing
```
/genimage edit photo.png - replace the sky with a dramatic sunset
```

### 4K High Resolution
```
/genimage 4K Da Vinci style anatomical sketch of a butterfly on parchment
```

### Style Transfer
```
/genimage apply the style of starry-night.jpg onto my photo.png
```

### Search Grounded (Real-Time Data)
```
/genimage visualize the current weather forecast for NYC as a modern infographic
```

### Inpainting
```
/genimage replace the background in portrait.png with a mountain landscape
```

### Add/Remove Objects
```
/genimage remove the car from street-photo.png and fill naturally
```

### Multi-Reference (up to 14 images)
```
/genimage group photo of person1.png person2.png person3.png in an office setting
```

### Bring to Life
```
/genimage bring this pencil sketch to life as a photorealistic image
```

### Character Consistency
```
/genimage show this character from front, side, back, and 3/4 view in a 2x2 grid
```

---

## Supported Aspect Ratios

`1:1` | `2:3` | `3:2` | `3:4` | `4:3` | `4:5` | `5:4` | `9:16` | `16:9` | `21:9`

## Supported Resolutions (Gemini 3 Pro Image)

| Resolution | Max Size |
|-----------|----------|
| **1K** | 1024 x 1024 (default) |
| **2K** | 2048 x 2048 |
| **4K** | 4096 x 4096 |

---

## Models

| Model | Codename | Best For |
|-------|----------|----------|
| `gemini-2.5-flash-image` | **Nano Banana** | Fast generation, high-volume, low-latency |
| `gemini-3-pro-image-preview` | **Nano Banana Pro** | Professional assets, 4K, thinking mode, search grounding, 14 reference images |

---

## Plugin Components

| Component | File | Purpose |
|-----------|------|---------|
| Slash Command | `commands/genimage.md` | `/genimage` - user-facing command with smart routing |
| Agent | `agents/gemini-image-gen.md` | Autonomous agent for complex image tasks |
| Skill | `skills/genimage/SKILL.md` | Auto-activating prompting knowledge and decision tree |
| Scripts | `scripts/*.py` | 13 specialized Python scripts for each generation mode |

---

## Plugin Structure

```
nano-banana-claude-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── genimage.md
├── agents/
│   └── gemini-image-gen.md
├── skills/
│   └── genimage/
│       └── SKILL.md
├── scripts/
│   ├── .env.example
│   ├── texttoimage.py
│   ├── imageedit.py
│   ├── multiturn.py
│   ├── multiref.py
│   ├── searchground.py
│   ├── hires.py
│   ├── styletransfer.py
│   ├── inpaint.py
│   ├── addremove.py
│   ├── detailpreserve.py
│   ├── bringtolife.py
│   ├── consistency360.py
│   └── compose.py
├── requirements.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

---

## Requirements

- **Claude Code** (latest version)
- **Python 3.9+**
- **Google Gemini API key** ([get one free](https://aistudio.google.com/apikey))
- Python packages: `google-genai`, `python-dotenv`, `Pillow`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new generation modes and submitting pull requests.

## Security

See [SECURITY.md](SECURITY.md) for API key safety and vulnerability reporting.

## License

[MIT](LICENSE)

---

**Built for Claude Code** | Powered by **Google Gemini API** | **Nano Banana** & **Nano Banana Pro**
