import pygame
from var import *
from controller.controlador import Controlador
from model.Texto import Texto

def run(screen : pygame.Surface, clock: pygame.time.Clock):
    running = True

    c = Controlador(screen, 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        c.render()

        if(c.naveDestruida()):
            return GAMEOVER
        
        else:
            pontuacao = c.getPontuacao()
            textoP1 = Texto(f"Pontuação P1: {pontuacao[0]}", 30, (150, 50), "white", screen)
            textoP1.draw()

            textoP2 = Texto(f"Pontuação P2: {pontuacao[1]}", 30, (1100, 50), "white", screen)
            textoP2.draw()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    
    return EXIT