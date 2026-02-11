---
name: Gemini Image Generation
description: Use when the user wants to generate images, edit images, create artwork, do style transfer, 4K generation, or any visual content creation using the Gemini API. Activates on phrases like "generate an image", "create a picture", "edit this image", "style transfer", "remove background", "upscale to 4K", or "make an illustration".
version: 1.0.0
---

# Gemini Image Generation Skill

Provides comprehensive knowledge for generating and editing images using the Gemini API through 8 specialized Python scripts.

## How It Works

All generation and editing is **text-guided** through the Gemini API. There is no visual UI, mask painter, or interactive editor. You describe what you want in natural language, and Gemini's AI handles the rest.

For image editing, Gemini **semantically understands** your text instructions and automatically identifies which regions of the image to modify. For example, "replace the sky with a sunset" - Gemini knows what "the sky" means and replaces only that region.

## Available Modes

### Text-to-Image (no input image)
- **Standard** (`texttoimage.py`): Fast generation via gemini-2.5-flash-image at 1K
- **High-res** (`hires.py`): 2K or 4K via gemini-3-pro-image-preview
- **Search-grounded** (`searchground.py`): Uses real-time Google Search data

### Image Editing (input image + text)
- **General edit** (`imageedit.py`): All text-guided editing - inpainting, add/remove objects, background replacement, detail-preserving edits, bringing sketches to life, changing angles, and any other modification
- **Style transfer** (`styletransfer.py`): Apply the artistic style of one image onto another (requires 2 images)

### Multi-Image
- **Compose** (`compose.py`): Combine elements from multiple images
- **Multi-reference** (`multiref.py`): Up to 14 reference images (gemini-3-pro)

### Interactive
- **Multi-turn** (`multiturn.py`): Chat-based iterative editing with memory

## Running Scripts

```
python "$CLAUDE_PLUGIN_ROOT/scripts/<script>.py" --prompt "..." [options]
```

## Editing Examples

All of these use `imageedit.py --image photo.png --prompt "..."`:

- **Inpainting**: "Replace the sky with dramatic storm clouds"
- **Remove object**: "Remove the person on the left and fill naturally"
- **Add object**: "Add a golden retriever sitting on the couch"
- **Background swap**: "Replace the background with a tropical beach"
- **Bring to life**: "Transform this pencil sketch into a photorealistic image"
- **Detail preserve**: "Place this logo on a billboard in Times Square, keep the logo sharp"
- **Style change**: "Make this photo look like an oil painting"

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
