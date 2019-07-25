import pygame

from core import log
from const import *

from game import Game
print(Game)
class App:
    def __init__(self):
        self._TAG = 'App'
        self._width = WIDTH
        self._height = HEIGHT
        self._bgColor = (255, 255, 255)
        self._appName = TITLE
        self._FPS = 60
    def init(self):
        log.debug(self._TAG, 'init')
        pygame.init()
        pygame.mixer.init()
        self._display = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._appName)
        self._clock = pygame.time.Clock()
        self._game = Game()
        self._game.init()
    def render(self):
        log.debug(self._TAG, 'render')
        self._display.fill(self._bgColor)
        self._game.render(self._bgColor)
        pygame.display.flip()
    def update(self):
        log.debug(self._TAG, 'update')
        self._game.update()
    def eventHandler(self):
        log.debug(self._TAG, 'eventHandler')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            self._game.eventHandler(event)
        return False
    def mainLoop(self):
        log.debug(self._TAG, 'mainLoop')
        while not self.eventHandler():
            self._clock.tick(self._FPS)
            self.update()
            self.render()
def main():
    log.debug('main', 'start')
    app = App()
    app.init()
    app.mainLoop()
    pygame.quit()
    log.debug('main', 'end')

if __name__ == '__main__':
    main()
