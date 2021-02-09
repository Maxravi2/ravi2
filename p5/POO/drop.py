import random
from pyclbr import Class

import pygame
from pygame import Vector2

class Drop:

    def __init__(self,largeur):
        self.gravity = random.randint(5,20)
        self.size = random.randint(10,20)
        self.r=random.randint(0,255)
        self.v=random.randint(0,255)
        self.b=random.randint(0,255)
        self.position =Vector2(random.randint(0,  largeur), random.randint(-largeur,0))

    def tomber(self,hauteur):
        self.position.y= self.position.y+self.gravity
        if self.position.y > hauteur:
            self.raz()

    def raz(self):
        self.position.y=0

    def afficher(self,core):
        pygame.draw.line(core.screen, (self.r, self.v, self.b), (self.position.x, self.position.y), (self.position.x, self.position.y + 10), 1)