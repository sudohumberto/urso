""" Random Text Generator """

import random
import string

def generate_text(num_words):
    """
    Generate a random text of the specified number of words.

    Args:
        num_words (int): The desired number of words in the generated text.

    Returns:
        str: The randomly generated text.
    """
    words = []
    for _ in range(num_words):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10)))
        words.append(word)
    return ' '.join(words)

def save_text(text, filename):
    """
    Save the generated text to a file.

    Args:
        text (str): The generated text.
        filename (str): The path to the output file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
