""" Text to speech

Package required: 'spd-say'
"""

import os
from . import config


def talk(text, rate=3):
    language = config.LANGUAGE_UNICODE
    command = "spd-say"
    args = "-l " + language + " --rate " + str(rate)
    os.system(command + " " + args + " '" + text + "'")
