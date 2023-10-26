from random import randint, choice
from model.asteroid import Asteroid
from model.tiro import Tiro
from math import pi
import pygame

class GeradorAsteroids:

    def __init__(self, tela: pygame.Surface, mode=0) -> None:
        self.asteroids: [Asteroid] = []
        self.tela: pygame.Surface = tela
        self.mode: int = mode

        for i in range(5):
            self.addRand()

    def addRand(self, ):

        pos = [choice([0, self.tela.get_width()]), randint(0, self.tela.get_height())]
        if self.mode == 1:
            pos = [ randint(self.tela.get_width()//2 - 250, 250 + self.tela.get_width()//2),
                    choice([0, self.tela.get_height()]) ]

        self.add(pos, 3)
    
    def add(self, pos: list, tipo: int, theta: float = 0, destroido=False):
        phi = pi/4

        if destroido:
            self.asteroids.extend([Asteroid(self.tela, [pos[0], pos[1]], theta+phi, tipo), 
                                   Asteroid(self.tela, [pos[0], pos[1]], theta-phi, tipo)])
        else:
            theta = 2*pi*randint(0, 100)/100
            self.asteroids.append(Asteroid(self.tela, pos, theta, tipo))


    def destroi(self, asteroid: Asteroid, tiro: Tiro = None):

        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)

        if asteroid.tipo>1:
            if tiro == None:
                self.add(asteroid.pos, asteroid.tipo-1, destroido=True)
            else:
                self.add(asteroid.pos, asteroid.tipo-1, theta=tiro.theta, destroido=True)
        else:
            self.addRand()

    
    def render(self,):
        for asteroid in self.asteroids:
            asteroid.render()
    
