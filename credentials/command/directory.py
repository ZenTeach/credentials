from typing import Generator, Tuple

import os
from io import BytesIO
import tempfile
from contextlib import ContextDecorator, contextmanager
from pathlib import Path


@contextmanager
def working_directory(path: Path) -> Generator[None, None, None]:
    """
        working_directory
    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

class SecureTempFile(ContextDecorator):
    """
        secure_temp_file
    """
    resolved_temp_directory = ""

    def __enter__(self) -> Generator[Tuple[BytesIO, str], None, None]:
        self.resolved_temp_directory = tempfile.mkstemp(suffix='.yml')
        with open(self.resolved_temp_directory[1], encoding='utf-8') as fp:
            yield fp

    def __exit__(self, *exc):
        try:
            os.rmdir(self.resolved_temp_directory[1])
        except:
            raise
