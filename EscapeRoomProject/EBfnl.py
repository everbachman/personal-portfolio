
class Area:
    def __init__(self, paths, interaction_message):
        self.paths = paths # dictionary of directions to other rooms and areas in the rooms
        self.interaction_message = interaction_message  # message shown when player enters the area

# Define areas
livingroom = Area({}, ["you are in the cozy living room.\nyou see a couch, a TV, and a window leading outside.\n\n'go east' to go to the mudroom.\n", "you are still in the living room.\nyou see a couch, a TV, and a window leading outside.\n\n'go east' to go to the mudroom.\n", "you are back in the living room.\nyou see the couch, TV, and window.\n\n'go east' to go to the mudroom.\n"])
couch = Area({}, ["you are on the couch.\nyou see some pillows to play with and an armrest near the window.\n\n'jump down' to get back to the livingroom.\n", "you are still on the couch.\nyou see some pillows to play with and an armrest near the window.\n\n'jump down' to get back to the livingroom.\n","you are on the couch.\nyou see some pillows to play with and an armrest near the window.\n\n'jump down' to get back to the livingroom.\n"])
bedroom = Area({}, ["you are in the bedroom.\nyou see a bed and a dresser.\n\n'go east' to go to the kitchen.\n", "you are still in the bedroom.\nyou see a bed and a dresser.\n\n'go east' to go to the kitchen.\n"])
bed = Area({}, ["you are on the bed.\nyou see a soft blanket and a pillow and you can almost see the top of the dresser from here!\n\n'jump down' to get back to the bedroom.\n", "you are still on the bed.\nyou see a soft blanket and a pillow and you can almost see the top of the dresser from here!\n\n'jump down' to get back to the bedroom.\n"])
dresser = Area({}, ["you are on top of the dresser.\nyou see a glass and the tops of some drawers below you.\n\n'jump down' to get back to the bedroom.\n", "you are still on the dresser top.\nyou see a glass and the tops of some drawers below you.\n\n'jump down' to get back to the bedroom.\n"])
kitchen = Area({}, ["you are in the kitchen.\nyou see a counter, a fridge, and a trashcan.\n\n'go west' to go to the bedroom.\n'go south' to go to the mudroom.\n", "you are still in the kitchen.\nyou see a counter, a fridge, and a trashcan.\n\n'go west' to go to the bedroom.\n'go south' to go to the mudroom.\n"])
counter = Area({}, ["you are on the kitchen counter.\nyou see a sink and a stove, you think you could reach the fridge from here.\n\n'jump down' to get back to the kitchen.\n", "you are still on the kitchen counter.\nyou see a sink and a stove, you think you could reach the fridge from here.\n\n'jump down' to get back to the kitchen.\n"])
counter2 = {}
mudroom = Area({}, ["you are in the mudroom.\nyou see a door leading outside, some umbrellas, and a coat rack.\n\n'go north' to go to the kitchen.\n'go west' to go to the livingroom.\n", "you are back in the mudroom.\nyou see a door leading outside, some umbrellas, and a coat rack.\n\n'go north' to go to the kitchen.\n'go west' to go to the livingroom.\n"])

# Define paths
livingroom.paths = {"go east": (mudroom, "you wander into the mudroom"), "window": (livingroom, "the window is too high to jump up to from here. I wonder if there is another way?\n"), "couch": (couch, "/ᐠ≽•ヮ•≼マ\nyou dig your claws in and scramble (gracefully) onto the couch\n"), "TV": (livingroom, "you sniff at the blank TV, it appears to be off\n")}
couch.paths = {"jump down": (livingroom, "you leap off the couch back onto the floor\n"), "pillow": (couch, "/ᐠ. .ᐟ\\ฅ\nyou bat at a pillow, but it doesn't do much :(\n"), "armrest": (couch, "from the armrest you leap to the windowsill but the window is closed so you jump back :(\n")}
bedroom.paths = {"go east": (kitchen, "you slink into the kitchen\n"), "bed": (bed, "/ᐠ≽•ヮ•≼マ\nyou leap onto the bed\n"), "dresser": (bedroom, "the dresser is too high to jump onto and too smooth to climb\n")}
bed.paths = {"jump down": (bedroom, "you pounce off the bed back onto the floor\n"), "blanket": (bed, "/ᐠ. .ᐟ\\ฅ\nyou knead the blanket with your paws and purr contentedly :D\n"), "pillow": (bed, "/ᐠ. .ᐟ\\ฅ\nyou bat at the pillow but it doesn't do much :(\n"), "dresser": (dresser, "You leap from the bed to the dresser, barely making it\n")}
dresser.paths = {"jump down": (bedroom, "you carefully jump down from the dresser back onto the floor\n"), "glass": (dresser, "/ᐠ. .ᐟ\\ฅ\nyou sniff at the glass of water and decide to knock it off :3\n the human is coming to clean up! better run\n(•˕ •マ.ᐟ\n"), "drawers": (dresser, "you try to open a drawer but they are all shut tight\n")} 
kitchen.paths = {"go west": (bedroom, "you sneak back into the bedroom\n"), "go south": (mudroom, "you prowl into the mudroom\n"), "counter": (counter, "/ᐠ≽•ヮ•≼マ\nyou scramble up onto the counter jumping off the trashcan\n"), "trashcan": (kitchen, "this smells yucky, you don't want to go too stay close >^<\n"), "fridge": (kitchen, "you try to open the fridge but it's shut tight. you see a window far above, too high to jump from here :O\n")} 
counter.paths = {"jump down": (kitchen, "you leap off the counter back onto the floor\n"), "sink": (counter, "you bat at the faucet but nothing happens\n"), "stove": (counter, "you sniff at the stove but it seems cold and uninteresting\n"), "fridge": (kitchen, "/ᐠ≽•ヮ•≼マyou jump onto the fridge with a clatter and find the window above open!\nthe human snatches you up and puts you back on the floor scolding you\n")} 
counter2 = {"jump down": (kitchen, "you leap off the counter back onto the floor\n"), "sink": (counter2, "/ᐠ. .ᐟ\\ฅ\nyou bat at the faucet but nothing happens\n"), "stove": (counter2, "you sniff at the stove but it seems cold and uninteresting\n"), "fridge": (livingroom, "/ᐠ≽•ヮ•≼マyou jump onto the fridge with a clatter and find the window above open!\nthe human is distracted by your mess so you make a break for it out into the wild!\n\n    |\\__/,|   (`\\\n  _.|o o  |_   ) )\n-(((---(((--------\nCONGRATULATIONS YOU HAVE ESCAPED!!\n\ntype 'quit' to exit the game.\ntype 'begin to start over"),}
mudroom.paths = {"go north": (kitchen, "you scamper back into the kitchen\n"), "go west": (livingroom, "you slink back into the livingroom\n"), "door": (mudroom, "/ᐠ. .ᐟ\\ฅ\nyou scratch at the door but it wont open\n"), "coat rack": (mudroom, "you sniff at the coats, but they don't seem interesting\n"), "umbrellas": (mudroom, "/ᐠ. .ᐟ\\ฅ\nyou bat at an umbrella but it doesn't do much :(\n")} 

# Game loop
curroom = livingroom
inp = input("\nWelcome to Cat Escape!\nyou are a sneaky cat trying to escape into the outdoors\n _._      _,-'\"\"`-._\n(,-.`._,'(      |\\`-/|\n    `-.-' \\ )-`( , o o)\n          `-    \\`_`\"'- \n\nType 'quit' to exit the game at any point.\nType 'begin' to start your adventure!\nwhen in a room, type the the name of an item you see to investigate\n\n")
while inp != "quit":
    if inp == "begin":
        curroom = livingroom
        print(curroom.interaction_message)
        inp = input()
    elif inp in curroom.paths:
        if ((inp == "glass") and (curroom == dresser)):
            counter.paths = counter2
        nextroom, message = curroom.paths[inp]
        curroom = nextroom
        if ((inp == "fridge") and (curroom == livingroom)):
            print(message)
        else:
            print(message + curroom.interaction_message)
        inp = input()
    else:
        print("invalid input, try again\n/ᐠ • ˕ •マ ?\n")
        inp = input()
