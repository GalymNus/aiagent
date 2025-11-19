import os
import subprocess
import sys


def run_python_file(working_directory, file_path, args=[]):
    print("file_path", file_path)
    path = os.path.join(working_directory, file_path)
    print("path", path)
    abs_path = os.path.abspath(path)
    print("abs_path", abs_path)
    print('file_path', file_path)
    print('working ', working_directory, abs_path,
          working_directory in abs_path)
    if (working_directory not in abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    right_extention = path.endswith(".py")
    if (not right_extention):
        return f'Error: "{file_path}" is not a Python file.'
    exists = os.path.exists(abs_path)
    print("exists", exists)
    if (not exists):
        return f'Error: File "{file_path}" not found.'
    try:
        commands = ["python", abs_path]
        if args:
            commands.extend(args)
        result_string = ""
        result_dict = subprocess.run(
            commands, cwd=working_directory, capture_output=True, timeout=30)
        print("result_dict", result_dict)
        if (len(result_dict.stdout) > 0):
            result_string += f"STDOUT: {result_dict.stdout}"
        if (len(result_dict.stderr) > 0):
            result_string += f"STDERR: {result_dict.stderr}"
        exit_code = result_dict.returncode
        if (exit_code != 0):
            result_string += f"Process exited with code {exit_code}"
        return result_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
