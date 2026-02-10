import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def style_transfer(prompt, image_path, style_image_path, output="styled_image.png", aspect_ratio=None):
    image = Image.open(image_path)
    style_image = Image.open(style_image_path)

    config = None
    if aspect_ratio:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio)
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, image, style_image],
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            result = part.as_image()
            result.save(output)
            print(f"Styled image saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transfer style from one image to another")
    parser.add_argument("--prompt", "-p", required=True,
                        help="Style transfer instruction (e.g. 'Apply the style of the second image to the first')")
    parser.add_argument("--image", "-i", required=True, help="Path to content image")
    parser.add_argument("--style-image", "-s", required=True, help="Path to style reference image")
    parser.add_argument("--output", "-o", default="styled_image.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    args = parser.parse_args()
    style_transfer(args.prompt, args.image, args.style_image, args.output, args.aspect_ratio)
