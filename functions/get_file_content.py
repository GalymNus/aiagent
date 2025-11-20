import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    exists = os.path.exists(os.path.dirname(abs_path))
    if (working_directory not in abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if (not exists):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(abs_path) as file:
        result = file.read(MAX_CHARS)
        if len(result) == MAX_CHARS:
            result = result[:MAX_CHARS] + \
                f"[...File '{file_path}' truncated at 10000 characters]."
        return result
