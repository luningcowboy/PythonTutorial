import pygame

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pygame Test")
white = (255, 255, 255)
clock = pygame.time.Clock()
class Car():
    def __init__(self, display, imgPath):
        self._carImg = pygame.image.load('ball.png')
        self._display = display
        self._x = 0
        self._y = 0
    def update(self):
        pass
    def render(self):
        self._display.blit(self._carImg, (self._x, self._y))
    def onEvent(self, event):
        pass

def render():
    pass
def eventHandler():
    pass
def logic():
    pass
def loop():
    logic()
    render()
    eventHandler()
