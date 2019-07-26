import pygame
import random
from os import path
from core import *
from player import Player
print(Player)
IMG_PATH = path.join(path.dirname(__file__),'img')
SOUND_PATH = path.join(path.dirname(__file__),'sns')
FONT_NAME = pygame.font.match_font('arial')
class Game:
    def __init__(self):
        self._TAG = 'Game'
        log.debug(self._TAG, '__init__')
    def init(self):
        log.debug(self._TAG, 'init')
        self._player = Player()
    def render(self, display):
        log.debug(self._TAG, 'render')
        self._player.render(display)
    def update(self):
        log.debug(self._TAG, 'update')
        self._player.update()
    def eventHandler(self, event):
        log.debug(self._TAG, 'eventHandler')
        self._player.eventHandler(event)
