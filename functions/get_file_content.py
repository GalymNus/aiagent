import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(file_path)
    is_file = os.path.isfile(file_path)
    if (working_directory not in abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if (not is_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(file_path) as file:
        result = file.read(MAX_CHARS)
        if len(result) == MAX_CHARS:
            result = result[:MAX_CHARS] + \
                f"[...File '{file_path}' truncated at 10000 characters]."
        return result
