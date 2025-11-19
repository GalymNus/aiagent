import os


def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(full_path)
    file_name = full_path.split("/")[-1]
    only_directory = "/".join(full_path.split("/")[:-1])
    success_str = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    if (working_directory not in abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    exists = os.path.exists(file_path)
    if (exists):
        with open(file_path, "w") as file:
            file.write(content)
            return success_str
    else:
        os.makedirs(only_directory)
        with open(file_path, "x") as file:
            file.write(content)
        return success_str
