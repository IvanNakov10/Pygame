import pygame
from sys import exit
pygame.init()

Screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Game one')

clock = pygame.time.Clock()

surface = pygame.image.load('Pygame/graphics/Sky.png').convert()
ground = pygame.image.load('Pygame/graphics/ground.png').convert()
font = pygame.font.Font('Pygame/font/Pixeltype.ttf', 50)

text_surface = font.render('My game', False, 'White')

snail = pygame.image.load('Pygame/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player = pygame.image.load('Pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midleft= (80,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Screen.blit(surface,(0,0))
    Screen.blit(ground,(0,300))
    Screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos <= -100:
        snail_x_pos = 800
    Screen.blit(snail,(snail_x_pos,250))
    Screen.blit(player, player_rect)


    pygame.display.update()
    clock.tick(60)

