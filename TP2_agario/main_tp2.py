from TP2_agario.bille import Bille
from TP2_agario.creep import Creep
from TP2_agario.playeur import Playeur
from p5 import core

#Attention variables globales
playeur1 = None
creeps = []
bille1 = Bille()

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]



    global playeur1, creeps
    playeur1 = Playeur()

    for i in range(0, 1000):
        creeps.append(Creep())

    print("Setup END-----------")


def run():
    print("run")

    playeur1.afficher(core)
    if core.getMouseLeftClick() is not None:
        playeur1.deplacer(core.getMouseLeftClick())

    for c in creeps:
        c.afficher(core)

if __name__ == '__main__':
    core.main(setup, run)