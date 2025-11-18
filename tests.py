import unittest

from functions.get_files_info import get_files_info


class TestFunctions(unittest.TestCase):
    def test_current_directory(self):
        print("----------------------------------------------------------------------")
        result = get_files_info("calculator", ".")
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
        result = get_files_info("calculator", "pkg")
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
        result = get_files_info("calculator", "/bin")
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
        result = get_files_info("calculator", "folder")
        expected = [
            "Result for 'folder' directory:",
            "Error: \"folder\" is not a directory"
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
