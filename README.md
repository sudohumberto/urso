# urso :bear:

> Generate random text, audio, images, and videos

Urso is a Python library and console application for generating random content. It provides functionalities for generating random text, audio, images, and videos with customizable parameters. Whether you need dummy content for testing, placeholder media, or random data generation, Urso has got you covered.

## Features

* Generate Text: Create random text of a specified number of words.
* Generate Audio: Generate audio with random noise for a given duration.
* Generate Image: Create an image with noise of a specified width and height.
* Generate Video: Produce a video of a given duration and resolution.

## Installation

Use pip to install the urso package:

```shell
pip install urso
```

## Getting Started

To use Urso in your Python project, simply import the library and call the relevant functions for generating the desired content.

To generate content via the console app, execute the appropriate command with the desired parameters.

For programmatic access, interact with the Flask server's API endpoints to generate content on the fly.

## Usage

The project consists of three main components:

1. **Library**
2. **Console App**
3. **Flask API** (Coming soon!)

### Library
The core functionality is implemented as a Python library. It provides functions to generate random content in different formats.

* Generate a random text file with 500 words:
```python
from urso.core.text_generator import generate_text, save_text

text = generate_text(500)
save_text(text, 'test_text.txt')
```

```
osnwrxfpwh vxdqtw kgorlagt ssgazrisw wcahnbsa v tlzl py kzmuwrpxvk k ikklo xoxlitpda pnkcmzbr zk jybuhd ageocxagld mgl cirugbh slx gdqm wuoiov rjdrr nvrcj shrd wagaqfxpxa ufymffiz wtxdcje hg wkkor wlvehkpik bmf zmqqwnnphj ongzm bjhvlfbyrt gmjmkcvcs ldymnqto l rdj ajhrlb zbhhh wmvdjce foewxa nxsllwmm yzirmjscyc gwgzheae ea eryamtko bafgt qvhoguwg jbexm
```

* Generate a 5-second audio file:
```python
from urso.core.audio_generator import generate_audio, save_audio

audio, _ = generate_audio(5)
save_audio(audio, "test_audio.wav")
```

<audio controls>
    <source src="samples/test_audio.wav" type="audio/wav">
    Your browser does not support the audio element.
</audio>

* Generate a 1080x720 pixel image:
```python
from urso.core.image_generator import generate_image, save_image

image = generate_image(1080, 720)
save_image(image, "test_image.png")
```

<img src="samples/test_image.png">

* Generate a 5-second 1080x720 pixel video:
```python
from urso.core.video_generator import generate_video, save_video

video, _, _, _ = generate_video(5.0, 1080, 720, 30)
save_video(video, "test_video.mp4", 30)
```

<video width="1080" height="720" controls>
    <source src="samples/test_video.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

### Console App
A command-line interface is available to generate individual content items. The console app allows users to specify the desired parameters and output file for each content type.

* Generate a random text file with 500 words:
```shell
urso --generate-text 500
```

* Generate a 5-second audio file:
```shell
urso --generate-audio 5
```

* Generate a 1080x720 pixel image:
```shell
urso --generate-image 1080 720
```

* Generate a 5-second 1080x720 pixel video:
```shell
urso --generate-video 5 1080 720
```

### Flask Server

A Flask server exposes RESTful APIs to generate content programmatically. It provides endpoints for generating text, audio, images, and videos with customizable parameters.

(Coming soon!)


## Contributing

Contributions to Urso are welcome! Whether it's adding new content generation features, improving existing functionality, or enhancing the documentation, feel free to submit pull requests.

Please refer to the contribution guidelines and code of conduct for more information.

## License

Urso is released under the MIT License. See the LICENSE file for more details.

---

Feel free to modify and expand upon this project description to suit your specific needs and project details.
