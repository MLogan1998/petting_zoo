from models import Cobra, Dolphin, Donkey, Giraffe, Goldfish, Horse, Kingsnake, Llama, Mamba, Monkey, Rattlesnake, Shark, Tuna, Viper, Whale, PettingZoo, Snakepit, Wetlands


def add_animals_to_attractions():

  petting_zoo = PettingZoo('Petting Zoo', 'Pet Pet Pet')
  snakepit = Snakepit("Creepy Crawlers", "Keep your hands outside of the tanks")
  aquarium = Wetlands("Awesome Aquatics", "Sharks, Whales, and Tunas Oh MY")

  miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Morning", "Grass", 92549)
  george = Monkey("George", "Howler Monkey", "Afternoon", "Bananas", 39181)  
  gregory = Giraffe("Gregory", "Spotted Giraffe", "Midday", "Carrots", 76876)
  donnie = Donkey("Donnie", "Catalan Donkey", "Morning", "Hay", 23648)
  helen = Horse("Helen", "Arabian Horse", "Afternoon", "Apples", 54921)

  petting_zoo.append_animal(miss_fuzz)
  petting_zoo.append_animal(george)
  petting_zoo.append_animal(gregory)
  petting_zoo.append_animal(donnie)
  petting_zoo.append_animal(helen)

  randy = Rattlesnake("Randy", "Texas Rattlesnake", "Mice", 81625)
  mary = Mamba("Mary", "Black Mamba", "Gerbils", 71603)
  vinnie = Viper("Vinnie", "Viper", "Lizzards", 49816)
  kerry = Kingsnake("Kerry", "King Snake", "Turtle Eggs", 19254)
  carlos = Cobra("Carlos", "King Cobra", "Hamster", 12345)

  snakepit.append_animal(randy)
  snakepit.append_animal(mary)
  snakepit.append_animal(vinnie)
  snakepit.append_animal(kerry)
  snakepit.append_animal(carlos)

  debra = Dolphin("Debra", "Striped Dolphin", "Squids", 5678)
  walker = Whale("Walker", "Killer Whale", "Penguins", 41376)
  sarah = Shark("Sarah", "Great White Shark", "Seals", 59175)
  gary = Goldfish("Gary", "Lionhead Goldfish", "Fish Food", 28922)
  tina = Tuna("Tina", "Blackfin Tuna", "Shrimp", 43819)

  aquarium.appened_animal(debra)
  aquarium.appened_animal(walker)
  aquarium.appened_animal(sarah)
  aquarium.appened_animal(gary)
  aquarium.appened_animal(tina)

  for animal in petting_zoo.animals:
    print(f'You can find {animal.name} the {animal.species} in {petting_zoo.name}')
  
  for animal in snakepit.animals:
    print(f'You can find {animal.name} the {animal.species} in {snakepit.name}')

  for animal in aquarium.animals:
    print(f"You can find {animal.name} the {animal.species} in {aquarium.name}")
  
  donnie.chipnum = 12334

  print(donnie.chipnum)

  print(petting_zoo.last_critter_added)

  print(carlos)
