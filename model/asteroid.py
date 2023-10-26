import pygame as pg
from math import sin, cos
from model.tiro import Tiro

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

    def colide(self, bala: Tiro):
        d = ((self.pos[0]-bala.pos[0])**2 + (self.pos[1]-bala.pos[1])**2)**0.5
        
        if d <= (bala.raio + self.raio):
            return True   
        return False
    
    def render(self, ):
        self.move()
        self.pos[0] = self.pos[0]%self.tela.get_width()
        self.pos[1] = self.pos[1]%self.tela.get_height()
        pg.draw.circle(self.tela, "white", self.pos, self.raio, 2) # Melhorar