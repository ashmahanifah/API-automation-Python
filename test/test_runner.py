import webbrowser

import pytest

class TestRunner:
    def __init__(self, test_dir='test', report_file='report.html'):
        self.test_dir = test_dir
        self.report_file = report_file

    def run_tests(self):
        pytest.main([self.test_dir, f'--html={self.report_file}'])

if __name__ == '__main__':
    runner = TestRunner()
    runner.run_tests()

file_path = 'C:\\Users\\ashma.shalihah\\api-automation-python\\report.html'
webbrowser.open('file://' + file_path)



