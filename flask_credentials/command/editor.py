import os
from logging import Logger
import subprocess
from tempfiile import mkdtemp

logger = Logger(__name__)

class Editor:

    @property
    def _system_editor_not_set(cls):
        if os.getenv("EDITOR", "") == "":
              logger.error("No $EDITOR to open file in. Assign one like this:")
              logger.error("")
              logger.error("For editors that fork and exit immediately, it's important to pass a wait flag;")
              logger.error("otherwise, the file will be saved immediately with no chance to edit.")

    @property
    def _system_editor(file_path: Path):
        editor = os.getenv("EDITOR", None)
        if editor is None:
            raise Exception(self._system_editor_not_not)

    def open_system_editor(self, path: Optional[str] = ""):
        os.system(f"{self._system_editor} {path}")
