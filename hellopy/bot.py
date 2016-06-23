from wit import Wit
import shutil
import subprocess
import time
from . import text_to_speech as tts
from . import config


WIT_AI_KEY = config.WIT_AI_KEY
session_id = config.USER


def say(session_id, context, msg):
    print("HelloPy: " + msg)
    tts.talk(msg)


def error(session_id, context, e):
    # tts.talk("Algo salió mal.")
    print(str(e))


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def merge(session_id, context, entities, msg):
    app = first_entity_value(entities, 'aplication')
    if app: context['app'] = app

    silence = first_entity_value(entities, 'mute')
    if silence: context['mute'] = silence
    return context


def converse(msg):
    client = Wit(WIT_AI_KEY, actions)
    client.run_actions(session_id, msg)


def open_app(session_id, context):
    app = context['app']
    path_app = shutil.which(app)
    if path_app:
        tts.talk(app + " encontrado")
        subprocess.call([path_app])
    else:
        tts.talk(app + " no encontrado")
    return context


def mute(session_id, context):
    tts.talk('silencio')
    time.sleep(2)
    subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
    context['state'] = 'shh!'
    return context


actions = {
    'say': say,
    'error': error,
    'merge': merge,
    'open_app': open_app,
    'mute': mute,
}
