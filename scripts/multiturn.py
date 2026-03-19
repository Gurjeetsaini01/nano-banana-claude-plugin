import argparse
from PIL import Image
from google.genai import types
from utils import get_client, NANO_BANANA_2

def multi_turn_edit(prompt, output="chat_output.png"):
    client = get_client()
    
    # Simple multi-turn simulation for CLI (stateless per call, but API supports it)
    # In a real chat, we'd persist the session. Here we treat it as an advanced generation.
    print(f"Processing chat-based edit with {NANO_BANANA_2}...")
    
    response = client.models.generate_content(
        model=NANO_BANANA_2,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            tools=[{"google_search": {}}]
        )
    )

    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(output)
            print(f"Iterative edit saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-turn chat editing with Gemini 3.1")
    parser.add_argument("--prompt", "-p", required=True, help="Chat instruction")
    parser.add_argument("--output", "-o", default="chat_output.png", help="Output filename")
    args = parser.parse_args()
    multi_turn_edit(args.prompt, args.output)
