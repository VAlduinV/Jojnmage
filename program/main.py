import os
import openai
import json
from base64 import b64decode
from argparse import ArgumentParser
from pathlib import Path


class ImageGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def create_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='512x512',
            response_format='b64_json'
        )
        return response['data'][0]['b64']

    def save_image(self, data, filename):
        image_data = b64decode(data)
        with open(filename, 'wb') as file:
            file.write(image_data)


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
