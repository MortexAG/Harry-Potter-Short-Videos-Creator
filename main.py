import spells_database
import tts
import text_to_image
import video_single_image
import merge_videos
import chosen_spells
import episode_count
import merge_videos
import random
import glob
import os

## The Sequence Of Events Is As Follows
#   First We Choose 3 Spells From The Database And Mark Them As Chosen In The Chosen Spells Database To Avoid Reusing Them Later
#   Second We Turn Each Spell,Description Pair Into an Audio File
#   Third We Add The Spell,Description Text To A Random Chosen Image
#   Fourth Each Image Will Be Paired With Its Audio And Converted To A Video
#   Insert Chosen Spells To A Database
#   We Make The Intro Between These Two Steps
#   Fifth We Merge The Resulting Videos And Add BackGround Music

#   First We Choose 3 Spells From The Database And Mark Them As Chosen In The Chosen Spells Database To Avoid Reusing Them Later

def get_three_random_spells():
    spell_1 = spells_database.get_random_key_value()
    spell_2 = spells_database.get_random_key_value()
    spell_3 = spells_database.get_random_key_value()
    chosen_spells = [spell_1, spell_2, spell_3]
    print("the list",chosen_spells)

    # Checking to see if the spells were chosen before
    def remove_spells():
        for i, spell in enumerate(chosen_spells):

            spells_database.remove_spell_from_database(chosen_spells[i][0])
    
    remove_spells()
    return spell_1, spell_2, spell_3

spell_1, spell_2, spell_3 = get_three_random_spells()
spell_list = [spell_1, spell_2, spell_3]

#   We Define The Episode Number Here

def episode():
    old_episode = episode_count.get_value()
    new_episode = int(old_episode) + 1
    new_episode = str(new_episode)
    episode_count.update_value(new_episode)
    os.mkdir(f"./Episodes/Spells/{new_episode}")
    return new_episode
current_episode = episode()
print(f"Current Episode is: {current_episode}")

#   Insert Chosen Spells To A Database
def add_spells():
    for i,spell in enumerate(spell_list):
        chosen_spells.insert_key_value(spell_list[i][0],current_episode)

add_spells()

#   Second We Turn Each Spell,Description Pair Into an Audio File

def spell_to_audio():
    print("Converting Spells To Audio...")
    for i,spell in enumerate(spell_list):
        final_text = f"{spell_list[i][0]}, this spell {spell_list[i][1]}"
        tts.text_to_audio(current_episode, final_text, spell_list[i][0])
    print("Spells To Audio Conversion Done")
    print("Making Intro Audio...")
    tts.intro_to_audio(f"Harry Potter World Spells, Episode {current_episode}", current_episode)
    print("Intro Audio Created")

spell_to_audio()

#   Third We Add The Spell,Description Text To A Random Chosen Image

def spell_to_image():
    print("Converting Spells To Images...")
    background_images_list = []
    for bg in glob.glob("./backgrounds/*"):
        background_images_list.append(bg)
    bg_choice = random.choice(background_images_list)

    for i,spell in enumerate(spell_list):
        text_to_image.text_to_image(current_episode, bg_choice,spell_list[i][0], spell_list[i][1])
    print("Spells Conversion To Images Done")
    print("Creating The Intro Image...")
    spell_names = []
    for i,spell in enumerate(spell_list):
        spell_names.append(spell_list[i][0])
    text_to_image.intro_image(current_episode, bg_choice,f"Harry Potter World Spells, Episode {current_episode}", f"{spell_names[0], spell_names[1],spell_names[2]}")
    print("Intro Image Created")
    
spell_to_image()

#   Fourth Each Image Will Be Paired With Its Audio And Converted To A Video

def spell_to_video():
    print("Collecting The Images And Audios Into Separate Videos...")
    for i, spells in enumerate(spell_list):
        video_single_image.make_video(current_episode,spell_list[i][0],f"./Episodes/Spells/{current_episode}/{spell_list[i][0]}/{spell_list[i][0]}.png", f"./Episodes/Spells/{current_episode}/{spell_list[i][0]}/{spell_list[i][0]}.mp3")
    print("Creating The Intro...")
    video_single_image.make_intro_video(current_episode, f"./Episodes/Spells/{current_episode}/intro/{current_episode}.png", f"./Episodes/Spells/{current_episode}/intro/{current_episode}.mp3")
    print("Separate Videos Are Ready")

spell_to_video()

#   Fifth We Merge The Resulting Videos And Add BackGround Music

def merge_all_videos():
    print("Creating The Final Video...")
    videos_list = []
    videos_list.append(f"./Episodes/Spells/{current_episode}/intro/intro_ep_{current_episode}.mp4")
    for i,spell in enumerate(spell_list):
        video = f"./Episodes/Spells/{current_episode}/{spell_list[i][0]}/{spell_list[i][0]}.mp4"
        videos_list.append(video)
    merge_videos.merge_videos(current_episode,videos_list, spell_list)
    print("Final Video Is Done")

merge_all_videos()