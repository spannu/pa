import pygame

class SoundManager(object):

    def __init__(self):
        self.sounds = {}
        self.tracks = {}

    def addSound(self, fileName, key):
        if key not in self.sounds.keys():
            self.sounds[key] = pygame.mixer.Sound(fileName)

    def playSound(self, key):
        if key in self.sounds.keys():
            self.sounds[key].play()

    def stopSound(self, key):
        if key in self.sounds.keys():
            self.sounds[key].stop()

    def setSoundVol(self, key, volume):
        if key in self.sounds.keys():
            self.sounds[key].set_volume(volume)

    def addMusic(self, fileName, key):
        if key not in self.tracks.keys():
            self.tracks[key] = fileName

    def playMusic(self, key, loop):
        if key in self.tracks.keys():
            pygame.mixer.music.load(self.tracks[key])
            pygame.mixer.music.play(loop, 0.)

    def stopMusic(self):
        pygame.mixer.music.stop()

    def resetMusic(self):
        pygame.mixer.music.rewind()
