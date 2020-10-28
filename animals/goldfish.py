from datetime import date
from .critter import Critter
from movements import Swimming

class Goldfish(Critter, Swimming):
    def __init__(self, name, species, food, chipnum):
        super().__init__(name, species, food, chipnum)
        Swimming.__init__(self)
