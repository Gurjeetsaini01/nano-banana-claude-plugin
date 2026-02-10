# Contributing to Nano Banana

Thanks for your interest in contributing to the Nano Banana plugin.

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-mode`)
3. Make your changes
4. Test locally with `claude --plugin-dir /path/to/your/fork`
5. Commit your changes
6. Push to your fork and open a Pull Request

## Adding a New Generation Mode

1. Create a new Python script in `scripts/` following the existing pattern
2. Add the script to the decision tree in `commands/genimage.md`
3. Add the script to the agent at `agents/gemini-image-gen.md`
4. Update the skill at `skills/genimage/SKILL.md`
5. Update `README.md` with the new mode
6. Update `CHANGELOG.md`

## Script Conventions

- Use `argparse` with `--prompt` as required argument
- Load `.env` via `SCRIPT_DIR` pattern (not hardcoded paths)
- Support `--output`, `--aspect-ratio`, and `--image`/`--images` flags where applicable
- Print output filename on success

## Reporting Issues

Open an issue on GitHub with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your Python version and OS
