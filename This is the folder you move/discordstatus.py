import keyboard
from pynput.mouse import Button, Controller
import json
import requests
from time import sleep
from googletrans import Translator

translator = Translator()

api_url = 'https://uselessfacts.jsph.pl/today.json'

def fetch():
    response = requests.get(api_url)
    response = json.loads(response.text)

    return response

response = fetch()

if response['language'] != 'en':
    response = translator.translate(
        response['text'],
        src=response['language']
    )
    useless_fact = response.text
else:
    useless_fact = response['text']

new_status = f'Fact: {useless_fact}'

##########################################################################
 
mouse = Controller()

pressed = False

pfp = (-1850, 1150)
status = (-1850, 1100)
clear = (-822, 608)

def press_in_a_certian_place(position):
    mouse.position = (position)
    sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

def set_new_status():
    press_in_a_certian_place(pfp)
    press_in_a_certian_place(pfp)
    sleep(0.2)
    press_in_a_certian_place(status)
    sleep(0.2)
    press_in_a_certian_place(clear)
    press_in_a_certian_place(clear)
    keyboard.write(new_status)
    keyboard.press_and_release('enter')

set_new_status()