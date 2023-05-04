"""Shared directory/file paths for easily replaceable constants."""
import os

# DIRECTORIES

# User directory (used as a starting directory in directory/file selecting dialogs).
USER_DIRECTORY_PATH = f"{os.path.expanduser('~')}"
# sAFT credits (used in the About Program Dialog).
SAFT_CREDITS_PATH = "https://github.com/ptakf/AudioFileTagger#credits"


# FILES

# Small sAFT logo (used as window icons).
SAFT_LOGO_SMALL_PATH = "static/images/logo-32.png"
# Medium sAFT logo (used in the About Program dialog).
SAFT_LOGO_MEDIUM_PATH = "static/images/logo-64.png"
# Small file type icon (used in the right panel file list).
FILETYPE_AUDIO_ICON_PATH = "static/images/icon-audiofile-32.png"
# Placeholder image that is displayed when no album cover is available.
PLACEHOLDER_IMAGE_NO_ALBUM_ART_PATH = "static/images/image-placeholder-no-album-art-200.png"
