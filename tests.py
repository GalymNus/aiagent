import os
import unittest

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from config import WORKING_DIRECTORY


class TestFunctions(unittest.TestCase):
    def test_current_directory(self):
        print("----------------------------------------------------------------------")
        result = get_files_info(WORKING_DIRECTORY, ".")
        expected = [
            "Result for current directory:",
            "- main.py: is_dir=False, file_size=",
            "- pkg: is_dir=True, file_size="
        ]
        print("Result:\n", result)
        for line in expected:
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_pkg_directory(self):
        print("----------------------------------------------------------------------")
        result = get_files_info(WORKING_DIRECTORY, "pkg")
        expected = [
            "Result for 'pkg' directory:",
            "- calculator.py: is_dir=False, file_size=",
            "- render.py: is_dir=False, file_size="
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_bin_directory(self):
        print("----------------------------------------------------------------------")
        result = get_files_info(WORKING_DIRECTORY, "/bin")
        expected = [
            "Result for '/bin' directory:",
            "Error: Cannot list \"/bin\" as it is outside the permitted working directory",
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test__directory(self):
        print("----------------------------------------------------------------------")
        result = get_files_info(WORKING_DIRECTORY, "folder")
        expected = [
            "Result for 'folder' directory:",
            "Error: \"folder\" is not a directory"
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_main_content(self):
        print("----------------------------------------------------------------------")
        result = get_file_content(WORKING_DIRECTORY, "calculator/main.py")
        expected = [
            'Usage: python main.py "<expression>',
            'to_print = format_json_output(expression, result)',
            'print("Error: Expression is empty or contains only whitespace.")'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_calculator_content(self):
        print("----------------------------------------------------------------------")
        result = get_file_content(
            WORKING_DIRECTORY, "calculator/pkg/calculator.py")
        expected = [
            'raise ValueError("invalid expression")',
            'raise ValueError(f"not enough operands for operator {operator}"',
            'values.append(self.operators[operator](a, b))'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_lorem_content(self):
        print("----------------------------------------------------------------------")
        path = "lorem.txt"
        result = get_file_content(WORKING_DIRECTORY, path)
        expected = [
            f"wait, this isn't lorem ipsum",
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_non_exist_content(self):
        print("----------------------------------------------------------------------")
        result = get_file_content(
            WORKING_DIRECTORY, "calculator/pkg/does_not_exist.py")
        expected = [
            'Error: File not found or is not a regular file:',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_write_lorem_content(self):
        print("----------------------------------------------------------------------")
        content = "wait, this isn't lorem ipsum"
        path = "calculator/lorem.txt"
        result = write_file(
            WORKING_DIRECTORY, path, content)
        expected = [
            f'Successfully wrote to "{path}" ({len(content)} characters written)',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")
        with open(path) as file:
            file_content = file.read()
            print("expected:\n", content, f"| in file {path}")
            self.assertTrue(content in file_content,
                            f"{content} <= is missing")

    def test_write_morelorem_content(self):
        print("----------------------------------------------------------------------")
        content = "lorem ipsum dolor sit amet"
        path = "calculator/pkg/morelorem.txt"
        result = write_file(
            WORKING_DIRECTORY, path, content)
        expected = [
            f'Successfully wrote to "{path}" ({len(content)} characters written)',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")
        with open(path) as file:
            file_content = file.read()
            print("expected:\n", content, f"| in file {path}")
            self.assertTrue(content in file_content,
                            f"{content} <= is missing")

    def test_write_readme_content(self):
        print("----------------------------------------------------------------------")
        content = "# calculator"
        path = "readme.md"
        result = write_file(
            WORKING_DIRECTORY, path, content)
        expected = [
            f'Successfully wrote to "{path}" ({len(content)} characters written)',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")
        with open(f"./{WORKING_DIRECTORY}/{path}") as file:
            file_content = file.read()
            print("expected:\n", content, f"| in file {path}")
            self.assertTrue(content in file_content,
                            f"{content} <= is missing")

    def test_write_outside_content(self):
        print("----------------------------------------------------------------------")
        content = "# calculator"
        path = "./README2.md"
        result = write_file(
            WORKING_DIRECTORY, path, content)
        expected = [
            f'Error: Cannot write to "{path}" as it is outside the permitted working directory',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")
        exists = os.path.exists(path)
        self.assertFalse(exists, f"{path} <= should not exist")

    def test_main_run(self):
        print("----------------------------------------------------------------------")
        path = "main.py"
        result = run_python_file(
            WORKING_DIRECTORY, path)
        expected = [
            f'Calculator App',
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_main_run_with_args(self):
        print("----------------------------------------------------------------------")
        path = "main.py"
        result = run_python_file(
            WORKING_DIRECTORY, path, ["3 + 5"])
        expected = [
            'expression": "3 + 5"',
            '"result": 8'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_tests_run(self):
        print("----------------------------------------------------------------------")
        path = "tests.py"
        result = run_python_file(
            WORKING_DIRECTORY, path)
        expected = [
            f'Ran 9 tests in'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected no:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_diff_main_run(self):
        print("----------------------------------------------------------------------")
        path = "../main.py"
        result = run_python_file(
            WORKING_DIRECTORY, path)
        expected = [
            f'Error: Cannot execute "{path}" as it is outside the permitted working directory'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_non_existing_run(self):
        print("----------------------------------------------------------------------")
        path = "nonexistent.py"
        result = run_python_file(
            WORKING_DIRECTORY, path)
        expected = [
            f'Error: File "{path}" not found.'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")

    def test_lorem_run(self):
        print("----------------------------------------------------------------------")
        path = "lorem.txt"
        result = run_python_file(
            WORKING_DIRECTORY, path)
        expected = [
            f'Error: "{path}" is not a Python file.'
        ]
        print("Result:\n", result)
        for line in expected:
            print("expected:\n", line, "| in result")
            self.assertTrue(line in result, f"{line} <= is missing")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFunctions)
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    print("\n--- Final Test Summary ---")
    print(f"Total Tests Run: {result.testsRun}")
    print(
        f"Passes (OK):     {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fails:           {len(result.failures)}")
    print(f"Errors:          {len(result.errors)}")
