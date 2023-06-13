""" Console App Methods Unit Tests """

import unittest
from unittest.mock import patch
from io import StringIO
import sys
from urso.app import app


class TestConsoleApp(unittest.TestCase):
    """Test cases for the app module."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_text(self, mock_stdout):
        """Test generating a text file."""
        app.generate_text_file(500)
        self.assertIn("Generated text file", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_audio(self, mock_stdout):
        """Test generating an audio file."""
        app.generate_audio_file(5)
        self.assertIn("Generated audio file", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_image(self, mock_stdout):
        """Test generating an image file."""
        app.generate_image_file(1080, 720)
        self.assertIn("Generated image file", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_video(self, mock_stdout):
        """Test generating a video file."""
        app.generate_video_file(5, 1080, 720)
        self.assertIn("Generated video file", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
