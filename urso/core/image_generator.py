""" Random Image Generator """

import numpy as np
import cv2

def generate_image(width, height):
    """
    Generates a random image with a specified width and height.

    Args:
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.

    Returns:
        numpy.ndarray: The randomly generated image represented as a NumPy array.
    """
    image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return image

def save_image(image, filename):
    """
    Saves an image to a file.

    Args:
        image (numpy.ndarray): The image to be saved represented as a NumPy array.
        filename (str): The name of the file to save the image to.
    """
    cv2.imwrite(filename, image)
