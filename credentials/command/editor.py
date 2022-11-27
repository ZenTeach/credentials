import os
import subprocess
from logging import Logger
from typing import Optional
from pathlib import Path
from tempfiile import mkdtemp

logger = Logger(__name__)

class Editor:

    @property
    def _system_editor_not_set(self) -> bool:
        if os.getenv("EDITOR", "") == "":
              logger.error("No $EDITOR to open file in. Assign one like this:")
              logger.error("")
              logger.error("For editors that fork and exit immediately, it's important to pass a wait flag;")
              logger.error("otherwise, the file will be saved immediately with no chance to edit.")
              return False
        return True

    @property
    def _system_editor(self):
        editor = os.getenv("EDITOR", None)
        if editor is None:
            raise Exception(self._system_editor_not_set)

    def open_system_editor(self, path: Optional[str] = "") -> None:
        os.system(f"{self._system_editor} {path}")
