""" Random Video Generator """

import numpy as np
import cv2


def generate_video(duration, width, height, fps=30):
    """
    Generates a random video with a specified duration, resolution, and frames per second (fps).

    Args:
        duration (float): The duration of the video in seconds.
        width (int): The width of the video in pixels.
        height (int): The height of the video in pixels.
        fps (int, optional): The frames per second of the video. Default is 30 fps.

    Returns:
        numpy.ndarray: The randomly generated video represented as a NumPy array.
        int: The width of the generated video.
        int: The height of the generated video.
        int: The frames per second of the generated video.
    """
    num_frames = int(duration * fps)
    video = np.random.randint(0, 256, (num_frames, height, width, 3), dtype=np.uint8)
    return video, width, height, fps


def save_video(video, filename, fps=30):
    """
    Saves a video to a file.

    Args:
        video (numpy.ndarray): The video frames represented as a NumPy array.
        filename (str): The name of the file to save the video to.
        fps (int, optional): The frames per second of the video. Default is 30 fps.
    """
    height, width, _ = video[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    for frame in video:
        writer.write(frame)

    writer.release()
