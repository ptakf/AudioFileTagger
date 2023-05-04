import os

from PyQt6.QtWidgets import QFileDialog

from constant_paths import USER_DIRECTORY_PATH


def remove_file_paths(files):
    """Generate a list of filenames of passed files without their full paths."""
    for file in files:
        # Return the base name of the pathname.
        yield os.path.basename(file)


def list_directory_files(directory):
    """Generate a list of all audio files in a selected directory."""
    for file in os.listdir(directory):
        # Check if the file extension in lowercase is in the list.
        if os.path.splitext(file)[-1].lower() in [
            ".mp3",
            ".flac"
        ]:
            # Return a file with a normalized pathname.
            yield os.path.normpath(os.path.join(directory, file))


def user_select_directory():
    """
    Prompt the user to select a directory using the system file dialog
    and return a list of audio files from the directory.
    """
    selected_directory = QFileDialog.getExistingDirectory(
        None,
        "Select a directory.",
        USER_DIRECTORY_PATH
    )

    # Check whether selecting directory action was aborted.
    if selected_directory:
        # Return a list of files.
        return list(list_directory_files(selected_directory))


def normalize_file_paths(files):
    """Generate a list of filenames of passed files with normalized file paths."""
    for file in files:
        # Return the normalized pathname of a file.
        yield os.path.normpath(file)


def user_select_files():
    """
    Prompt the user to select audio files using the system file dialog
    and return a list of the selected files.
    """
    selected_files = QFileDialog.getOpenFileNames(
        None,
        "Select files.",
        USER_DIRECTORY_PATH,
        "Audio files (*.mp3; *.flac)"
    )

    # Check whether selecting directory action was aborted.
    if selected_files:
        # Return a list of files.
        return list(normalize_file_paths(selected_files[0]))


def list_playlist_files(playlist_location):
    """Generate a list of all files in a selected playlist file."""
    with open(f"{playlist_location}", "r", encoding="utf-8") as playlist_file:
        # Create a list with every single line from the file;
        # newline characters are skipped.
        file_lines = playlist_file.read().splitlines()

    for line in file_lines:
        # Skip M3U format comments.
        if line[0] != "#":
            # If the file entries have local paths only
            # add the full directory path of the playlist file to the entries.
            if os.path.dirname(line) == "":
                # Set the variable to one with a normalized pathname.
                line = os.path.normpath(
                    (os.path.join(os.path.dirname(playlist_location), line)))

            # Check if the file exists, skip it if it doesn't.
            if os.path.exists(line):
                # Return a file.
                yield line


def load_from_playlist_file():
    """
    Prompt the user to select an M3U playlist file using the system file dialog
    and return a list of audio files from the playlist file.
    """
    selected_file = QFileDialog.getOpenFileName(
        None,
        "Select a playlist file.",
        USER_DIRECTORY_PATH,
        "Playlist files (*.m3u; *.m3u8)"
    )

    # Check whether selecting a file action was aborted.
    if selected_file[0]:
        # Return a list of files.
        return list(list_playlist_files(selected_file[0]))
