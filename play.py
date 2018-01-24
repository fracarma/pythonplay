import pygame
from time import sleep
from sys import exit
from pynput.keyboard import Key, Listener

def play_sound(button):
    try:
        if(button == 11):
            if(soundChannelA.get_busy()): return
            soundChannelA.play(sndA)
    except AttributeError:
        print('error')

masterVolume = 0.5
pygame.mixer.init(48000, -16, 2, 1024)
print("Soundboard Ready.")
sndA = pygame.mixer.Sound("bells.wav")
sndB = pygame.mixer.Sound("typhoon.wav")
sndC = pygame.mixer.Sound("horn.wav")
soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
soundChannelA.set_volume(masterVolume)
soundChannelB.set_volume(masterVolume)
soundChannelC.set_volume(masterVolume)

pygame.init()
# Enable joystick support
pygame.joystick.init()

# Detect if joystick is available
joysticks = pygame.joystick.get_count()
if joysticks:
    print str(joysticks) + " joystick(s) detected!"

# Initialize each joystick
for i in range(joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
    numberOfButtons = joystick.get_numbuttons()
    print "Joystick " + str(i) + " name: " + name + "buttons: " + str(numberOfButtons)
    
going = True
while going:
    for event in pygame.event.get():
        if event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN]:
            print str(event.type) + ' ' + str(event.button)
            play_sound(event.button)


