import pygame as pg
from math import sin, cos

class Tiro:

    def __init__(self, tela, pos, theta) -> None:
        self.pos = pos
        self.theta = theta
        self.vel = 5
        self.tela = tela
        self.raio = 1

    def move(self, ):
        self.pos[0] += self.vel*cos(self.theta)
        self.pos[1] -= -self.vel*sin(self.theta)

    def render(self, ):
        self.move()
        pg.draw.circle(self.tela, "white", self.pos, self.raio)
