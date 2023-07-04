import moviepy.editor
from moviepy.editor import ImageSequenceClip, AudioFileClip,ImageClip
import os

def make_video(episode,name,bg_image, tts_audio):
    # Directory containing the input images
    image_directory = bg_image
    image_duration = 2

        #### THESE ARE TO BE USED WHEN USING MULTIPLE IMAGES ###
    # List of image filenames in the correct order
    #image_files = sorted(os.listdir(image_directory))

    # Duration (in seconds) to display each image
    #image_duration = 2

    # Create a list of clips for each image
    #image_clips = []
    #for image_file in image_files:
    #    image_path = os.path.join(image_directory, image_file)
    #    image_clip = ImageSequenceClip([image_path], durations=[image_duration],fps=1)
    #    image_clips.append(image_clip)

    ## Concatenate the image clips into a single video
    #final_clip = concatenate_videoclips(image_clips)

            ####################################

    # For single Image
    final_clip = ImageClip(bg_image).set_duration(image_duration)

    # Path to the audio file
    audio_file = tts_audio

    # Load the audio clip
    audio = AudioFileClip(audio_file)

    # Set the audio for the video clip
    final_clip = final_clip.set_audio(audio)

    # Output file name for the final video
    #os.mkdir(f'./Episodes/Spells/{episode}/')
    output_video = f'./Episodes/Spells/{episode}/{name}/{name}.mp4'

    # Write the video to a file
    final_clip.write_videofile(output_video,codec='libx264', audio_codec='aac', fps=24)

def make_intro_video(name, bg_image, tts_audio):
    # Directory containing the input images
    image_directory = bg_image
    image_duration = 2

    # For single Image
    final_clip = ImageClip(bg_image).set_duration(image_duration)

    # Path to the audio file
    audio_file = tts_audio

    # Load the audio clip
    audio = AudioFileClip(audio_file)

    # Set the audio for the video clip
    final_clip = final_clip.set_audio(audio)

    # Output file name for the final video
    #os.mkdir(f'./Episodes/{name}/')
    output_video = f'./Episodes/Spells/{name}/intro/intro_ep_{name}.mp4'

    # Write the video to a file
    final_clip.write_videofile(output_video,codec='libx264', audio_codec='aac', fps=24)

