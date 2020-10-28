from datetime import date
from .critter import Critter
from movements import Slithering

class Mamba(Critter, Slithering):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        Slithering.__init__(self)
