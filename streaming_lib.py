import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client using the API key from .env
client = OpenAI()

def get_streaming_response(prompt, streaming_callback):
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-3.5-turbo",
        stream=True,
        max_tokens=2000,
        temperature=0.0
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            streaming_callback(chunk.choices[0].delta.content)