from datetime import date
from .critter import Critter

class Horse(Critter):
    def __init__(self, name, species, shift, food, chipnum):
        super().__init__(name, species, food, chipnum)
        self.walking = True
        self.shift = shift
