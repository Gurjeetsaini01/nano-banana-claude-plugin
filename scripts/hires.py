import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_hires(prompt, output="hires_output.png", aspect_ratio="1:1", resolution="2K"):
    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=resolution,
            ),
        ),
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            img = part.as_image()
            img.save(output)
            print(f"Image saved to {output} ({resolution} resolution, {aspect_ratio})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate high-resolution images (2K/4K)")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--output", "-o", default="hires_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default="1:1",
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--resolution", "-r", default="2K", choices=["1K", "2K", "4K"],
                        help="Output resolution (default: 2K)")
    args = parser.parse_args()
    generate_hires(args.prompt, args.output, args.aspect_ratio, args.resolution)
