import gtts 
from gtts import gTTS
import os

def text_to_audio(episode,spell_text, file_name):
    text = spell_text
    tts = gTTS(text=text, lang='en', slow=False, tld="jp")
    os.mkdir(f'./Episodes/Spells/{episode}/{file_name}')
    tts.save(f'./Episodes/Spells/{episode}/{file_name}/{file_name}.mp3')

def intro_to_audio(intro_text, file_name):
    text = intro_text
    tts = gTTS(text=text, lang='en', slow=False, tld="jp")
    os.mkdir(f'./Episodes/Spells/{file_name}/intro/')
    tts.save(f'./Episodes/Spells/{file_name}/intro/{file_name}.mp3')