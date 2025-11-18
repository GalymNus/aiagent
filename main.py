import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from aiagent!")
    args = sys.argv
    is_verbose = "--verbose" in sys.argv
    if (len(args) == 1):
        print("Not enough arguments")
        sys.exit(1)
    user_prompt = args[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if (is_verbose):
        print(f"User prompt: {user_prompt}")
    print("Response \n", response.text)
    if (is_verbose):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(
            f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
