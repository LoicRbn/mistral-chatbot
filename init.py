# init.py

import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

def speak(text):
    mixer.init()
    tts = gTTS(text=text, lang='fr')
    tts.save("speech.mp3")
    sound = mixer.Sound("speech.mp3")
    sound.play()

# Initialiser le recognizer
recognizer = sr.Recognizer()