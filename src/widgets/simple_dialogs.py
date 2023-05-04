import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QDialogButtonBox
)

from constant_paths import (
    SAFT_CREDITS_PATH,
    SAFT_LOGO_SMALL_PATH,
    SAFT_LOGO_MEDIUM_PATH)


class AboutDialog(QDialog):
    """AboutDialog objects display a short message containing information about the program."""

    def __init__(self, dark_mode, light_theme, dark_theme):
        super().__init__()

        self.dark_mode = dark_mode
        self.light_theme = light_theme
        self.dark_theme = dark_theme

        if self.dark_mode:
            self.setPalette(dark_theme)
        else:
            self.setPalette(light_theme)

        self.setWindowTitle("About sAFT...")
        self.setWindowIcon(QIcon(SAFT_LOGO_SMALL_PATH))

        popup_message = QLabel(
            "<center>"
            "<h1>sAFT</h1>"
            "<p>v0.0.1</p>"
            f"<p><img src={SAFT_LOGO_MEDIUM_PATH}</p>"
            "<p>&copy; 2022-2022 Ptak Filip</p>"
            f"<a href={SAFT_CREDITS_PATH}>Credits</a>"
        )

        self.layout = QVBoxLayout()
        self.layout.addWidget(popup_message)
        self.setLayout(self.layout)

        self.setFixedSize(self.sizeHint())


class ExitDialog(QDialog):
    """ExitDialog objects display a short Yes/No message whether to exit the program."""

    def __init__(self, dark_mode, light_theme, dark_theme):
        super().__init__()

        self.dark_mode = dark_mode
        self.light_theme = light_theme
        self.dark_theme = dark_theme

        if self.dark_mode:
            self.setPalette(dark_theme)
        else:
            self.setPalette(light_theme)

        self.setWindowTitle("Exit...")
        self.setWindowIcon(QIcon(SAFT_LOGO_SMALL_PATH))

        # Configure choice buttons of the dialog.
        choice_buttons = QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No

        self.button_box = QDialogButtonBox(choice_buttons)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        popup_message = QLabel("Are you sure you want to exit the program?")

        # Create the dialog layout and add
        self.layout = QVBoxLayout()
        self.layout.addWidget(popup_message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)

        self.setFixedSize(self.sizeHint())

    def accept(self):
        """Exit the program after clicking the "Yes" button."""
        sys.exit()
