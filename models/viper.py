from datetime import date

class Viper:
    def __init__(self, name, species, food, chipnum):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
        self.__chipnum = chipnum

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}. {self.name} eats {self.food}. {self.name} was last fed on {self.date_added}."

    @property
    def chipnum(self):
        return self.__chipnum

    @chipnum.setter
    def chipnum(self, number):
        pass
