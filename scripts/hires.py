import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_PRO

def generate_hires(prompt, output="hires_output.png", resolution="4K", aspect_ratio=None):
    client = get_client()
    
    image_config_kwargs = {"image_size": resolution}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio

    config = types.GenerateContentConfig(
        image_config=types.ImageConfig(**image_config_kwargs)
    )

    print(f"Generating high-res ({resolution}) image with {NANO_BANANA_PRO}...")
    response = client.models.generate_content(
        model=NANO_BANANA_PRO,
        contents=[prompt],
        config=config,
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output)
            print(f"High-res image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="High-resolution generation with Gemini 3 Pro")
    parser.add_argument("--prompt", "-p", required=True, help="Text prompt")
    parser.add_argument("--resolution", "-r", default="4K", choices=["1K", "2K", "4K"], help="Target resolution")
    parser.add_argument("--output", "-o", default="hires_output.png", help="Output filename")
    parser.add_argument("--aspect-ratio", "-ar", default=None, help="Aspect ratio")
    args = parser.parse_args()
    generate_hires(args.prompt, args.output, args.resolution, args.aspect_ratio)
