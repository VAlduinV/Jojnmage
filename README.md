# Jojnmage

Jojnmage is a Python script that generates an image based on a user-provided prompt using the OpenAI API.

## Requirements

- Python 3.6 or higher
- Required Python libraries (see requirements.txt)

## Installation

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/VAlduinV/Jojnmage.git
    ```
    ```shell
    cd Jojnmage
    ```
   

2. Install the required Python libraries:

    ```shell
    pip install -r requirements.txt
    ```
   

## Usage

1. Set up your OpenAI API key:
- Obtain an API key from OpenAI by following their documentation (https://openai.com/docs/).
- Set your API key as an environment variable:
  ```
  export OPENAI_API_KEY=your_api_key_here
  ```

2. Run the script and provide a prompt to generate the image:

    ```shell
    python main.py "The prompt for image generation goes here"
    ```
   
Replace `"The prompt for image generation goes here"` with your desired prompt. Make sure to enclose the prompt in double quotes if it contains spaces.

3. The generated image will be saved in the current directory with a filename based on the prompt text.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- [VAlduinV](https://github.com/VAlduinV)

## Acknowledgments

Jojnmage uses the OpenAI API for image generation. We acknowledge the creators of the OpenAI API for their fantastic work.

## Troubleshooting

If you encounter any issues or have questions, please [create an issue](https://github.com/VAlduinV/Jojnmage/issues) in the repository.

## Support

For any support or further assistance, you can contact the author via email: prime72w@gmail.com.
