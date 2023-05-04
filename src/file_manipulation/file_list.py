from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QIcon

from constant_paths import FILETYPE_AUDIO_ICON_PATH


class FileList(QAbstractListModel):
    """FileList objects manipulate file lists."""

    def __init__(self, file_list=None):
        super().__init__()

        self.file_list = file_list or []

    def data(self, index, role):
        """Handle requests to FileList objects for data."""
        # If the type of data requested is text, return a filename.
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.file_list[index.row()]
            return text

        # If the type of data requested is decoration, return a file icon.
        if role == Qt.ItemDataRole.DecorationRole:
            icon = QIcon(FILETYPE_AUDIO_ICON_PATH)
            return icon

    def rowCount(self, index):
        """Return the number of rows in the current file list."""
        return len(self.file_list)
