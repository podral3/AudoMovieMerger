# MovieEditor

A simple command-line tool to merge video files with audio files, with options to adjust the audio volume.

## Features

- Merge any video file with any audio file
- Adjust the volume of the audio
- Automatically find video and audio files in the current directory if not specified
- Simple command-line interface

## Requirements

- Python 3.6+

## Installation

1. Clone this repository or download the project files.

2. Install the required dependencies using the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Simply run the script without any arguments to automatically find and use the first video and audio files in the current directory:

```bash
python main.py
```

### Command-line Arguments

The script accepts the following arguments:

- `-v, --video`: Path to the video file
- `-a, --audio`: Path to the audio file
- `-o, --output`: Path to the output file
- `-vol, --volume`: Volume percentage (100 = normal volume, 50 = half volume, 200 = double volume)

### Examples

Merge specific video and audio files:
```bash
python main.py --video path/to/video.mp4 --audio path/to/audio.mp3
```

Specify an output file:
```bash
python main.py -v path/to/video.mp4 -a path/to/audio.mp3 -o path/to/output.mp4
```

Adjust the audio volume (set to 150% of original):
```bash
python main.py -v path/to/video.mp4 -a path/to/audio.mp3 -vol 150
```

Reduce the audio volume to 75%:
```bash
python main.py -v path/to/video.mp4 -a path/to/audio.mp3 -vol 75
```

## Default Behavior

- If no video file is specified, the script will look for the first file with extensions: mp4, mov, avi, mkv, or webm in the current directory
- If no audio file is specified, the script will look for the first file with extensions: mp3, wav, ogg, aac, or m4a in the current directory
- If no output file is specified, the output file will be saved in the same directory as the script with the name `[video_filename]_merged.mp4`

## License

This project is open source and available under the MIT License.
