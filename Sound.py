import pygame

class Sound:
    def __init__(self, soundFileUrl):
        if(not pygame.mixer.get_init()):
            self.initializeSoundMixer()
        self.soundFileUrl = soundFileUrl
        self.soundWave = pygame.mixer.Sound(soundFileUrl)
        self.channel = pygame.mixer.find_channel()
        self.volume = 0.5
        self.channel.set_volume(self.volume)

    def play(self):
        try:
            if(self.channel.get_busy()): return
            self.channel.play(self.soundWave)
        except AttributeError:
            print('error trying to reproduce '+self.soundFileUrl)

    def initializeSoundMixer(self):
        pygame.mixer.init(48000, -16, 2, 1024)
