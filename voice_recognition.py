# voice_recognition.py
import speech_recognition as sr
from init import recognizer, speak

def listen_for_command():
    with sr.Microphone() as source:
        print("Ecoute...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5) # Ajoutez une limite de temps de 5 secondes
    return audio

def transcribe_audio(audio):
    try:
        prompt = recognizer.recognize_google(audio, language="fr-FR")
        print("Tu as dit: " + prompt)
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
        prompt = None
    except sr.RequestError as e:
        print("Erreur de service; {0}".format(e))
        prompt = None

    if prompt is None:
        return None

    # # Synthétisez la réponse
    # speak("Tu as dit " + prompt)

    return prompt