import pygame
from math import cos, sin, pi

class Cursor:

    def __init__(self, screen) -> None:
        self.tela = screen
        self.pos = [400, 0]
    
    def move(self, modo):
        self.pos[1] = 400 + modo*100
    
    def draw(self, modo):
        self.move(modo)

        r = 20
        phi = pi/5
        d = r/cos(phi)
        P = [r+self.pos[0], self.pos[1]]
        Q = [d*cos(pi-phi)+self.pos[0], d*sin(pi-phi)+self.pos[1]]
        R = [d*cos(pi+phi)+self.pos[0], d*sin(pi+phi)+self.pos[1]]

        pygame.draw.polygon(self.tela, 'white', [P, Q, R], 2)