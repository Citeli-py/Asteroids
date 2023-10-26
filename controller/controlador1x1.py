from model.geradorAsteroids import GeradorAsteroids
from model.asteroid import Asteroid
from model.tiro import Tiro
from model.nave import Nave
from time import sleep
from math import pi
import pygame


class Controlador1x1:
    def __init__(self, screen: pygame.Surface) -> None:

        self.screen = screen
        self.naves = [Nave(screen,[50, 720//2], 0), Nave(screen, [1230, 720//2], pi, 2)] 
        self.gerador = GeradorAsteroids(screen, 1)

        self.placar = [0, 0]


    
    def colisao(self,) -> None: # Existem melhorias para fazer aqui
        # colisao tiro e asteroid
        for asteroid in self.gerador.asteroids:

            for nave in self.naves:
                if nave.colide(asteroid):
                    self.gerador.destroi(asteroid)
                    nave.destroi()
                    self.naves.remove(nave)
                     
            for nave in self.naves:
                for bala in nave.balas:
                    if asteroid.colide(bala):
                        nave.aumentaPontuacao()
                        self.gerador.destroi(asteroid, bala)
                        nave.destroiBala(bala)
        
        if len(self.naves) > 1: # Erro: como definir quem é p1 e p2 caso um fosse destruido
            for bala in self.naves[0].balas: # Se balas do P1 colidem com o P2
                if self.naves[1].colideTiro(bala):
                    self.naves[0].destroiBala(bala)
                    self.naves[1].destroi()
                    self.naves = [self.naves[0]]
                    break
        
        if len(self.naves) > 1:
            for bala in self.naves[1].balas: # Se balas do P2 colidem com o P1
                if self.naves[0].colideTiro(bala):
                    self.naves[1].destroiBala(bala)
                    self.naves[0].destroi()
                    self.naves = [self.naves[1]]
                    break
        
        #print(self.placar)


    def naveDestruida(self,) -> int:
        '''
        retorna 2, 1, 0, -1
        2 -> p2 morreu, 1 -> p1 morreu, 
        0 -> ambos morreram, e -1 -> ninguem morreu
        '''
        p1_vivo, p2_vivo = False, False
        for nave in self.naves:
            if not(p1_vivo):
                p1_vivo = (nave.player == 1)
            
            if not(p2_vivo):
                p2_vivo = (nave.player == 2)

        
        #print(p1_vivo, p2_vivo)

        # 0 0 -> 0, 0 1 -> 1, 1 0 -> 2, 1 1 -> -1

        if p1_vivo == False and p2_vivo == False: # ambos mortos
            return 0

        if  p1_vivo == False and p2_vivo == True: # p1 morreu
            self.placar[1] += 1
            return 1
        
        if  p1_vivo == True and p2_vivo == False: # p2 morreu
            self.placar[0] += 1
            return 2
        
        if  p1_vivo == True and p2_vivo == True: # ambos vivos
            return -1
                

    
    def getPontuacao(self, ) -> (int, int) or int:
        if len(self.naves) > 1:
            return (self.naves[0].pontuacao, self.naves[1].pontuacao)
        
        return self.naves[0].pontuacao
    

    def recomecar(self, ) -> None:
        if(self.naveDestruida() != -1):
            self.render()
            print(len(self.naves))
            sleep(1)

            self.naves = [Nave(self.screen,[50, 720//2], 0), Nave(self.screen, [1230, 720//2], pi, 2)] 
            self.gerador = GeradorAsteroids(self.screen, 1)

        pass

    
    def render(self,) -> None:
        self.screen.fill("purple")
        self.colisao()
        for nave in self.naves:
            nave.render()
        self.gerador.render()
        