import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def run_chat(initial_prompt, output_prefix="multiturn", aspect_ratio=None, resolution=None):
    image_config_kwargs = {}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio
    if resolution:
        image_config_kwargs["image_size"] = resolution

    chat = client.chats.create(
        model="gemini-3-pro-image-preview",
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            tools=[{"google_search": {}}],
        ),
    )

    turn = 1
    message = initial_prompt
    while True:
        print(f"\n--- Turn {turn} ---")
        print(f"Prompt: {message}")

        config = None
        if image_config_kwargs:
            config = types.GenerateContentConfig(
                image_config=types.ImageConfig(**image_config_kwargs),
            )

        response = chat.send_message(message, config=config)

        for part in response.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                img = part.as_image()
                filename = f"{output_prefix}_{turn}.png"
                img.save(filename)
                print(f"Image saved to {filename}")

        turn += 1
        message = input("\nEnter next edit instruction (or 'quit' to exit): ").strip()
        if message.lower() in ("quit", "exit", "q", ""):
            print("Session ended.")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-turn chat-based image editing")
    parser.add_argument("--prompt", "-p", required=True, help="Initial prompt")
    parser.add_argument("--output-prefix", "-o", default="multiturn", help="Output filename prefix")
    parser.add_argument("--aspect-ratio", "-ar", default=None,
                        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                        help="Aspect ratio")
    parser.add_argument("--resolution", "-r", default=None, choices=["1K", "2K", "4K"],
                        help="Output resolution (Gemini 3 Pro only)")
    args = parser.parse_args()
    run_chat(args.prompt, args.output_prefix, args.aspect_ratio, args.resolution)
