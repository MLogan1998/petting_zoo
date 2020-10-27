from datetime import date
from .critter import Critter

class Shark(Critter):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        self.swimming = True

    def feed(self):
        print(f'{self.name} is a picky eater and prefers her {self.food} with fried rice.')
