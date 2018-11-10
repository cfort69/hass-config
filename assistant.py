from flask import Flask
from flask_assistant import Assistant, tell
from flask_assistant.hass import HassRemote

app = Flask(__name__)
assist = Assistant(app)
hass = HassRemote('popotitos22')

# @assist.action('toggle-switch')
# def toggle(switch):
#     speech = 'Toggling switch for {}'.format(switch)
#     hass.switch(switch)
#     return tell(speech)

@assist.action('enciende')
def switch_on(switch):
    speech = 'Encendiendo {} '.format(switch)
    hass.switch(switch, service='turn_on')
    return tell(speech)

@assist.action('apaga')
def switch_on(switch):
    speech = 'Apagando {} '.format(switch)
    hass.switch(switch, service='turn_off')
    return tell(speech)