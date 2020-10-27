from datetime import date
from .critter import Critter

class Cobra(Critter):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        self.slithering = True
