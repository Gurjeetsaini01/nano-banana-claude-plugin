import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def inpaint(prompt, image_path, output="inpainted_image.png", aspect_ratio=None):
    image = Image.open(image_path)

    config = None
    if aspect_ratio:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio)
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, image],
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            result = part.as_image()
            result.save(output)
            print(f"Inpainted image saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inpainting / semantic masking on an image")
    parser.add_argument("--prompt", "-p", required=True,
                        help="Inpainting instruction (e.g. 'Replace the sky with a sunset')")
    parser.add_argument("--image", "-i", required=True, help="Path to input image")
    parser.add_argument("--output", "-o", default="inpainted_image.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    args = parser.parse_args()
    inpaint(args.prompt, args.image, args.output, args.aspect_ratio)
