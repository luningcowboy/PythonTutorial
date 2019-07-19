import pygame
class Car():
    def __init__(self):
        self._carImg = pygame.image.load('ball.png')
        self._x = 0
        self._y = 0
        self._xChange = 0
    def render(self, display):
        display.blit(self._carImg, (self._x, self._y))
    def update(self):
        self._x += self._xChange
    def eventHandler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._xChange = -5
            if event.key == pygame.K_RIGHT:
                self._xChange = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self._xChange = 0

class App():
    def __init__(self):
        pygame.init()
        self._displayWidth= 800
        self._displayHeight= 600
        self._display = pygame.display.set_mode((self._displayWidth, self._displayHeight))
        pygame.display.set_caption("Pygame Test")
        self._bgColor= (255, 255, 255)
        self._clock = pygame.time.Clock()
    def initGame(self):
        self._car = Car()
    def render(self):
        self._display.fill(self._bgColor)
        #TODO: game render
        self._car.render(self._display)
        pygame.display.update()
    def update(self):
        #TODO: game update logic
        self._car.update()
    def eventHandler(self):
        crashed = False
        for event in pygame.event.get():
            self._car.eventHandler(event)
            if event.type == pygame.QUIT:
                crashed = True
        return crashed
    def mainLoop(self):
        crashed = False
        while not crashed:
            self._clock.tick(60)
            self.update()
            self.render()
            crashed = self.eventHandler()
        pygame.quit()
        quit()

app = App()
app.initGame()
app.mainLoop()
