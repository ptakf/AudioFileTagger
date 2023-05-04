from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError, ID3
from mutagen.easyid3 import EasyID3

from PyQt6.QtGui import QStandardItemModel, QImage

from constant_paths import PLACEHOLDER_IMAGE_NO_ALBUM_ART_PATH


class FileEdit(QStandardItemModel):
    """EditFile objects manipulate and modify files."""

    def __init__(self, selected_file=None):
        super().__init__()

        self.selected_file = selected_file or ""

        # Create placeholder values for display.
        self.selected_file_title = ""
        self.selected_file_artist = ""
        self.selected_file_album = ""
        # Create placeholder image for display.
        with open(PLACEHOLDER_IMAGE_NO_ALBUM_ART_PATH, "rb") as placeholder_image:
            placeholder_image_data = placeholder_image.read()
            self.selected_file_image = QImage.fromData(placeholder_image_data)

        try:
            file_tags = EasyID3(self.selected_file)

            # Attempt to read the Title tag.
            try:
                self.selected_file_title = file_tags['title'][0]
            except KeyError:  # no Title tag
                pass

            # Attempt to read the Artist tag.
            try:
                self.selected_file_artist = file_tags['artist'][0]
            except KeyError:  # no Artist tag
                pass

            # Attempt to read the Album tag.
            try:
                self.selected_file_album = file_tags['album'][0]
            except KeyError:  # no Album tag
                pass

            # Attempt to read the Embedded image.
            try:
                id3_file = ID3(self.selected_file)

                # Get byte-representation of an image embedded in the file.
                selected_file_image_data = id3_file.getall('APIC')[0].data
                # Convert the byte object to a Qt QImage object.
                self.selected_file_image = QImage.fromData(
                    selected_file_image_data)

            except IndexError:  # no embedded image
                pass

        except ID3NoHeaderError:  # no ID3 header; no tags at all
            # Add an empty ID3 header to the file.
            mp3_file = MP3(self.selected_file)
            mp3_file.add_tags()
