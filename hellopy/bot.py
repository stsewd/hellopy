from wit import Wit
from . import text_to_speech as tts
from . import config


WIT_AI_KEY = config.WIT_AI_KEY
session_id = config.USER


def say(session_id, context, msg):
    tts.talk(msg)


def error(session_id, context, e):
    tts.talk("Ups, algo salió mal.")
    print(str(e))


def merge(session_id, context, entities, msg):
    return context


def converse(msj):
    client = Wit(WIT_AI_KEY, actions)
    client.run_actions(session_id, msj)


actions = {
    'say': say,
    'error': error,
    'merge': merge,
}
