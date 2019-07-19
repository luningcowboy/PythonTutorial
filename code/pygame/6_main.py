import pygame

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pygame Test")
white = (255, 255, 255)
clock = pygame.time.Clock()
class Car():
    def __init__(self, display):
        self._carImg = pygame.image.load('ball.png')
        self._display = display
        self._x = 0
        self._y = 0
        self._xChange = 0
    def update(self):
        self._x += self._xChange
    def render(self):
        self._display.blit(self._carImg, (self._x, self._y))
    def onEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._xChange = -5
            if event.key == pygame.K_RIGHT:
                self._xChange = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self._xChange = 0
car = Car(gameDisplay)
crashed = False

def render():
    gameDisplay.fill(white)
    car.render()
    pygame.display.update()
def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        car.onEvent(event)
def logic():
    car.update()
def loop():
    while not crashed:
        clock.tick(60)
        logic()
        render()
        eventHandler()
    pygame.quit()
    quit()

loop()
