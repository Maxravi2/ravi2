from random import random

import pygame
from pygame.math import Vector3, Vector2


class Creep:

    def __init__(self):
        self.taille = 5
        self.couleur = Vector3(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position = Vector2()

    def mourir(self):
        pass

    def afficher(self,core):
        pygame.draw.circle(core.screen,(int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)), (int(self.position.x),int(self.position.y)), self.taille)
