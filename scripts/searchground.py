import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_with_search(prompt, output="search_output.png", aspect_ratio=None, resolution=None):
    image_config_kwargs = {}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio
    if resolution:
        image_config_kwargs["image_size"] = resolution

    config_kwargs = {
        "response_modalities": ["Text", "Image"],
        "tools": [{"google_search": {}}],
    }
    if image_config_kwargs:
        config_kwargs["image_config"] = types.ImageConfig(**image_config_kwargs)

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            img = part.as_image()
            img.save(output)
            print(f"Image saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate images grounded with Google Search")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt (can reference real-time data)")
    parser.add_argument("--output", "-o", default="search_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    parser.add_argument("--resolution", "-r", default=None, choices=["1K", "2K", "4K"],
                        help="Output resolution")
    args = parser.parse_args()
    generate_with_search(args.prompt, args.output, args.aspect_ratio, args.resolution)
