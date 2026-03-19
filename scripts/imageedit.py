import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def edit_image(prompt, image_path, output="edited_image.png", aspect_ratio=None):
    client = get_client()
    image = Image.open(image_path)
    
    config = None
    if aspect_ratio:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio)
        )

    print(f"Editing image with {NANO_BANANA_2}...")
    response = client.models.generate_content(
        model=NANO_BANANA_2,
        contents=[prompt, image],
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            res_image = part.as_image()
            res_image.save(output)
            print(f"Edited image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image editing with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Editing instructions")
    parser.add_argument("--image", "-i", required=True, help="Path to source image")
    parser.add_argument("--output", "-o", default="edited_image.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None, help="Aspect ratio")
    args = parser.parse_args()
    edit_image(args.prompt, args.image, args.output, args.aspect_ratio)
