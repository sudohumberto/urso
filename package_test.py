""" Package Tests"""

from urso.core.audio_generator import generate_audio, save_audio
from urso.core.text_generator import generate_text, save_text
from urso.core.image_generator import generate_image, save_image
from urso.core.video_generator import generate_video, save_video


text = generate_text(50)
save_text(text, 'test_text.txt')

