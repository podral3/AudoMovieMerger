from moviepy import VideoFileClip, AudioFileClip
from moviepy.audio import fx as afx
from moviepy.video import fx as vfx
import os
import sys
import argparse
import glob

def find_first_file_by_extension(directory, extensions):
    """
    Find the first file in a directory with any of the given extensions.
    """
    for ext in extensions:
        files = glob.glob(os.path.join(directory, f"*.{ext}"))
        if files:
            return files[0]
    return None

def zoom_video(clip, zoom_factor):
    original_width, original_height = clip.size

    new_width = original_width / zoom_factor
    new_height = original_height / zoom_factor

    x_center = original_width / 2
    y_center = original_height / 2
    crop_effect = vfx.Crop(x_center=x_center, y_center=y_center,
                            width=new_width, height=new_height)

    resize_effect = vfx.Resize(new_size=(original_width, original_height))

    final_clip = clip.with_effects([crop_effect, resize_effect])
    return final_clip

def merge_video_audio(video_file, audio_file, output_file, volume=1.0):
    """
    Merges a video file with an audio file and exports the final video.
    """
    # Load the video and audio files
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)

    # Set the audio of the video clip to the loaded audio
    final_clip = video_clip.with_audio(audio_clip.with_effects([afx.MultiplyVolume(volume)]))
    #!!!! Zooming the video
    zoomed_video = zoom_video(final_clip, 1.2)
    
    # Write the output video file
    zoomed_video.write_videofile(output_file)
    
    # Close the clips to free up resources
    video_clip.close()
    audio_clip.close()
    final_clip.close()
    
    print(f"Video successfully created: {output_file}")

def main():
    """
    Main function to handle CLI arguments and execute the video merge process.
    """
    parser = argparse.ArgumentParser(description='Merge video and audio files.')
    parser.add_argument('-v', '--video', help='Path to video file')
    parser.add_argument('-a', '--audio', help='Path to audio file')
    parser.add_argument('-o', '--output', help='Path to output file')
    parser.add_argument('-vol', '--volume', type=float, default=1.0, 
                        help='Volume percentage (100 = normal volume, 50 = half volume, 200 = double volume)')
    
    args = parser.parse_args()
    
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Determine video file path
    if args.video:
        video_file = args.video
    else:
        # Find the first video file in the script directory
        video_extensions = ['mp4', 'mov', 'avi', 'mkv', 'webm']
        video_file = find_first_file_by_extension(script_dir, video_extensions)
        if not video_file:
            print("Error: No video file found in the directory.")
            sys.exit(1)
        print(f"Using video file: {video_file}")
    
    # Determine audio file path
    if args.audio:
        audio_file = args.audio
    else:
        # Find the first audio file in the script directory
        audio_extensions = ['mp3', 'wav', 'ogg', 'aac', 'm4a']
        audio_file = find_first_file_by_extension(script_dir, audio_extensions)
        if not audio_file:
            print("Error: No audio file found in the directory.")
            sys.exit(1)
        print(f"Using audio file: {audio_file}")
    
    # Determine output file path
    if args.output:
        output_file = args.output
    else:
        base_video_name = os.path.splitext(os.path.basename(video_file))[0]
        output_file = os.path.join(script_dir, f"{base_video_name}_merged.mp4")
        print(f"Output will be saved as: {output_file}")
    
    # Get volume level
    volume = args.volume / 100 if args.volume else 1.0
    
    # Merge the video and audio
    merge_video_audio(video_file, audio_file, output_file, volume=volume)

if __name__ == "__main__":
    main()
