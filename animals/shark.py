from datetime import date
from .critter import Critter
from movements import Swimming

class Shark(Critter, Swimming):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} is a picky eater and prefers her {self.food} with fried rice.')
