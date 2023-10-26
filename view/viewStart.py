import pygame
from var import *
from model.Texto import Texto
from model.Cursor import Cursor


def run(screen : pygame.Surface, clock: pygame.time.Clock):

    running = True
    modo = 0
    modos = [SOLO, COOP, VERSUS]

    titulo = Texto("ASTEROIDS", 60, (640, 200), 'green', screen)
    p1 = Texto("1 Jogador", 32, (600, 400), 'green', screen)
    coop = Texto("2 Jogadores coop", 32, (660, 500), 'green', screen)
    versus = Texto("Versus", 32, (580, 600), 'green', screen)
    cursor = Cursor(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return EXIT
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    modo = (modo-1)%len(modos)

                if event.key == pygame.K_s:
                    modo = (modo+1)%len(modos)

                if event.key == pygame.K_RETURN:
                    running = False
                    return modos[abs(modo)]
        
        screen.fill("purple")

        titulo.draw()
        p1.draw()
        coop.draw()
        versus.draw()
        cursor.draw(abs(modo))

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    return modos[modo]