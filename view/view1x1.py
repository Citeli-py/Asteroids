import pygame
from var import *
from controller.controlador1x1 import Controlador1x1
from model.Texto import Texto

def run(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True

    c = Controlador1x1(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        c.render()
        c.recomecar()

        textoPlacar = f"{c.placar[0]} : {c.placar[1]}"
        Placar = Texto(textoPlacar, 50, (screen.get_width()//2, 50), "white", screen)
        Placar.draw()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    
    return EXIT