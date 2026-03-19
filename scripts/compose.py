import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def compose(prompt, image_paths, output="compose_output.png"):
    client = get_client()
    contents = [prompt]
    for path in image_paths:
        contents.append(Image.open(path))

    print(f"Composing images with {NANO_BANANA_2}...")
    response = client.models.generate_content(
        model=NANO_BANANA_2,
        contents=contents,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output)
            print(f"Composed image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compose multiple images with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Composition instructions")
    parser.add_argument("--images", "-i", nargs="+", required=True, help="Paths to source images")
    parser.add_argument("--output", "-o", default="compose_output.png", help="Output filename")
    args = parser.parse_args()
    compose(args.prompt, args.images, args.output)
