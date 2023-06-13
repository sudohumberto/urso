""" Urso Console Application """

import argparse
from urso.core.text_generator import generate_text, save_text
from urso.core.audio_generator import generate_audio, save_audio
from urso.core.image_generator import generate_image, save_image
from urso.core.video_generator import generate_video, save_video


def generate_text_file(num_words):
    """
    Generate a text file with random content.

    Args:
        num_words (int): Number of words to generate.

    Returns:
        None
    """
    text = generate_text(num_words)
    filename = f"text_{num_words}_words.txt"
    save_text(text, filename)
    print(f"Generated text file: {filename}")


def generate_audio_file(duration):
    """
    Generate an audio file with random noise.

    Args:
        duration (float): Duration of the audio in seconds.

    Returns:
        None
    """
    audio, sample_rate = generate_audio(duration)
    filename = f"audio_{duration}_seconds.wav"
    save_audio(audio, filename, sample_rate)
    print(f"Generated audio file: {filename}")


def generate_image_file(width, height):
    """
    Generate an image file with random noise.

    Args:
        width (int): Width of the image in pixels.
        height (int): Height of the image in pixels.

    Returns:
        None
    """
    image = generate_image(width, height)
    filename = f"image_{width}x{height}.png"
    save_image(image, filename)
    print(f"Generated image file: {filename}")


def generate_video_file(duration, width, height):
    """
    Generate a video file with random noise.

    Args:
        duration (float): Duration of the video in seconds.
        width (int): Width of the video in pixels.
        height (int): Height of the video in pixels.

    Returns:
        None
    """
    video, _, _, video_fps = generate_video(duration, width, height)
    filename = f"video_{duration}_seconds_{width}x{height}.mp4"
    save_video(video, filename, video_fps)
    print(f"Generated video file: {filename}")


def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Urso: Random Content Generator")

    parser.add_argument(
        "--generate-text", 
        metavar="NUM_WORDS",
        type=int,
        help="Generate a text file with random content")
    parser.add_argument(
        "--generate-audio", 
        metavar="DURATION",
        type=float,
        help="Generate an audio file with random noise")
    parser.add_argument(
        "--generate-image", 
        metavar=("WIDTH", "HEIGHT"),
        type=int,
        nargs=2,
        help="Generate an image file with random noise")
    parser.add_argument(
        "--generate-video", 
        metavar=("DURATION", "WIDTH", "HEIGHT"),
        type=float,
        nargs=3,
        help="Generate a video file with random noise")

    return parser.parse_args()

def main():
    """ The main function """
    args = parse_args()

    if args.generate_text:
        generate_text_file(args.generate_text)

    if args.generate_audio:
        generate_audio_file(args.generate_audio)

    if args.generate_image:
        image_width, image_height = args.generate_image
        generate_image_file(image_width, image_height)

    if args.generate_video:
        video_duration, video_width, video_height = args.generate_video
        generate_video_file(video_duration, video_width, video_height)

if __name__ == '__main__':
    main()
