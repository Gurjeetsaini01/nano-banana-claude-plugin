import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def generate(prompt, output="generated_image.png", aspect_ratio=None):
    client = get_client()
    config = None
    if aspect_ratio:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio)
        )

    print(f"Generating image with {NANO_BANANA_2}...")
    response = client.models.generate_content(
        model=NANO_BANANA_2,
        contents=[prompt],
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output)
            print(f"Image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text-to-image generation with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--output", "-o", default="generated_image.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    args = parser.parse_args()
    generate(args.prompt, args.output, args.aspect_ratio)
