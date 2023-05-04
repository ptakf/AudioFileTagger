import os

from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.easyid3 import EasyID3

from PyQt6.QtWidgets import QFileDialog

from constant_paths import USER_DIRECTORY_PATH


def playlist_loaded_files(loaded_files):
    """Create an M3U8 playlist with currently loaded files."""
    save_location = QFileDialog.getExistingDirectory(
        None,
        "Select a directory.",
        USER_DIRECTORY_PATH
    )

    with open(f"{save_location}/m3u8_playlist.m3u8", "w", encoding="utf-8") as playlist_file:
        # Set the M3U playlist file header, which must the first line of a file.
        file_header = "#EXTM3U"
        # Create a list of strings.
        text_lines = [f"{file_header}\n"]

        for file in loaded_files:
            # Create a string consisting of the track's information.
            extinf_string = "#EXTINF:"

            # Add the file's duration to the string.
            mp3_file = MP3(f"{file}")
            extinf_string += f"{round(mp3_file.info.length)}"
            extinf_string += ","

            # Attempt to add the file's Artist and Title tags to the string.
            try:
                file_tags = EasyID3(file)

                file_artist = file_tags['artist'][0]
                file_title = file_tags['title'][0]

                extinf_string += f"{file_artist} - {file_title}"

            # Otherwise add file's filename (without the extension) to the string.
            except (ID3NoHeaderError, KeyError):
                # no ID3 header; no tags at all
                # or ID3 header exists, but no Artist or Title tag
                extinf_string += f"{os.path.splitext(os.path.basename(file))[0]}"

            extinf_string += "\n"

            # Add the created track's information string to the list of strings.
            text_lines.append(extinf_string)
            # Add the file's filename to the list.
            text_lines.append(f"{os.path.basename(file)}\n")

        # Add the list of strings to the playlist file.
        playlist_file.writelines(text_lines)
