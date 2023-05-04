from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QFrame


def create_light_mode():
    """Create and return light theme."""
    light_theme = QPalette()

    return light_theme


def create_dark_mode():
    """Create and return dark theme."""
    dark_theme = QPalette()
    dark_theme.setColor(QPalette.ColorRole.Window, QColor(50, 50, 50))
    dark_theme.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_theme.setColor(QPalette.ColorRole.Base, QColor(210, 210, 210))
    dark_theme.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))
    dark_theme.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    dark_theme.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_theme.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
    dark_theme.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
    dark_theme.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
    dark_theme.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_theme.setColor(QPalette.ColorRole.Link, QColor(40, 130, 220))
    dark_theme.setColor(QPalette.ColorRole.Highlight, QColor(40, 130, 220))
    dark_theme.setColor(QPalette.ColorRole.HighlightedText,
                        Qt.GlobalColor.white)

    return dark_theme


def create_vertical_separator():
    """Create and return a vertical separator."""
    vertical_separator = QFrame()
    vertical_separator.setFrameShape(QFrame.Shape.VLine)

    return vertical_separator
