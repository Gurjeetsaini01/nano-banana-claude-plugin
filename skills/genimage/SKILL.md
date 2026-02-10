---
name: Gemini Image Generation
description: Use when the user wants to generate images, edit images, create artwork, do style transfer, inpainting, 4K generation, or any visual content creation using the Gemini API. Activates on phrases like "generate an image", "create a picture", "edit this image", "style transfer", "remove background", "upscale to 4K", "inpaint", or "make an illustration".
version: 1.0.0
---

# Gemini Image Generation Skill

Provides comprehensive knowledge for generating and editing images using the Gemini API through a suite of 13 specialized Python scripts.

## Available Modes

### Text-to-Image (no input image)
- **Standard** (`texttoimage.py`): Fast generation via gemini-2.5-flash-image at 1K
- **High-res** (`hires.py`): 2K or 4K via gemini-3-pro-image-preview
- **Search-grounded** (`searchground.py`): Uses real-time Google Search data

### Image Editing (input image + text)
- **General edit** (`imageedit.py`): Any text-guided edit
- **Style transfer** (`styletransfer.py`): Apply style from a reference image
- **Inpainting** (`inpaint.py`): Replace/fill regions semantically
- **Add/remove** (`addremove.py`): Add or remove objects
- **Detail preserve** (`detailpreserve.py`): Edit while preserving fine details
- **Bring to life** (`bringtolife.py`): Animate static objects
- **360 view** (`consistency360.py`): Character consistency across angles

### Multi-Image
- **Compose** (`compose.py`): Combine elements from multiple images
- **Multi-reference** (`multiref.py`): Up to 14 reference images (gemini-3-pro)

### Interactive
- **Multi-turn** (`multiturn.py`): Chat-based iterative editing with memory

## Running Scripts

```
python "$CLAUDE_PLUGIN_ROOT/scripts/<script>.py" --prompt "..." [options]
```

## Prompting Guide

### Photorealistic Scenes
Use photography terms: camera angles, lens types, lighting, fine details.

**Template:** "A photorealistic [shot type] of [subject], [action], set in [environment]. Illuminated by [lighting], creating a [mood] atmosphere. Captured with [camera/lens]. [aspect ratio] format."

### Stylized Illustrations
Specify art style, color palette, medium, background.

**Template:** "A [style] illustration of [subject] in the style of [medium]. Color palette: [colors]. Background: [description]. No text."

### Text-Heavy Images
Put desired text in quotes. Specify font style and placement.

**Template:** "An image containing the text \"[text]\" in [font]. [Describe scene around it]."

### Product Photography
Describe materials, lighting setup, environment, camera angle.

**Template:** "Professional product photography of [product] on [surface]. [Lighting] lighting, [background]. Shot from [angle] with [lens]."

## Aspect Ratios

Supported: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`

## Resolution (gemini-3-pro-image-preview only)

- `1K` - Default (1024px)
- `2K` - High resolution (2048px)
- `4K` - Ultra resolution (4096px)

Must use uppercase K.

## Models

- **gemini-2.5-flash-image** (Nano Banana): Fast, 1K, high-volume
- **gemini-3-pro-image-preview** (Nano Banana Pro): Pro quality, up to 4K, thinking mode, search grounding, 14 reference images
