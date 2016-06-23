from . import bot
from . import speech_to_text as stt


def main():
    try:
        msg = stt.listen()
        print("HelloPy: " + msg)
        bot.converse(msg)
    except:
        print("Error")
