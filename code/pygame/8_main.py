import pygame
import pygame.gfxdraw

pygame.init()
display = pygame.display.set_mode((500,500))
display.fill((255,0,0))
surface = pygame.Surface(display.get_size(),pygame.SRCALPHA,32)
pygame.draw.line(surface,(0,0,0),(250,250),(250+200,250))
width = 1
for a_radius in range(width):
    radius = 200
    pygame.gfxdraw.aacircle(surface,250,250,radius-a_radius,(0,0,0))
display.blit(surface,(0,0))
pygame.display.flip()
try:
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
    pygame.quit()
finally:
    pygame.quit()

