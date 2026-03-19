import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def generate_with_refs(prompt, image_paths, output="multiref_output.png", aspect_ratio=None, resolution=None):
    client = get_client()
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
        config.image_config = types.ImageConfig(**image_config_kwargs)

    print(f"Generating with {len(image_paths)} references using {NANO_BANANA_2}...")
    response = client.models.generate_content(
        model=NANO_BANANA_2,
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
    parser = argparse.ArgumentParser(description="Multi-reference generation with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--images", "-i", nargs="+", required=True, help="Paths to reference images (up to 14)")
    parser.add_argument("--output", "-o", default="multiref_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None, help="Aspect ratio")
    parser.add_argument("--resolution", "-r", default=None, help="Resolution (1K, 2K, 4K)")
    args = parser.parse_args()
    if len(args.images) > 14:
        print("Error: Maximum 14 reference images supported.")
        exit(1)
    generate_with_refs(args.prompt, args.images, args.output, args.aspect_ratio, args.resolution)
