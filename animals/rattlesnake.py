from datetime import date
from .critter import Critter
from movements import Slithering

class Rattlesnake(Critter, Slithering):
    def __init__(self, name, species, food, chipnum):
        Critter.__init__(self, name, species, food, chipnum)
        Slithering.__init__(self)

    def feed(self):
        print(f'{self.name} is a picky eater. He prefers his {self.food} ice cold')
