from datetime import date
from .critter import Critter
from movements import Swimming

class Dolphin(Critter, Swimming):
    def __init__(self, name, species, food, chipnum):
        Critter.__init__(self, name, species, food, chipnum)
        Swimming.__init__(self)
