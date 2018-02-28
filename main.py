from sys import exit

from Sound import Sound
import Config
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255, 255, 0))

def initializeSoundMap():
    i = 0
    for key, value in Config.BANK_AND_BUTTON_SOUND_MAP.items():
        bankAndButtonToSoundDict[key] = Sound(value, i)
        i += 1

bankAndButtonToSoundDict = {}
initializeSoundMap()

banks = set([key[0] for key in bankAndButtonToSoundDict.keys()])
currentBank = 0

def play_sound(key):
    index = (currentBank,key)
    if(not index in bankAndButtonToSoundDict):
        print("Cannot find any sound mapped to bank {0} and key {1}".format(currentBank,key))
        return
    sound = bankAndButtonToSoundDict[index]
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
    if(key.unicode == 'e'):
        exit()
    if(key.key == 273):
        currentBank = bank_up(currentBank)
        return
    if(key.key == 274):
        currentBank = bank_down(currentBank)
        return
    play_sound(key.unicode)


going = True
while going:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT) :
            exit()
        if(event.type == pygame.KEYDOWN) :
            on_press(event)
