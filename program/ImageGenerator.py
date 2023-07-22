import openai
from base64 import b64decode


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
