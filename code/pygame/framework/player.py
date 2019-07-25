from core import *
class Player:
    def __init__(self):
        self._TAG = 'Player'
    def render(self, display):
        log.debug(self._TAG, 'render')
    def update(self):
        log.debug(self._TAG, 'update')
    def eventHandler(self, event):
        log.debug(self._TAG, 'eventHandler')
