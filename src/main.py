from PyQt6.QtGui import (
    QAction,
    QIcon,
    QKeySequence,
    QPixmap
)
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QListView
)

from utils.load_utils import (
    load_from_playlist_file,
    user_select_files,
    user_select_directory
)
from utils.edit_utils import playlist_loaded_files

from utils.view_utils import (
    create_light_mode,
    create_dark_mode,
    create_vertical_separator
)
from file_manipulation.file_list import FileList
from file_manipulation.file_edit import FileEdit
from constant_paths import SAFT_LOGO_SMALL_PATH

from widgets.simple_dialogs import AboutDialog, ExitDialog
from widgets.left_panel import LeftPanel


class MainWindow(QMainWindow):
    """MainWindow objects are the main GUI components of the program."""

    def __init__(self):
        super().__init__()

        # Set attributes related to the main window properties.
        self.setWindowTitle("sAFT")
        self.setWindowIcon(QIcon(SAFT_LOGO_SMALL_PATH))
        self.setMinimumSize(1280, 720)

        # Create light and dark themes.
        self.light_theme = create_light_mode()
        self.dark_theme = create_dark_mode()
        # Trn on the light theme.
        self.setPalette(self.light_theme)
        self.dark_mode = False

        # Create main menu and main window layout.
        self.create_main_menu()
        self.create_main_layout()
        self.setStatusBar(QStatusBar(self))

    def create_main_menu(self):
        """Create the main menu."""
        # A button used for creating playlists.
        playlist_files = QAction("Playlist (all files)", self)
        playlist_files.triggered.connect(self.playlist_all_files)
        playlist_files.setShortcut(QKeySequence("Ctrl+p"))

        # A button used for resetting the current file list.
        reset_list = QAction("Reset file list", self)
        reset_list.triggered.connect(self.reset_file_list)

        # A button used for choosing the currently used directory.
        change_dir = QAction("Change directory...", self)
        change_dir.triggered.connect(self.change_directory)
        change_dir.setShortcut(QKeySequence("Ctrl+d"))

        # A button used for adding files from a selected directory
        # to the current file list.
        add_dir = QAction("Add directory...", self)
        add_dir.triggered.connect(self.add_directory)

        # A button used for adding selected files to the current file list.
        add_files = QAction("Add files...", self)
        add_files.triggered.connect(self.add_selected_files)

        # A button used for replacing the current file list
        # with files loaded from a playlist.
        load_playlist = QAction("Load from a playlist...", self)
        load_playlist.triggered.connect(self.load_from_playlist)

        # A button used for exiting the program.
        exit_program = QAction("Exit", self)
        exit_program.triggered.connect(self.show_exit_dialog)
        exit_program.setShortcut(QKeySequence("Alt+f4"))

        # A button used for removing files from the current file list.
        remove_file = QAction("Remove", self)
        remove_file.triggered.connect(self.remove_from_file_list)
        remove_file.setShortcut(QKeySequence("Del"))

        # A button used for toggling dark mode.
        toggle_theme = QAction("Toggle dark theme", self)
        toggle_theme.triggered.connect(self.toggle_dark_mode)
        toggle_theme.setShortcut(QKeySequence("Ctrl+t"))

        # A button used for displaying About Program dialog.
        about_dialog = QAction("About...", self)
        about_dialog.triggered.connect(self.show_about_dialog)

        # Create a main menu bar.
        main_menu = self.menuBar()
        # Create a "File" submenu and add actions to it.
        file_menu = main_menu.addMenu("&File")

        file_menu.addAction(playlist_files)

        file_menu.addSeparator()
        file_menu.addAction(reset_list)
        file_menu.addAction(change_dir)
        file_menu.addAction(add_dir)
        file_menu.addAction(add_files)
        file_menu.addAction(load_playlist)

        file_menu.addSeparator()
        file_menu.addAction(exit_program)

        # Create an "Edit" submenu and add actions to it.
        edit_menu = main_menu.addMenu("&Edit")
        edit_menu.addAction(remove_file)

        # Create a "View" submenu and add actions to it.
        view_menu = main_menu.addMenu("&View")
        view_menu.addAction(toggle_theme)

        # Create a "Help" submenu and add actions to it.
        help_menu = main_menu.addMenu("&Help")
        help_menu.addAction(about_dialog)

    def create_main_layout(self):
        """Create the main layout of the program."""
        # Set the main layout of the program.
        self.main_layout = QHBoxLayout()

        # Create the left panel layout and add it to the main layout.
        self.left_panel = LeftPanel()
        self.main_layout.addWidget(self.left_panel)

        # Create a vertical separator.
        self.vertical_separator = create_vertical_separator()
        # Add the vertical separator between left and right panels.
        self.main_layout.addWidget(self.vertical_separator)

        # Create the right panel layout.
        right_panel_layout = QVBoxLayout()

        filename_label = QLabel("Filename")

        # Create a list object that will display files from the current file list.
        self.file_list_view = QListView()
        # Execute self.update_left_panel after selecting a file from the list.
        self.file_list_view.clicked.connect(self.update_left_panel)

        # Add the list to the right panel layout.
        right_panel_layout.addWidget(filename_label)
        right_panel_layout.addWidget(self.file_list_view)

        self.right_panel_model = FileList()
        self.file_list_view.setModel(self.right_panel_model)
        # Add the right panel layout to the main layout.
        self.main_layout.addLayout(right_panel_layout)

        # Create the main working area of the program.
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

    def update_left_panel(self, file):
        """Update the left panel with a new file."""
        # Load selected file to FileEdit object.
        self.left_panel_model = FileEdit(file.data())

        # Update Title tag combobox.
        self.left_panel.title_combobox.clear()
        self.left_panel.title_combobox.addItems([
            f"{self.left_panel_model.selected_file_title}",
            "<blank>",
            "<keep>"
        ])

        # Update Artist tag combobox.
        self.left_panel.artist_combobox.clear()
        self.left_panel.artist_combobox.addItems([
            f"{self.left_panel_model.selected_file_artist}",
            "<blank>",
            "<keep>"
        ])

        # Update Album tag combobox.
        self.left_panel.album_combobox.clear()
        self.left_panel.album_combobox.addItems([
            f"{self.left_panel_model.selected_file_album}",
            "<blank>",
            "<keep>"
        ])

        # Update embedded image label.
        self.left_panel.album_cover_pixmap.setPixmap(
            # Convert Qt QImage object to QPixmap object.
            QPixmap.fromImage(self.left_panel_model.selected_file_image)
        )

        # Refresh the panel.
        self.left_panel_model.layoutChanged.emit()

    def playlist_all_files(self):
        """Create an M3U8 playlist with files from the current file list."""
        playlist_loaded_files(self.right_panel_model.file_list)

    def reset_file_list(self):
        """Reset the current file list."""
        # Set the current file list to an empty list.
        self.right_panel_model.file_list = []

        # Refresh the panel.
        self.right_panel_model.layoutChanged.emit()

    def change_directory(self):
        """Reset the current file list and add files to it from a selected directory."""
        # Load files from the selected directory.
        loaded_files = user_select_directory()
        # Check whether selecting files action was aborted.
        if loaded_files:
            # Replace the old file list with newly loaded files.
            self.right_panel_model.file_list = loaded_files

        # Refresh the panel.
        self.right_panel_model.layoutChanged.emit()

    def add_directory(self):
        """Update the current file list with files from a selected directory."""
        # Load files from the selected directory.
        loaded_files = user_select_directory()
        # Check whether selecting directory action was aborted.
        if loaded_files:
            # Add loaded files to the current file list.
            self.right_panel_model.file_list.extend(loaded_files)

        # Refresh the panel.
        self.right_panel_model.layoutChanged.emit()

    def add_selected_files(self):
        """Update the current file list with selected files."""
        # Load the selected files.
        loaded_files = user_select_files()
        # Check whether selecting files action was aborted.
        if loaded_files:
            # Add loaded files to the current file list.
            self.right_panel_model.file_list.extend(loaded_files)

        # Refresh the panel.
        self.right_panel_model.layoutChanged.emit()

    def load_from_playlist(self):
        """Reset the current file list and add files to it from a selected playlist file."""
        # Load files from the selected playlist file.
        loaded_files = load_from_playlist_file()
        # Check whether selecting files action was aborted.
        if loaded_files:
            # Replace the old file list with newly loaded files.
            self.right_panel_model.file_list = loaded_files

        # Refresh the panel.
        self.right_panel_model.layoutChanged.emit()

    def show_exit_dialog(self):
        """Display a dialog with the option to exit the program."""
        exit_dialog = ExitDialog(
            self.dark_mode, self.light_theme, self.dark_theme)
        exit_dialog.exec()

    def remove_from_file_list(self):
        """Remove the selected file from the current file list."""
        # Create a list of selected files.
        indexes = self.file_list_view.selectedIndexes()

        if indexes:
            # Since it's possible to select only one file at a time,
            # the file is always the first item on the list.
            index = indexes[0]

            # Remove selected file from the current file list.
            del self.right_panel_model.file_list[index.row()]

            # Refresh the panel.
            self.right_panel_model.layoutChanged.emit()

    def toggle_dark_mode(self):
        """Check if dark mode is turned on and toggle dark mode on and off."""
        if not self.dark_mode:
            self.setPalette(self.dark_theme)
            self.dark_mode = True

        else:
            self.setPalette(self.light_theme)
            self.dark_mode = False

    def show_about_dialog(self):
        """Display a short message containing information about the program."""
        about_dialog = AboutDialog(
            self.dark_mode, self.light_theme, self.dark_theme)
        about_dialog.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
