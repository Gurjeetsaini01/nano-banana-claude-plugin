import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def transfer_style(prompt, source_image, style_image, output="style_output.png"):
    client = get_client()
    
    # Gemini 3.1 handles style transfer via multi-modal prompt
    contents = [
        f"Apply the style of the first image to the second image based on this description: {prompt}",
        Image.open(style_image),
        Image.open(source_image)
    ]

    print(f"Transferring style with {NANO_BANANA_2}...")
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
            print(f"Styled image saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Style transfer with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Style instructions")
    parser.add_argument("--image", "-i", required=True, help="Source image")
    parser.add_argument("--style-image", "-s", required=True, help="Style reference image")
    parser.add_argument("--output", "-o", default="style_output.png", help="Output filename")
    args = parser.parse_args()
    transfer_style(args.prompt, args.image, args.style_image, args.output)
