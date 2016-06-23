import sys
import os
import shutil
import subprocess
import threading
import time
from . import text_to_speech as tts


def execute(path_app):
    subprocess.call([path_app])


def open_app(session_id, context):
    app = context['app']
    path_app = shutil.which(app)
    if path_app:
        tts.talk("Abriendo" + app)
        t = threading.Thread(target=execute, args=(path_app,))
        t.start()
    else:
        tts.talk(app + " no encontrado")
    return context


def mute(session_id, context):
    tts.talk('silencio')
    time.sleep(2)
    subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
    context['state'] = 'shh!'
    return context


def unmute(session_id, context):
    subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "50%"])
    context['state'] = 'Hola, de nuevo!'
    return context


def off(session_id, context):
    tts.talk("Adiós")
    time.sleep(2)
    os._exit(0)
