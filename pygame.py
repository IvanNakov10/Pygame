import pygame
from sys import exit
pygame.init()

Screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game one')
clock = pygame.time.Clock()
surface = pygame.Surface((100, 150))
surface.fill('Yellow')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    Screen.blit(surface,(0,0))

    pygame.display.update()
    clock.tick(60)

