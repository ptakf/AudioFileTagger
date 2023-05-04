from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout
)

from constant_paths import PLACEHOLDER_IMAGE_NO_ALBUM_ART_PATH


class LeftPanel(QWidget):
    """
    LeftPanel object is used as the left panel of the main window layout.
    This object allows the user to modify a previously selected file.
    """

    def __init__(self):
        super().__init__()

        # Create left panel layout.
        self.left_panel_layout = QVBoxLayout(self)

        # Create title section.
        title_combobox_label = QLabel("Title")
        # Set width of the left panel.
        title_combobox_label.setFixedWidth(300)
        self.left_panel_layout.addWidget(title_combobox_label)

        self.title_combobox = QComboBox()
        self.title_combobox.addItems(["", "<blank>", "<keep>"])
        self.title_combobox.setEditable(True)
        self.left_panel_layout.addWidget(self.title_combobox)

        # Create artist section.
        artist_combobox_label = QLabel("Artist")
        self.left_panel_layout.addWidget(artist_combobox_label)

        self.artist_combobox = QComboBox()
        self.artist_combobox.addItems(["", "<blank>", "<keep>"])
        self.artist_combobox.setEditable(True)
        self.left_panel_layout.addWidget(self.artist_combobox)

        # Create album section.
        album_combobox_label = QLabel("Album")
        self.left_panel_layout.addWidget(album_combobox_label)

        self.album_combobox = QComboBox()
        self.album_combobox.addItems(["", "<blank>", "<keep>"])
        self.album_combobox.setEditable(True)
        self.left_panel_layout.addWidget(self.album_combobox)

        # Create album cover section.
        album_cover_label = QLabel("Cover")
        self.left_panel_layout.addWidget(album_cover_label)

        self.album_cover_pixmap = QLabel()
        self.album_cover_pixmap.setFixedSize(200, 200)
        self.album_cover_pixmap.setScaledContents(True)
        self.album_cover_pixmap.setPixmap(
            QPixmap(PLACEHOLDER_IMAGE_NO_ALBUM_ART_PATH))
        self.left_panel_layout.addWidget(self.album_cover_pixmap)
