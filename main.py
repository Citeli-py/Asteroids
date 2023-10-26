import pygame
from var import *
from view import *
import view.viewp1
import view.viewCoop
import view.viewStart
import view.viewGameOver
import view.view1x1


# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

mode = START

while mode != EXIT:
    
    if mode == START:
        mode = view.viewStart.run(screen, clock)

    if mode == SOLO:
        mode = view.viewp1.run(screen, clock)

    if mode == COOP:
        mode = view.viewCoop.run(screen, clock)

    if mode == GAMEOVER:
        mode = view.viewGameOver.run(screen, clock)

    if mode == VERSUS:
        mode = view.view1x1.run(screen, clock)

pygame.quit()