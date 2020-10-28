from datetime import date
from .critter import Critter
from movements import Walking

class Horse(Critter, Walking):
    def __init__(self, name, species, shift, food, chipnum):
        Critter.__init__(self, name, species, food, chipnum)
        Walking.__init__(self)
        self.shift = shift
