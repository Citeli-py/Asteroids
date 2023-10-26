import pygame

class Texto:

    def __init__(self, texto: str, size: int, pos: tuple, color: str, screen : pygame.Surface) -> None:
        self.screen = screen

        font = pygame.font.Font('freesansbold.ttf', size)
        self.texto = font.render(texto, True, color)
        self.textRect = self.texto.get_rect()
        self.textRect.center = (pos[0], pos[1])

    def draw(self, ):
        self.screen.blit(self.texto, self.textRect)