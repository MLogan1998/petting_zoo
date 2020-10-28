from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)


    def append_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)

        except AttributeError:
            print(f'{animal.name} the {animal.species} doesn\'t like to be petted, so please do not try to put it in the {self.name}.')
