from datetime import date
from .critter import Critter

class Rattlesnake(Critter):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        self.slithering = True

    def feed(self):
        print(f'{self.name} is a picky eater. He prefers his {self.food} ice cold')
