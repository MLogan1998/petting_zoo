from .attraction import Attraction

class Snakepit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def append_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)

        except AttributeError:
            print(f'{animal.name} the {animal.species} is scared of snakes, so please do not try to put it in the {self.name}.')
