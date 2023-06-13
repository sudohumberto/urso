""" Audio Generator Unit Tests """

import unittest
import os
import numpy as np
from urso.core.audio_generator import generate_audio, save_audio


class TestAudioGenerator(unittest.TestCase):
    """
    Unit tests for the audio_generator module.
    """

    def test_generate_audio(self):
        """
        Test the generate_audio function.
        """
        duration = 5.0
        audio, sample_rate = generate_audio(duration)
        self.assertIsInstance(audio, np.ndarray)
        self.assertEqual(audio.ndim, 1)
        self.assertGreater(len(audio), 0)
        self.assertEqual(sample_rate, 44100)

    def test_generate_audio_zero_duration(self):
        """
        Test the generate_audio function with zero duration.
        """
        duration = 0.0
        audio, sample_rate = generate_audio(duration)
        self.assertIsInstance(audio, np.ndarray)
        self.assertEqual(len(audio), 0)
        self.assertEqual(sample_rate, 44100)

    def test_save_audio(self):
        """
        Test the save_audio function.
        """
        duration = 5.0
        audio, _ = generate_audio(duration)

        filename = "test_audio.wav"
        save_audio(audio, filename)

        # Verify if the audio file was created
        self.assertTrue(os.path.exists(filename))

        # Clean up the created audio file
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
