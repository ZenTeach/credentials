from typing import IO, Callable, Generator, Optional

import os
from io import BytesIO
import tempfile
from contextlib import ContextDecorator, contextmanager
from pathlib import Path


@contextmanager
def working_directory(path: Path) -> Generator[None, None, None]:
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

class temp_directory(ContextDecorator):
    resolved_temp_directory = ""
    temp_path = None

    def __enter__(self, file_path: Path, file_type: Optional[str] = "yml") -> Generator[Tuple[BytesIO, str], None, None]:
        path_name = file_path.name
        self.resolved_temp_directory = tempfile.mkstemp(suffix=f".{file_type}", prefix=f"{path_name}")
        with open(self.resolved_temp_directory[1]) as fp:
            yield fp

    def __exit__(self):
        try:
            fp.close()
            os.rmdir(self.resolved_temp_directory[1])

        except e:
            raise e
