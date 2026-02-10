import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_with_refs(prompt, image_paths, output="multiref_output.png", aspect_ratio=None, resolution=None):
    contents = [prompt]
    for path in image_paths:
        contents.append(Image.open(path))

    image_config_kwargs = {}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio
    if resolution:
        image_config_kwargs["image_size"] = resolution

    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
    )
    if image_config_kwargs:
        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(**image_config_kwargs),
        )

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=contents,
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            img = part.as_image()
            img.save(output)
            print(f"Image saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate with up to 14 reference images")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--images", "-i", nargs="+", required=True, help="Paths to reference images (up to 14)")
    parser.add_argument("--output", "-o", default="multiref_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    parser.add_argument("--resolution", "-r", default=None, choices=["1K", "2K", "4K"],
                        help="Output resolution")
    args = parser.parse_args()
    if len(args.images) > 14:
        print("Error: Maximum 14 reference images supported.")
        exit(1)
    generate_with_refs(args.prompt, args.images, args.output, args.aspect_ratio, args.resolution)
