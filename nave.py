import pygame as pg
from math import sin, cos, pi
from tiro import Tiro

class Nave:
    
    def __init__(self, tela) -> None:
        self.p = [1280/2, 720/2]
        self.vel = [0., 0.]
        self.theta = 0
        self.tela = tela
        self.balas = list()
        self.timerTiro = 100

    def norm(self, vec):
        return (vec[0]**2 + vec[1]**2)**.5

    def getPontos(self, ):
        r = 20
        phi = pi/5
        d = r/cos(phi)
        P = [r*cos(self.theta)+self.p[0], r*sin(self.theta)+self.p[1]]
        Q = [d*cos(pi-phi+self.theta)+self.p[0], d*sin(pi-phi+self.theta)+self.p[1]]
        R = [d*cos(pi+phi+self.theta)+self.p[0], d*sin(pi+phi+self.theta)+self.p[1]]
        return [P, Q, R]
    
    def dispara(self, ):
        d = 20
        self.balas.append(Tiro(self.tela, [self.p[0]+d*cos(self.theta), self.p[1]+d*sin(self.theta),], self.theta))
        self.timerTiro = 0
    
    def atualizaTiros(self, ):
        width, height = self.tela.get_width(), self.tela.get_height()

        for bala in self.balas:
            fora = (bala.pos[0] < 0) or (bala.pos[0]>width)
            fora = fora or (bala.pos[1] < 0) or (bala.pos[1]>height)
            if fora:
                self.balas.remove(bala)

            else:
                bala.render()

    def lerp(self, A, B, t):
        return [A[0] + t*(B[0]-A[0]), A[1] + t*(B[1]-A[1])]

    def fogo(self, ):
        P, Q, R = self.getPontos()
        cos0, sin0 = cos(self.theta), sin(self.theta)
        r = 60
        d = 5
        t = 0.75

        P1 = self.lerp(Q, R, t)
        P1 = [P1[0]-d*cos0, P1[1]-d*sin0]

        P2 = self.lerp(R, Q, t)
        P2 = [P2[0]-d*cos0, P2[1]-d*sin0]

        M = [P[0]-r*cos0, P[1]-r*sin0]

        pg.draw.polygon(self.tela, "red", [M, P1, P2], 2)

    def move(self, ):
        keys = pg.key.get_pressed()
        dt=1
        vmax = 2
        if keys[pg.K_w]:
            cos0, sin0 = cos(self.theta), sin(self.theta)

            self.vel[0] += cos0*dt/50
            self.vel[1] -= sin0*dt/50

            if self.norm(self.vel) > vmax:
                self.vel[0] = vmax*cos0
                self.vel[1] = -vmax*sin0

            self.fogo()

        if keys[pg.K_a]:
            self.theta -= 0.05

        if keys[pg.K_d]:
            self.theta += 0.05

        if keys[pg.K_0]:
            self.p = [1280/2, 720/2]
            self.vel = [0, 0]

        if keys[pg.K_SPACE] and self.timerTiro>=30:
            self.dispara()

        self.timerTiro +=1
        self.p[0] += self.vel[0]
        self.p[1] -= self.vel[1]

    def render(self, ):
        self.move()
        self.atualizaTiros()
        for bala in self.balas:
            bala.render()
        
        pg.draw.polygon(self.tela, "white", self.getPontos(), 2)