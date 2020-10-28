from datetime import date
from .critter import Critter
from movements import Walking

class Donkey(Critter, Walking):
    def __init__(self, name, species, shift, food, chipnum):
        Critter.__init__(self, name, species, food, chipnum)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(f'{self.name} is a picky eater and insists on having ketchup on his {self.food}')
