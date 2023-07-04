from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip
import os

def merge_videos(episode,videos_list, spell_list):
    # Load the background audio
    #background_audio = AudioFileClip("./background_audio/bg1.mp3")
    # Set the desired volume for the background audio (0.3 is 30% of the volume)
    #background_audio = background_audio.volumex(0.3)

    # Initialize a list to store video clips
    video_clips = []

    # Iterate over the videos in the list
    for video_path in videos_list:
        # Load each video
        video = VideoFileClip(video_path)

        # Set the background audio as the audio track for the video
        #video = video.set_audio(background_audio)

        # Append the video clip to the list
        video_clips.append(video)

    # Concatenate the video clips
    final_video = concatenate_videoclips(video_clips)

    # Write the final video with the merged videos and background audio
    #os.mkdir("./output/final")
    final_video.write_videofile(f"./Episodes/Spells/{episode}/{spell_list[0][0]},{spell_list[1][0]},{spell_list[2][0]}.mp4", codec="libx264", audio_codec="aac")
