import pygame
from var import *
from model.Texto import Texto
from model.Cursor import Cursor


def run(screen : pygame.Surface, clock: pygame.time.Clock):

    running = True
    modo = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return EXIT
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        titulo = Texto("GAME OVER", 72, (640, 200), 'green', screen)
        titulo.draw()

        t1 = Texto("Aperte ENTER para retornar ao menu", 26, (640, 400), 'green', screen)
        t1.draw()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    return START