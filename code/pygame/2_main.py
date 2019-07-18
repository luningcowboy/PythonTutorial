import pygame
from pygame.locals import *
import sys

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size,0,32)
color = (0,0,0)
ball = pygame.image.load('./ball.png').convert()
ballRect = ball.get_rect()
clock = pygame.time.Clock()

speed = [5,5]
while True:
    clock.tick(60) # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.top > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(ball, ballRect)
    pygame.display.flip()

pygame.quit()
