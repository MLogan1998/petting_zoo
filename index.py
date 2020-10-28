from animals import Cobra, Dolphin, Donkey, Giraffe, Goldfish, Horse, Kingsnake, Llama, Mamba, Monkey, Rattlesnake, Shark, Tuna, Viper, Whale
from attractions import PettingZoo, Snakepit, Wetlands

def main():

  petting_zoo = PettingZoo('Petting Zoo', 'Pet Pet Pet')
  snakepit = Snakepit("Creepy Crawlers", "Keep your hands outside of the tanks")
  aquarium = Wetlands("Awesome Aquatics", "Sharks, Whales, and Tunas Oh MY")

  miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Morning", "Grass", 92549)
  george = Monkey("George", "Howler Monkey", "Afternoon", "Bananas", 39181)  
  gregory = Giraffe("Gregory", "Spotted Giraffe", "Midday", "Carrots", 76876)
  donnie = Donkey("Donnie", "Catalan Donkey", "Morning", "Hay", 23648)
  helen = Horse("Helen", "Arabian Horse", "Afternoon", "Apples", 54921)

  randy = Rattlesnake("Randy", "Texas Rattlesnake", "Mice", 81625)
  mary = Mamba("Mary", "Black Mamba", "Gerbils", 71603)
  vinnie = Viper("Vinnie", "Viper", "Lizzards", 49816)
  kerry = Kingsnake("Kerry", "King Snake", "Turtle Eggs", 19254)
  carlos = Cobra("Carlos", "King Cobra", "Hamster", 12345)

  debra = Dolphin("Debra", "Striped Dolphin", "Squids", 5678)
  walker = Whale("Walker", "Killer Whale", "Penguins", 41376)
  sarah = Shark("Sarah", "Great White Shark", "Seals", 59175)
  gary = Goldfish("Gary", "Lionhead Goldfish", "Fish Food", 28922)
  tina = Tuna("Tina", "Blackfin Tuna", "Shrimp", 43819)

  petting_zoo.append_animal(miss_fuzz)
  petting_zoo.append_animal(george)
  petting_zoo.append_animal(gregory)
  petting_zoo.append_animal(donnie)
  petting_zoo.append_animal(helen)
  petting_zoo.append_animal(debra) # Will Not Append.

  snakepit.append_animal(randy)
  snakepit.append_animal(mary)
  snakepit.append_animal(vinnie)
  snakepit.append_animal(kerry)
  snakepit.append_animal(carlos)
  snakepit.append_animal(helen) # Will Not Append.

  aquarium.append_animal(debra)
  aquarium.append_animal(walker)
  aquarium.append_animal(sarah)
  aquarium.append_animal(gary)
  aquarium.append_animal(tina)
  aquarium.append_animal(randy) # Will Not Append.

  for animal in petting_zoo.animals:
    print(f'You can find {animal.name} the {animal.species} in {petting_zoo.name}')
  
  for animal in snakepit.animals:
    print(f'You can find {animal.name} the {animal.species} in {snakepit.name}')

  for animal in aquarium.animals:
    print(f"You can find {animal.name} the {animal.species} in {aquarium.name}")

  donnie.chipnum = 12334

  print(donnie.chipnum)

  print(aquarium.last_critter_added)

  print(carlos)

  donnie.feed()
  randy.feed()
  sarah.feed()
  sarah.swim()

main()
