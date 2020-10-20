from Cobra import Cobra
from Dolphin import Dolphin
from Donkey import Donkey
from Giraffe import Giraffe
from Goldfish import Goldfish
from Horse import Horse
from Kingsnake import Kingsnake
from Llama import Llama
from Mamba import Mamba
from Monkey import Monkey
from Rattlesnake import Rattlesnake
from Shark import Shark
from Tuna import Tuna
from Viper import Viper
from Whale import Whale


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Morning", "Grass")
george = Monkey("George", "Howler Monkey", "Afternoon", "Bananas")
gregory = Giraffe("Gregory", "Spotted Giraffe", "Midday", "Carrots")
donnie = Donkey("Donnie", "Catalan Donkey", "Morning", "Hay")
helen = Horse("Helen", "Arabian Horse", "Afternoon", "Apples")
randy = Rattlesnake("Randy", "Texas Rattlesnake", "Mice")
mary = Mamba("Mary", "Black Mamba", "Gerbils")
vinnie = Viper("Vinnie", "Viper", "Lizzards")
kerry = Kingsnake("Kerry", "King Snake", "Turtle Eggs")
carlos = Cobra("Carlos", "King Cobra", "Hamster")
debra = Dolphin("Debra", "Striped Dolphin", "Squids")
walker = Whale("Walker", "Killer Whale", "Penguins")
sarah = Shark("Sarah", "Great White Shark", "Seals")
gary = Goldfish("Gary", "Lionhead Goldfish", "Fish Food")
tina = Tuna("Tina", "Blackfin Tuna", "Shrimp")

print(miss_fuzz, george, gregory, donnie, helen, randy, mary, vinnie, kerry, carlos, debra, walker, sarah, gary, tina)
print(tina.feed())
