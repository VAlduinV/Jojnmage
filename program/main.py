import os
import json
from argparse import ArgumentParser
from pathlib import Path
from ImageGenerator import *


def main():
    parser = ArgumentParser(description="Generate and save an image based on a prompt.")
    parser.add_argument("prompt", nargs='?', type=str, default="", help="The prompt for image generation.")
    args = parser.parse_args()

    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    generator = ImageGenerator(api_key)
    prompt = args.prompt.strip()
    if not prompt:
        print("Error: Please provide a prompt.")
        return

    image_data = generator.create_image(prompt)

    # Construct a valid filename without spaces
    filename = "_".join(prompt.split()).lower() + ".png"
    generator.save_image(image_data, filename)


if __name__ == "__main__":
    main()
