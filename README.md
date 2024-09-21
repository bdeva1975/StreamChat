# StreamChat

StreamChat is a Streamlit-based application that demonstrates real-time AI text generation using OpenAI's GPT models. This project showcases how to create a responsive and interactive chat interface with streaming responses.

## Features

- **Real-time Streaming**: Witness AI-generated responses appear instantly, word by word.
- **Simple UI**: Clean interface with an input area and a "Go" button for easy interaction.
- **OpenAI Integration**: Leverages OpenAI's powerful language models for high-quality responses.
- **Custom Streaming Library**: Efficient handling of API calls and response streaming.

## OpenAI API Features Used

- **Chat Completions API**: Utilizes the `gpt-3.5-turbo` model for generating responses.
- **Streaming**: Implements the streaming option to receive and display partial responses in real-time.
- **Temperature Control**: Set to 0.0 for more deterministic outputs.
- **Max Tokens**: Limit set to 2000 tokens per response.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/StreamChat.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the Streamlit app:
   ```
   streamlit run streaming_app.py
   ```

## Usage

1. Enter your text prompt in the input area.
2. Click the "Go" button to generate a response.
3. Watch as the AI-generated response appears in real-time!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
