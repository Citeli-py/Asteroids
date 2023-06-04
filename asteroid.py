import pygame as pg
from math import sin, cos

class Asteroid:

    def __init__(self, tela, pos, theta, tipo) -> None:
        self.pos = pos
        self.theta = theta
        self.vel = 1
        self.tela = tela
        self.tipo = tipo
        self.raio = 10*self.tipo

    def move(self, ):
        self.pos[0] += self.vel*cos(self.theta)
        self.pos[1] -= -self.vel*sin(self.theta)

    def colide(self, ):
        pass


    def render(self, ):
        self.move()
        pg.draw.circle(self.tela, "white", self.pos, self.raio, 2) # Melhorar