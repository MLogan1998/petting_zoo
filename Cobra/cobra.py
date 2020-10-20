from datetime import date

class Cobra:
    def __init__(self, name, species, food):
        self.name = name
        self.sepcies = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
