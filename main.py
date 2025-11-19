import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from schemas import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.call_function import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from aiagent!")
    args = sys.argv
    system_prompt = """
        You are a helpful AI coding agent.
        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files
        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    is_verbose = "--verbose" in sys.argv
    if (len(args) == 1):
        print("Not enough arguments")
        sys.exit(1)
    user_prompt = args[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt
                                           ))
    if (is_verbose):
        print(f"User prompt: {user_prompt}")
    print("Response \n", response.text)
    print("Functions used: \n", )
    if (response.function_calls is not None):
        exceptions = []
        print("response.function_calls", response.function_calls)
        for func in response.function_calls:
            print("func", func)
            func_result = {}
            try:
                func_result = call_function(func, is_verbose)
            except Exception as e:
                exceptions.append(e)
            print("func_result", func_result)
            if (is_verbose):
                # print(
                #     f"-> {func_result.parts[0].function_response.response}")
                print(f"-> {func_result}")
            print("exceptions", exceptions)

    if (is_verbose):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(
            f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
