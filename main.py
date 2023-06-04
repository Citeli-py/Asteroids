import pygame
from nave import Nave
from asteroid import Asteroid
from geradorAsteroids import GeradorAsteroids

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

n = Nave(screen) 
gerador = GeradorAsteroids(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    n.render()
    gerador.render(n.balas)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()