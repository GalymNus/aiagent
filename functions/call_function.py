from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from config import WORKING_DIRECTORY
from google.genai import types


def call_function(function_call_part, verbose=False):
    functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }
    function_name = function_call_part.name
    args = dict({"working_directory": WORKING_DIRECTORY,
                **function_call_part.args})
    if (verbose):
        print(
            f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")

    if (function_call_part.name not in functions):
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    func = functions[function_name]
    function_result = func(**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
