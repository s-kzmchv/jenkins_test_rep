import os.path
import subprocess
import sys


class TestLibrary(object):

    def __init__(self):
        self._path = os.path.join('./', 'app.py')
        self._answer = ''

    def get_theoretical(self, start):
        self._run_command('get_theoretical', start)

    def get_im(self, start):
        self._run_command('get_im', start)

    def compare(self):
        self._run_command('compare')

    def expect_answer(self, expected_answer):
        if expected_answer != self._answer:
            raise AssertionError("Expected answer '%s' but was '%s'."
                                 % (expected_answer, self._answer))

    def expect_answer_with_approximation(self, expected_answer, approximation):
        if float(expected_answer) - float(self._answer) > float(approximation):
            raise AssertionError("Expected answer '%s' but was '%s'."
                                 % (expected_answer, self._answer))

    def _run_command(self, command, *args):
        command = [sys.executable, self._path, command] + list(args)
        print(command)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._answer = process.communicate()[0].strip()
