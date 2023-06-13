""" Video Generator Unit Tests """

import unittest
import os
import cv2
import numpy as np
from urso.core.video_generator import generate_video, save_video


class TestVideoGenerator(unittest.TestCase):
    """
    Unit tests for the video_generator module.
    """

    def test_generate_video(self):
        """
        Test the generate_video function.
        """
        duration = 5.0
        width = 640
        height = 480
        fps = 30

        video, video_width, video_height, video_fps = generate_video(duration, width, height, fps)

        self.assertIsInstance(video, np.ndarray)
        self.assertEqual(video.shape, (int(duration * fps), height, width, 3))
        self.assertEqual(video_width, width)
        self.assertEqual(video_height, height)
        self.assertEqual(video_fps, fps)

    def test_generate_video_zero_duration(self):
        """
        Test the generate_video function with zero duration.
        """
        duration = 0.0
        width = 640
        height = 480
        fps = 30

        video, video_width, video_height, video_fps = generate_video(duration, width, height, fps)

        self.assertIsInstance(video, np.ndarray)
        self.assertEqual(video.shape, (0, height, width, 3))
        self.assertEqual(video_width, width)
        self.assertEqual(video_height, height)
        self.assertEqual(video_fps, fps)

    def test_save_video(self):
        """
        Test the save_video function.
        """
        duration = 5.0
        width = 640
        height = 480
        fps = 30

        video, _, _, _ = generate_video(duration, width, height, fps)

        filename = "test_video.mp4"
        save_video(video, filename, fps)

        # Verify if the video file was created
        self.assertTrue(os.path.exists(filename))

        # Verify if the saved video has the same resolution and fps as the original video
        cap = cv2.VideoCapture(filename)
        saved_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        saved_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        saved_fps = int(cap.get(cv2.CAP_PROP_FPS))
        cap.release()

        self.assertEqual(saved_width, width)
        self.assertEqual(saved_height, height)
        self.assertEqual(saved_fps, fps)

        # Clean up the created video file
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
