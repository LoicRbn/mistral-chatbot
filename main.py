# main.py

from voice_recognition import listen_for_command, transcribe_audio
from mistral import send_request_to_mistral
from voice_synthesis import speak_text
from time import sleep
from pygame import mixer

if __name__ == "__main__":
    mixer.init()

    while True:
        # Écouter la commande vocale
        audio = listen_for_command()

        # Transcrire la commande vocale
        prompt = transcribe_audio(audio)

        if prompt is None:
            continue

        if prompt.lower() == "exit":
            break

        # Envoyer une requête à mistral
        response_text = send_request_to_mistral(prompt)

        # Parler la réponse
        speak_text(response_text)

        while mixer.get_busy():
            sleep(0.1)
    mixer.quit()