import unittest

import HtmlTestRunner

HTML_REPORTS_DIR = 'reports'


def main():
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Load all test case class in tests folder.
    all_test_cases = unittest.defaultTestLoader.discover('tests', '*.py')

    # Loop the found test cases and add them into test suite.
    for test_case in all_test_cases:
        test_suite.addTests(test_case)

    # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=HTML_REPORTS_DIR)
    test_runner.run(test_suite)


if __name__ == '__main__':
    main()
