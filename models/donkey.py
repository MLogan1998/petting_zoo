from datetime import date
from .critter import Critter

class Donkey(Critter):
    def __init__(self, name, species, shift, food, chipnum):
        super().__init__(name, species, food, chipnum)
        self.walking = True
        self.shift = shift

    def feed(self):
        print(f'{self.name} is a picky eater and insists on having ketchup on his {self.food}')
