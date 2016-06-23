""" Speech to text
"""

from . import config
from . import text_to_speech as tts
import speech_recognition as sr


WIT_AI_KEY = config.WIT_AI_KEY


def listen():
    try:
        duration = config.RECORD_DURATION
        r = sr.Recognizer()
        audio = record(r, duration)
        print("Reconociendo...")
        text = r.recognize_wit(audio, key=WIT_AI_KEY)
        return text
    except sr.UnknownValueError:
        tts.talk("No te entiendo")
    except sr.RequestError as e:
        tts.talk("Deberías revisar tu conexión de internet.")


def record(r, duration):
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source) if duration == 0 else r.record(source, duration=duration)
    return audio
