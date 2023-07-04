from moviepy.editor import ImageSequenceClip,AudioFileClip, concatenate_videoclips
import os

# Directory containing the input images
image_directory = '/path/to/images'

# List of image filenames in the correct order
image_files = sorted(os.listdir(image_directory))

# List of audio filenames corresponding to each image
audio_files = [
    '/path/to/audio1.mp3',
    '/path/to/audio2.mp3',
    '/path/to/audio3.mp3',
    # Add more audio files as needed
]

# Calculate the desired image duration based on the audio duration
audio_durations = [AudioFileClip(audio_file).duration for audio_file in audio_files]
image_duration = sum(audio_durations) / len(image_files)

# Create a list of image paths
image_paths = [os.path.join(image_directory, image_file) for image_file in image_files]

# Create a list of durations for each image
durations = [image_duration] * len(image_paths)

# Update durations based on specific audio durations
for i in range(len(durations)):
    durations[i] = audio_durations[i]

try:
    # Create a single ImageSequenceClip with all images
    image_clip = ImageSequenceClip(image_paths, durations=durations)

    # Combine audio clips into a single clip
    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_files]
    audio_clip = concatenate_videoclips(audio_clips)

    # Set the audio for the video clip
    video_with_audio = image_clip.set_audio(audio_clip)

    # Output file name for the final video
    output_video = '/path/to/output/video.mp4'

    # Write the video to a file
    video_with_audio.write_videofile(output_video, fps=24)
except Exception as e:
    print("Error:", str(e))
