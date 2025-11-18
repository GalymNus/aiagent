import os


def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(path)
    erorr = ""
    if (working_directory not in abs_path):
        erorr = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    is_dir = os.path.isdir(path)
    if (not is_dir):
        erorr = f'Error: "{directory}" is not a directory'
    files = []
    if (not erorr):
        for file in os.listdir(path):
            is_file = os.path.isfile(f"{path}/{file}")
            size = os.path.getsize(f"{path}/{file}")
            is_dir = os.path.isdir(f"{path}/{file}")
            files.append(f"- {file}: is_dir={is_dir}, file_size={size} bytes")
    if (directory == "."):
        directory = "current"
    else:
        directory = f"\'{directory}\'"
    return f"Result for {directory} directory:\n" + "\n".join(files)[:-2]+erorr
