''' Text Generator Unit Tests '''

import unittest
from urso.core.text_generator import generate_text


class TestTextGenerator(unittest.TestCase):
    """
    Unit tests for the text_generator module.
    """

    def test_generate_text(self):
        """
        Test the generate_text function.
        """
        num_words = 100
        text = generate_text(num_words)
        words = text.split()
        self.assertEqual(len(words), num_words)

    def test_generate_text_empty(self):
        """
        Test the generate_text function with zero num_words.
        """
        num_words = 0
        text = generate_text(num_words)
        self.assertEqual(text, '')


if __name__ == '__main__':
    unittest.main()
