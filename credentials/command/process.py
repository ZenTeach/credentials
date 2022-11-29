"""
    process module
"""
import sys
from typing import Optional, IO
import subprocess

class Process:
    """
        Process
    """
    process = None
    def __init__(self, writer: Optional[IO] = sys.stdout):
        self.writer = writer

    @classmethod
    def execute_shell(cls, command):
        """
            execute_shell
        """
        processor = cls()
        try:
            processor(command)
        finally:
            processor.clean()

    def clean(self):
        """
            clean
        """
        self.writer.close()


    def __call__(self, command):
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE)
        for _c in iter(lambda: self.process.stdout.read(1), ""):
            self.writer.write(_c)
