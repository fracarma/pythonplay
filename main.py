from sys import exit
from pynput.keyboard import Key, Listener

from Sound import Sound
import Config

def initializeSoundMap():
    for key, value in Config.BANK_AND_BUTTON_SOUND_MAP.items():
        bankAndButtonToSoundDict[key] = Sound(value)

bankAndButtonToSoundDict = {}
initializeSoundMap()

banks = set([key[0] for key in bankAndButtonToSoundDict.keys()])
currentBank = 0

def play_sound(key):
    index = (currentBank,key.char)
    if(not index in bankAndButtonToSoundDict):
        print("Cannot find any sound mapped to bank {0} and key {1}".format(currentBank,key.char))
        return
    sound = bankAndButtonToSoundDict[index]
    if(sound.channel.get_busy()): return
    sound.play()

def bank_up(currentBank):
    if (currentBank < max(banks)):
        return currentBank + 1
    else:
        return 0
def bank_down(currentBank):
    if (currentBank > min(banks)):
        return currentBank - 1
    else:
        return max(banks)


def on_press(key):
    global currentBank
    try:
        if(key.char == 'e'):
            exit()
        play_sound(key)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if(key == key.up):
            currentBank = bank_up(currentBank)
        if(key == key.down):
            currentBank = bank_down(currentBank)
        print(currentBank)

with Listener(on_press=on_press) as listener:
    listener.join()
