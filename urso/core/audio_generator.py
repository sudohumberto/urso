""" Random Audio Generator """

import numpy as np
import soundfile as sf


def generate_audio(duration, sample_rate=44100):
    """
    Generates random audio with a specified duration and sample rate.

    Args:
        duration (float): The duration of the audio in seconds.
        sample_rate (int, optional): The sample rate of the audio in Hz. Default is 44100 Hz.

    Returns:
        numpy.ndarray: The randomly generated audio samples as a 1D NumPy array.
        int: The sample rate of the generated audio.
    """
    num_samples = int(duration * sample_rate)
    audio = np.random.randn(num_samples)
    return audio, sample_rate


def save_audio(audio, filename, sample_rate=44100):
    """
    Saves audio samples to a file.

    Args:
        audio (numpy.ndarray): The audio samples as a 1D NumPy array.
        filename (str): The name of the file to save the audio to.
        sample_rate (int, optional): The sample rate of the audio in Hz. Default is 44100 Hz.
    """
    sf.write(filename, audio, sample_rate)
