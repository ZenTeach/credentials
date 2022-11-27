import os
from contextlib import contextmanager, ContextDecorator
import tempfile
from pathlib import Path

@contextmanager
def working_directory(path: Path):
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

@contextmanager
def temp_directory(ContextDecorator):
    resolved_temp_directory = ""
    temp_path = None

    def __enter__(self, file_path: Path, file_type: Optional[str] = "yml"):
        path_name = file_path.name
        temp_info = tempfile.mkstemp(suffix=f".{file_type}", prefix=f"{path_name}")
        self.temp_path =  temp_info[1]
        self.resolved_temp_directory = Path.joinpath(temp, (path_parent.__str__().split('/').join('_')))
        yield working_directory(self.resolved_temp_directory)

    def __exit__(self):
        try:
            os.rmdir(self.temp_path)
        except e:
            raise e
