"""
    editor helper module
"""

import os
from logging import Logger
from typing import Optional
from .process import Process

logger = Logger(__name__)

class Editor:
    """
        Editor
    """
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
        """
            open_system_editor
        """
        system_caller = Process()
        system_caller(f"{self._system_editor} {path}")
