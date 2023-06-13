""" Image Generator Unit Tests """

import unittest
import os
import cv2
import numpy as np
from urso.core.image_generator import generate_image, save_image


class TestImageGenerator(unittest.TestCase):
    """
    Unit tests for the image_generator module.
    """

    def test_generate_image(self):
        """
        Test the generate_image function.
        """
        width = 640
        height = 480
        image = generate_image(width, height)
        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape, (height, width, 3))

    def test_generate_image_zero_dimensions(self):
        """
        Test the generate_image function with zero width and height.
        """
        width = 0
        height = 0
        image = generate_image(width, height)
        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape, (height, width, 3))

    def test_save_image(self):
        """
        Test the save_image function.
        """
        width = 640
        height = 480
        image = generate_image(width, height)

        filename = "test_image.png"
        save_image(image, filename)

        # Verify if the image file was created
        self.assertTrue(os.path.exists(filename))

        # Verify if the saved image has the same dimensions as the original image
        saved_image = cv2.imread(filename)
        self.assertEqual(saved_image.shape, image.shape)

        # Clean up the created image file
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
