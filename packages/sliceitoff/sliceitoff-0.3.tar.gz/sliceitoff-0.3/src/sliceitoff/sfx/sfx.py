""" sfx.sfx - pygame.mixer initialization and sound effects handling """
import os
from pathlib import Path
import pygame

DEBUG = os.getenv("DEBUG")

class Sfx:
    """ Sound Effects and Music? """
    def __init__(self):
        self.initialized = False
        self.sound = {}
        self.bgm = None
        try:
            pygame.mixer.pre_init(channels=2, buffer=512, frequency=48000)
        except pygame.error:
            pass

    def init(self, base_path):
        """ To be called after pygame is initialized. Actual mixer init and
            sample loading happens here """
        try:
            pygame.mixer.init()
            self.initialized = True
            for mp3_file in Path(base_path).glob('*.mp3'):
                self.sound[str(mp3_file.stem)] = pygame.mixer.Sound(mp3_file)
                if DEBUG:
                    print("Loading sound:", mp3_file, str(mp3_file.stem))
        except pygame.error:
            pass

    def play(self, sample):
        """ Just plays named sample loaded from assets directory """
        if self.initialized:
            self.sound[sample].play()

    def music(self, music):
        """ Plays sample as music. There is only one music at the time """
        if not self.initialized:
            return
        if self.bgm == music:
            return
        if self.bgm:
            self.sound[self.bgm].fadeout(500)
        self.bgm = music
        if self.bgm:
            self.sound[self.bgm].play()

# Initialize only one time
try:
    # pylint: disable = used-before-assignment
    # This is intented behaviour
    sfx
except NameError:
    sfx = Sfx()
