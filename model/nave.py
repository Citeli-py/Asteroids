import pygame as pg
from math import sin, cos, pi
from model.tiro import Tiro
from model.asteroid import Asteroid


def norm(vec):
    return (vec[0]**2 + vec[1]**2)**.5

def lerp(A, B, t):
    return [A[0] + t*(B[0]-A[0]), A[1] + t*(B[1]-A[1])]

def toVec(A, B):
    return [(B[0]-A[0]), (B[1]-A[1])]

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]


class Nave:
    
    def __init__(self, tela, pos: [int, int], theta: float=0, player: int=1) -> None:

        self.tela = tela
        self.player = player
        self.pontuacao = 0

        self.p = pos
        self.vel = [0., 0.]
        self.theta = theta

        self.balas = list()
        self.timerTiro = 100
        self.vmax = 2

        cor = ["blue", "green"]
        self.cor = cor[player-1]

        controles = [   [pg.K_w, pg.K_a, pg.K_d, pg.K_SPACE],
                        [pg.K_UP, pg.K_LEFT, pg.K_RIGHT, pg.K_RSHIFT]   ]
        
        self.controle = controles[player-1]

        self.tiro_sound = pg.mixer.Sound("sounds/laser.wav")
        self.destroi_sound = pg.mixer.Sound("sounds/explosion.wav")

        self.tiro_sound.set_volume(.5)
        self.destroi_sound.set_volume(.5)

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

    def fogo(self, ) -> None:
        P, Q, R = self.getPontos()
        cos0, sin0 = cos(self.theta), sin(self.theta)
        r, d, t = 60, 5, 0.75

        P1 = lerp(Q, R, t)
        P1 = [P1[0]-d*cos0, P1[1]-d*sin0]

        P2 = lerp(R, Q, t)
        P2 = [P2[0]-d*cos0, P2[1]-d*sin0]

        M = [P[0]-r*cos0, P[1]-r*sin0]

        pg.draw.polygon(self.tela, "red", [M, P1, P2], 2)

    def move(self, ) -> bool:
        keys = pg.key.get_pressed()
        dt=1

        acelerando = False

        if keys[self.controle[0]]:
            cos0, sin0 = cos(self.theta), sin(self.theta)

            self.vel[0] += cos0*dt/50
            self.vel[1] -= sin0*dt/50

            if norm(self.vel) > self.vmax: # Velocidade máxima
                self.vel[0] = self.vmax*cos0
                self.vel[1] = -self.vmax*sin0

            acelerando = True

        if keys[self.controle[1]]:
            self.theta -= 0.05

        if keys[self.controle[2]]:
            self.theta += 0.05

        if keys[self.controle[3]] and self.timerTiro>=30:
            pg.mixer.Sound.play(self.tiro_sound)
            self.dispara()

        self.timerTiro +=1
        self.p[0] += self.vel[0]
        self.p[1] -= self.vel[1]

        return acelerando

    def hitbox2(self, pos: (int, int), raio: int) -> bool:
        # hitbox redonda
        R = 15
        d = ((self.p[0]-pos[0])**2 + (self.p[1]-pos[1])**2)**.5
        if d <= R + raio:
            return True
        return False
    
    def hitbox(self, pos: (int, int), raio: int) -> bool: 
        # Hitbox Poligonal
        R = 5/raio # tolerancia 
        Pontos = self.getPontos()
        for i in range(len(Pontos)):
            A, B = Pontos[i], Pontos[(i+1)%len(Pontos)] # segmento de reta do lado
            u, v = toVec(A, B), toVec(A, pos)

            # Projeção do centro da circunferencia no lado AB
            t = dot(u,v)/(norm(u)**2) 

            if (t<=1) and (t>=0):
                P = [u[0]*t+A[0], u[1]*t+A[1]]
                d = norm(toVec(P, pos))

                if d <= raio+R:
                    return True
        
        return False


    def colide(self, asteroid: Asteroid) -> bool:
        if self.hitbox(asteroid.pos, asteroid.raio):
            return True
        return False
    
    def colideTiro(self, tiro: Tiro) -> bool:
        if self.hitbox(tiro.pos, tiro.raio):
            return True
        return False

    def render(self, ) -> None:

        acelerando = self.move()
        self.atualizaTiros()
        for bala in self.balas:
            bala.render()
        
        self.p[0] = self.p[0]%self.tela.get_width()
        self.p[1] = self.p[1]%self.tela.get_height()
        

        pg.draw.polygon(self.tela, self.cor, self.getPontos(), 2)
        if acelerando:
            self.fogo()

    def destroiBala(self, bala: Tiro) -> None:
        self.balas.remove(bala)

    def destroi(self, ):
        self.vmax = 0
        pg.mixer.Sound.play(self.destroi_sound)


    def aumentaPontuacao(self, ):
        self.pontuacao += 100