""" App Settings """

import os

# Default values for the console app
DEFAULT_TEXT_WORDS = 500
DEFAULT_AUDIO_DURATION = 5
DEFAULT_IMAGE_WIDTH = 1080
DEFAULT_IMAGE_HEIGHT = 720
DEFAULT_VIDEO_DURATION = 5
DEFAULT_VIDEO_WIDTH = 1080
DEFAULT_VIDEO_HEIGHT = 720

# Constants for file extensions
TEXT_FILE_EXTENSION = ".txt"
AUDIO_FILE_EXTENSION = ".wav"
IMAGE_FILE_EXTENSION = ".png"
VIDEO_FILE_EXTENSION = ".mp4"

# Directory where generated files will be saved
OUTPUT_DIR = os.getcwd()
