class Wetlands:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def appened_animal(self, animal):
        self.animals.append(animal)
