from model.geradorAsteroids import GeradorAsteroids
from model.asteroid import Asteroid
from model.tiro import Tiro
from model.nave import Nave
import pygame


class Controlador:
    def __init__(self, screen: pygame.Surface, mode: int = 1) -> None:

        self.screen = screen
        
        if mode != 1:
            self.naves = [Nave(screen, [1280//2, 720//2]), Nave(screen, [1280//2, 720//2], 2)] 
        else:
            self.naves = [Nave(screen, [1280//2, 720//2])]

        self.gerador = GeradorAsteroids(screen)


    def colisao(self,) -> None: # Existem melhorias para fazer aqui
        # colisao tiro e asteroid
        for asteroid in self.gerador.asteroids:

            for nave in self.naves:
                if nave.colide(asteroid):
                    self.gerador.destroi(asteroid)
                    nave.destroi()
                    self.naves = []
                    
            for nave in self.naves:
                for bala in nave.balas:
                    if asteroid.colide(bala):
                        nave.aumentaPontuacao()
                        self.gerador.destroi(asteroid, bala)
                        nave.destroiBala(bala)



    def naveDestruida(self,) -> bool:
        if len(self.naves) <= 0:
            return True
        return False
    
    def getPontuacao(self, ) -> (int, int) or int:
        if len(self.naves) > 1:
            return (self.naves[0].pontuacao, self.naves[1].pontuacao)
        
        return self.naves[0].pontuacao

    
    def render(self,) -> None:
        self.screen.fill("purple")
        self.colisao()
        for nave in self.naves:
            nave.render()
        self.gerador.render()
        