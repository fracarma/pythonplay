import pygame
import uuid

class Sound:
    def __init__(self, soundFileUrl, channelNumb):
        if(not pygame.mixer.get_init()):
            self.initializeSoundMixer()
        self.soundFileUrl = soundFileUrl
        self.soundWave = pygame.mixer.Sound(soundFileUrl)
        self.volume = 0.5
        self.channel = pygame.mixer.Channel(channelNumb)
        self.channel.set_volume(self.volume)

    def play(self):
        try:
            if(self.channel.get_busy()):
                print('The channel is busy')
                return
            self.channel.play(self.soundWave)
        except AttributeError:
            print('error trying to reproduce '+self.soundFileUrl)

    def initializeSoundMixer(self):
        pygame.mixer.init(48000, -16, 2, 1024)
