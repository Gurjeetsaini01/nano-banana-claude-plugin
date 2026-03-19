import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def generate_with_search(prompt, output="search_output.png", aspect_ratio=None, resolution=None):
    client = get_client()
    
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

    print(f"Generating search-grounded image with {NANO_BANANA_2}...")
    response = client.models.generate_content(
        model=NANO_BANANA_2,
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            img = part.as_image()
            img.save(output)
            print(f"Search-grounded image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search-grounded generation with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--output", "-o", default="search_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None, help="Aspect ratio")
    parser.add_argument("--resolution", "-r", default=None, help="Resolution")
    args = parser.parse_args()
    generate_with_search(args.prompt, args.output, args.aspect_ratio, args.resolution)
