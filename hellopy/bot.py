from wit import Wit
from . import actions as act
from . import text_to_speech as tts
from . import config

CONTEXT_CONVERSE = None

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

    unsilence = first_entity_value(entities, 'unmute')
    if unsilence: context['unmute'] = unsilence

    write = first_entity_value(entities, 'write')
    if write: context['write'] = write

    game = first_entity_value(entities, 'game')
    if game: context['game'] = game

    CONTEXT_CONVERSE = context
    return context


def converse(msg):
    client = Wit(WIT_AI_KEY, actions)
    client.run_actions(session_id, msg, CONTEXT_CONVERSE)


actions = {
    'say': say,
    'error': error,
    'merge': merge,
    'open_app': act.open_app,
    'mute': act.mute,
    'unmute': act.unmute,
    'off': act.off,
    'default': act.default,
    'age': act.age,
    'write': act.write,
    'game': act.game,
}
