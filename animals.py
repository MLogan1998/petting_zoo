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


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Morning")
george = Monkey("George", "Howler Monkey", "Afternoon")
gregory = Giraffe("Gregory", "Spotted Giraffe", "Midday")
donnie = Donkey("Donnie", "Catalan Donkey", "Morning")
helen = Horse("Helen", "Arabian Horse", "Afternoon")
randy = Rattlesnake("Randy", "Texas Rattlesnake")
mary = Mamba("Mary", "Black Mamba")
vinnie = Viper("Vinnie", "Viper")
kerry = Kingsnake("Kerry", "King Snake")
carlos = Cobra("Carlos", "King Cobra")
debra = Dolphin("Debra", "Striped Dolphin")
walker = Whale("Walker", "Killer Whale")
sarah = Shark("Sarah", "Great White Shark")
gary = Goldfish("Gary", "Lionhead Goldfish")
tina = Tuna("Tina", "Blackfin Tuna")

print(miss_fuzz, george, gregory, donnie, helen, randy, mary, vinnie, kerry, carlos, debra, walker, sarah, gary, tina)
print(f'{george.name} the {george.species} is available to pet during the {george.shift} shift on {george.date_added}.')
