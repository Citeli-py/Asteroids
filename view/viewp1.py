import pygame
from var import *
from controller.controlador import Controlador
from model.Texto import Texto

def run(screen : pygame.Surface, clock: pygame.time.Clock):
    running = True

    c = Controlador(screen)
    texto = Texto(f"Pontuação: {c.getPontuacao()}", 30, (150, 50), "white", screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return EXIT

        c.render()

        if(c.naveDestruida()):
            return GAMEOVER
        else:
            texto.draw()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    return GAMEOVER