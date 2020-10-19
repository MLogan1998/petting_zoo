from datetime import date

class Cobra:
    def __init__(self, name, species):
        self.name = name
        self.sepcies = species
        self.date_added = date.today()
        self.slithering = True
