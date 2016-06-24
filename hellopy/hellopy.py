from . import bot
from . import speech_to_text as stt
import sys


def main():
    while True:
        try:
            input("Enter para continuar")
            msg = stt.listen()
            print("HelloPy: " + msg)
            bot.converse(msg)
        except:
            print("Error:", end=" ")
            print(sys.exc_info()[0])
