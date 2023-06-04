from random import randint, choice
from asteroid import Asteroid
from math import pi

class GeradorAsteroids:

    def __init__(self, tela) -> None:
        self.asteroids=[]
        self.tela = tela

        for i in range(5):
            pos = [choice([0, self.tela.get_width()]), randint(0, self.tela.get_height())]
            self.add(pos, 3)
    
    def add(self, pos, tipo):
        self.asteroids.append(Asteroid(self.tela, pos, 2*pi*randint(0, 360)/360, tipo))

    def crash(self, asteroid: Asteroid):
        if asteroid.tipo>1:
            for i in range(2):
                self.add(asteroid.pos, asteroid.tipo-1)
        self.asteroids.remove(asteroid)

    
    def colisao(self, asteroid, balas):
        for bala in balas:
            if asteroid.colide(bala):
                self.crash(asteroid)
                del bala
    
    def render(self, balas):
        for asteroid in self.asteroids:
            self.colisao(asteroid, balas)
            asteroid.render()
    
