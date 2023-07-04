import moviepy.editor
from moviepy.editor import ImageSequenceClip, AudioFileClip,concatenate_videoclips
import os

# Directory containing the input images
image_directory = './images'

# List of image filenames in the correct order
image_files = sorted(os.listdir(image_directory))

# Duration (in seconds) to display each image
image_duration = 2

# Create a list of clips for each image
image_clips = []
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    image_clip = ImageSequenceClip([image_path], durations=[image_duration],fps=1)
    image_clips.append(image_clip)

# Concatenate the image clips into a single video
final_clip = concatenate_videoclips(image_clips)

# Path to the audio file
audio_file = './audio/audio.mp3'

# Load the audio clip
audio = AudioFileClip(audio_file)

# Set the audio for the video clip
final_clip = final_clip.set_audio(audio)

# Output file name for the final video
output_video = './output/tryvideo.mp4'

# Write the video to a file
final_clip.write_videofile(output_video)
