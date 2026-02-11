# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-02-11

### Changed
- Consolidated 13 scripts down to 8 genuinely distinct scripts
- Merged inpaint.py, addremove.py, detailpreserve.py, bringtolife.py, consistency360.py into imageedit.py (all were identical API calls)
- Updated documentation to clarify that all editing is text-guided (no visual UI or mask tool)
- Updated decision tree routing in command, agent, and skill

### Removed
- `inpaint.py` - functionality covered by `imageedit.py`
- `addremove.py` - functionality covered by `imageedit.py`
- `detailpreserve.py` - functionality covered by `imageedit.py`
- `bringtolife.py` - functionality covered by `imageedit.py`
- `consistency360.py` - functionality covered by `imageedit.py`

## [1.0.0] - 2026-02-10

### Added
- Initial release with 13 image generation modes
- `/genimage` slash command with smart script selection
- `gemini-image-gen` autonomous agent
- `genimage` auto-activating skill with prompting knowledge
- Text-to-image generation (gemini-2.5-flash-image)
- Image editing with text instructions
- Multi-turn chat-based iterative editing (gemini-3-pro-image-preview)
- Style transfer between images
- 4K resolution generation up to 4096x4096
- Google Search grounded image generation
- Multi-reference image generation (up to 14 images)
- Advanced multi-image composition
- Support for 10 aspect ratios and 3 resolution tiers
