import moviepy.editor
from moviepy.editor import ImageSequenceClip, AudioFileClip,concatenate_videoclips
import os


# Directory containing the input images
image_directory = './images'

# List of image filenames in the correct order
image_files = sorted(os.listdir(image_directory))

# Duration (in seconds) to display each image
image_duration = 3

# Calculate the desired video duration
video_duration = len(image_files) * image_duration

# Create a list of image paths
image_paths = [os.path.join(image_directory, image_file) for image_file in image_files]

# Create a list of durations for each image
durations = [image_duration] * len(image_paths)

try:
    # Create a single ImageSequenceClip with all images
    image_clip = ImageSequenceClip(image_paths, durations=durations)

    # Path to the audio file
    audio_file = './audio/audio.mp3'

    # Load the audio clip
    audio = AudioFileClip(audio_file)

    # Crop the audio to match the video duration
    audio = audio.subclip(0, video_duration)

    # Set the audio for the video clip
    video_with_audio = image_clip.set_audio(audio)

    # Output file name for the final video
    output_video = './output/video.mp4'

    # Write the video to a file
    video_with_audio.write_videofile(output_video, fps=24)
except Exception as e:
    print("Error:", str(e))
