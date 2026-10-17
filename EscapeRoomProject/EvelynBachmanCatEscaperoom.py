class Stage:
    def __init__(self, description, actions):
        self.description = description
        self.actions = actions

canleave = False
needfood = False
humanout = False
hidingspot = False

livingroom_message = Stage("", {})
couch1 = Stage("", {})
window1 = Stage("", {})
tv1 = Stage("", {})
tv2 = Stage("", {})
tv3 = Stage("", {})
mudroom1 = Stage("", {})
couch_message = Stage("", {})
livingroom2 = Stage("", {})
pillow1 = Stage("", {})
window2 = Stage("", {})
pillow2 = Stage("", {})
nap1 = Stage("", {})
couch2 = Stage("", {})
toy1 = Stage("", {})
toy2 = Stage("", {})
hide1 = Stage("", {})
mudroom_message = Stage("", {})
frontdoor1 = Stage("", {})
shoes1 = Stage("", {})
meow1 = Stage("", {})
keydoor = Stage("", {})
tosskeys1 = Stage("", {})
hidekeys = Stage("", {})
mudroom2 = Stage("", {})
mudroom3 = Stage("", {})
keys1 = Stage("", {})
kitchen1 = Stage("", {})
kitchen_message = Stage("", {})
counter1 = Stage("", {})
counter2 = Stage("", {})
sink1 = Stage("", {})
fridge1 = Stage("", {})
feeder1 = Stage("", {})
feeder2 = Stage("", {})
code = Stage("", {})
kitchen2 = Stage("", {})
bedroom1 = Stage("", {})
bedroom_message = Stage("", {})
bed1 = Stage("", {})
bed2 = Stage("", {})
bed3 = Stage("", {})
dresser1 = Stage("", {})
dresser2 = Stage("", {})
glass1 = Stage("", {})
panic = Stage("", {})
checkfood1 = Stage("", {})
bathroom1 = Stage("", {})
bedroom2 = Stage("", {})
creditscene = Stage("", {})
eatfood = Stage("", {})
couch3 = Stage("",{})
shoes2 = Stage("", {})
fridge2 = Stage("", {})


# LIVING ROOM
livingroom1 = Stage("you are in a cozy living room\nyou neeed to escape, like ASAP", {"investigate": livingroom_message})

livingroom_message.description = "you see a couch in the middle of the room facing a boxy tv, a window off to the side, and your favorite mouse toy in the corner\nyou also see an open doorway off to the east"
livingroom_message.actions = {"couch": couch1, "window": window1, "tv": tv1, "toy": toy1, "mudroom": mudroom1}

couch1.description = "it looks like you could climb this couch or perhaps squeeze underneath"
couch1.actions = {"climb": couch2, "hide": hide1, "nevermind": livingroom2}

couch2.description = "you dig your claws in and scrable (gracefully as usual) onto the couch"
couch2.actions = {"investigate": couch_message, "jump down": livingroom2}

couch_message.description = "you see a pillow in the corner of the couch and have a better view of the window from here"
couch_message.actions = {"pillow": pillow1, "window": window2}

couch3.description = "you are on the couch"
couch3.actions = {"pillow": pillow1, "window": window2, "jump down": livingroom2}

hide1.description = "you squeeze under the couch\nits a bit cramped but this seems like a good place to hide\nyou'll remeber this"
hide1.actions = {"exit": livingroom2}

pillow1.description = "you sniff at the pillow, it looks like it would make a nice bed"
pillow1.actions = {"nap": nap1, "smak": pillow2, "boring": couch3}

pillow2.description = "you attack the pillow with a violent explosion of rage"
pillow2.actions = {"that was nice": couch3}

nap1.description = "you curl up on the pillow, but you cannot sleep\nyou\nmust\nescape"
nap1.actions = {"working on it": couch3}

livingroom2.description = "you are in the living room"
livingroom2.actions = {"couch": couch1, "window": window1, "tv": tv1, "toy": toy1, "mudroom": mudroom1}

toy1.description = "you sniff at your favorite toy\nyou can never quite tell if the mouse is alive\nno time to play now"
toy1.actions = {"look elsewhere": livingroom2, "but mouse": toy2}

toy2.description = "you bat at the mouse and it skids a little across the floor, you have to fight the urge to hunt it properly"
toy2.actions = {"look elsewhere": livingroom2}

window1.description = "you jump for the windwosill and fall short, which is what you had intended anyway so you saunter away"
window1.actions = {"saunter away": livingroom2}

window2.description = "you leap to the windosill with immense grace\nit is tightly closed and locked"
window2.actions = {"jump back": couch3, "jump down": livingroom2}

tv1.description = "you sniff at the blank screeen of the tv, it smells boring"
tv1.actions = {"smack": tv2, "boring": livingroom2}

tv2.description = "you smack at the tv and it makes a static-y sound but doesn't turn on"
tv2.actions = {"smack again": tv3, "boring": livingroom2}

tv3.description = "you smak the tv harder and hiss for good measure, it still doesn't do anything\nyou do notice a slip of paper taped to the back with four strange digits\n'8439'"
tv3.actions = {"boring": livingroom2}


# MUDROOM
mudroom1.description = "you are in a small mudroom entryway\nhow could you get out from here?"
mudroom1.actions = {"investigate": mudroom_message}

mudroom_message.description = "you can see coats lining the far wall with shoes underneath\nthere is a closed door to the south and another open doorway to the north"
mudroom_message.actions = {"front door": frontdoor1, "shoes": shoes1, "kitchen": kitchen1, "living room": livingroom2}

frontdoor1.description = "you scratch at the front door but it is locked tight"
frontdoor1.actions = {"meow sadly": meow1, "find another way": mudroom2}

meow1.description = "MEOOOOOWWW"
meow1.actions = {"move on": mudroom2}

shoes1.description = "you sniff at the shoes, they do not smell nice at all\nthere are some keys in one of shoes"
shoes1.actions = {"try keys on door": keydoor, "boring": mudroom2}

shoes2.description = "you sniff at the shoes, they do not smell nice at all"
shoes2.actions = {"boring": mudroom3}

keydoor.description = "you pick up the keys but immediately realize, you are a cat, you don't know how to use keys"
keydoor.actions = {"hide keys": hidekeys, "toss keys": tosskeys1}

hidekeys.description = "you sneakily hide they keys back in the shoe"
hidekeys.actions = {"move on": mudroom2}

tosskeys1.description = "you toss the keys onto the ground with a huff"
tosskeys1.actions = {"move on": mudroom3}

mudroom2.description = "you are in the mudroom"
mudroom2.actions = {"front door": frontdoor1, "shoes": shoes1, "kitchen": kitchen1, "living room": livingroom2}

mudroom3.description = "you are in the mudroom"
mudroom3.actions = {"front door": frontdoor1, "shoes": shoes2, "keys": keys1, "kitchen": kitchen1, "living room": livingroom2}

keys1.description = "you sniff at the useless keys out on the floor"
keys1.actions = {"hide them": hidekeys, "boring": mudroom3}


# KITCHEN
kitchen1.description = "you are in a cramped messy kitchen\nmaybe this room has a way out?"
kitchen1.actions = {"investigate": kitchen_message}

kitchen_message.description = "you can see a fridge, a wraparound counter, and your automatic feeder (never enough)\nthere is another open doorway to the west"
kitchen_message.actions = {"fridge": fridge1, "counter": counter1, "feeder": feeder1, "mudroom": mudroom2, "bedroom": bedroom1}

fridge1.description = "you scamper up to the fridge\nit is sooo tall and smooth\nnot climbable from here"
fridge1.actions = {"unfortunate": kitchen2}

fridge2.description = "you leap up onto the fridge top\nthe window is shut tight"
fridge2.actions = {"jump down": counter1}

counter1.description = "you leap gracefully onto the countertop and see a sink full of dishes\nyou can see a window peaking out over the fridge from here"
counter1.actions = {"sink": sink1, "fridge": fridge2, "jump down": kitchen2}

counter2.description = "you are on the counter\nyou can see a window peaking out over the fridge from here"
counter2.actions = {"sink": sink1, "fridge": fridge2, "jump down": kitchen2}

sink1.description = "you bat at the faucet but nothing happens and now your paw is a little damp"
sink1.actions = {"yuck": counter2}

feeder1.description = "you scamper over to your automatic feeder\nthe bowl is empty"
feeder1.actions = {"unfortunate": kitchen2, "smack it": feeder2}

feeder2.description = "you smack at the feeder but nothing happens\nyou notice a series of buttons along the top\nmaybe it needs a code"
feeder2.actions = {"unfortunate": kitchen2, "try a code": code}

code.description = "'give up' to give up\ninput a code:"
code.actions = {"give up": kitchen2}

temporary = Stage("", {"temp": eatfood})

eatfood.description = "the top of the feeder pops open\nyou quickly eat as much of the food as you can"
eatfood.actions = {"yum": kitchen2}

kitchen2.description = "you are in the kitchen"
kitchen2.actions = {"fridge": fridge1, "counter": counter1, "feeder": feeder1, "mudroom": mudroom2, "bedroom": bedroom1}


# BEDROOM
bedroom1.description = "you are in the cozy little bedroom\nthe last room in this tiny house\nmaybe this one finally has an exit"
bedroom1.actions = {"investigate": bedroom_message}

bedroom_message.description = "a bed takes up most of the room with a dresser on one side and closed bathroom door on the other"
bedroom_message.actions = {"bed": bed1, "dresser": dresser1, "bathroom door": bathroom1, "kitchen": kitchen2}

bed1.description = "you leap up onto the bed, it is so soft\nyou can probably reach the dresser from here"
bed1.actions = {"cozy": bed2, "dresser": dresser2, "jump down": bedroom2}

bed2.description = "you knead at the soft blankets and purr"
bed2.actions = {"nice": bed3}

bed3.description = "you are on the bed"
bed3.actions = {"cozy": bed2, "dresser": dresser2, "jump down": bedroom2}

bathroom1.description = "you scratch at the bathroom door\n\"not now kitty\" the human says from inside"
bathroom1.actions = {"ick": bedroom2}

dresser1.description = "you scratch at the dresser but it is too high to jump onto from here"
dresser1.actions = {"dang it": bedroom2}

dresser2.description = "you leap up onto the dresser and see a glass sitting near the edge"
dresser2.actions = {"mischief": glass1, "jump down": bed3}

glass1.description = "you bat the glass off the dresser\nit falls onto the carpet but unfortionatly does not break\nthe human bursts out of the bathroom!"
glass1.actions = {"panic": panic}

panic.description = "the human scoops you up\n\"you naughty kitty\"\nthey put the glass back on the dresser, plop you on the bed, and disapear back into the bathroom\n(you should scope out a hiding spot)"
panic.actions = {"dang it": bed3}

hide2 = Stage("you race back through the house and squeeze under the couch\nyou can hear the human come out of the bathroom and start looking for you", {"oh no": checkfood1})

checkfood1.description = "it sounds like they cleaned up your mess but are still out and about\nyou can hear birds chirping from a newly opened window!"
checkfood1.actions = {"interesting": livingroom2}

fridge3 = Stage("you leap up onto the fridge top\nthe window is open and you scramble to it\nbut the human plucks you off the fridge just in time\n\"you know you aren't alowed out, silly kitty\"", {"meowtherf**er": kitchen2})

fridge4 = Stage("you leap up onto the fridge top\nyour human foolishly forgot to close the window when they left!\nyou leap out the window to freedom!!\n\nCONGRADULATIONS YOU HAVE WON!!!", {"quit game": creditscene})

creditscene.description = "thank you for playing!!\ngame writen and designed by Evelyn Bachman"
creditscene.actions = {"quit": creditscene}

bedroom2.description = "you are in the bedroom"
bedroom2.actions = {"bed": bed1, "dresser": dresser1, "bathroom door": bathroom1, "kitchen": kitchen2}

hints = ["hint 1: hitting things repeatedly never hurt", "hint 2: you're pretty hungry", "hint 3: make sure the keys can be found", "hint 4: the way out is high up"]
hint_num = 0
def print_options(lst):
    print("options:")
    for str in lst:
        print("'" + str + "'")
    
cur = livingroom1
inp = input("\nWelcome to Cat Escape!\nyou are a sneaky cat trying to escape into the outdoors\n _._      _,-'\"\"`-._\n(,-.`._,'(      |\\`-/|\n    `-.-' \\ )-`( , o o)\n          `-    \\`_`\"'- \n\nType 'quit' to exit the game at any point.\nType 'hint' at any point for some help\nType 'begin' to start your adventure!\n\n")
while inp != "quit":
    if inp == "begin":
        print(cur.description)
        print("")
        print_options(cur.actions.keys())
        print("")
        inp = input()
    elif inp in cur.actions:
        ##
        if cur == livingroom_message and inp == "mudroom" and livingroom2.actions["mudroom"] != mudroom2:
            livingroom2.actions["mudroom"] = mudroom2
            cur = mudroom1
        elif cur == livingroom2 and inp == "mudroom" and livingroom2.actions["mudroom"] != mudroom2:
            livingroom2.actions["mudroom"] = mudroom2
            cur = mudroom1
        elif cur == mudroom_message and inp == "kitchen" and mudroom2.actions["kitchen"] != kitchen2:
            mudroom2.actions["kitchen"] = kitchen2
            mudroom3.actions["kitchen"] = kitchen2
            cur = kitchen1
        elif cur == mudroom2 and inp == "kitchen" and mudroom2.actions["kitchen"] != kitchen2:
            mudroom2.actions["kitchen"] = kitchen2
            mudroom3.actions["kitchen"] = kitchen2
            cur = kitchen1
        elif cur == mudroom3 and inp == "kitchen" and mudroom3.actions["kitchen"] != kitchen2:
            mudroom3.actions["kitchen"] = kitchen2
            cur = kitchen1
        elif cur == kitchen_message and inp == "bedroom" and kitchen2.actions["bedroom"] != bedroom2:
            kitchen2.actions["bedroom"] = bedroom2
            cur = bedroom1
        elif cur == kitchen2 and inp == "bedroom" and kitchen2.actions["bedroom"] != bedroom2:
            kitchen2.actions["bedroom"] = bedroom2
            cur = bedroom1
        else: 
            cur = cur.actions[inp]

        if canleave and cur == mudroom2:
            cur = mudroom3
        if cur == hide1:
            glass1.actions["hide"] = hide2
        if cur == hidekeys:
            canleave = False

        print(cur.description)
        ##
        if cur == code:
            temp = input()
            while temp != "8439" and temp != "give up":
                print("incorrect\ntry again:")
                temp = input()
            if temp == "8439":
                print("correct!")
                inp = "temp"
                cur = temporary
        else:
            if cur == tosskeys1:
                canleave = True
                if humanout and needfood:
                    counter1.actions["fridge"] = fridge4
                    counter2.actions["fridge"] = fridge4
                    print("your human snatches up the keys\n\"I can't believe you found them! I'm heading out to get you some more food kitty\"\nthe door opens and shuts and the human is gone!")
                    del mudroom3.actions["keys"]
            if cur == eatfood:
                needfood = True
                del feeder1.actions["smack it"]
                if humanout and canleave:
                    counter1.actions["fridge"] = fridge4
                    counter2.actions["fridge"] = fridge4
                    print("the human walks in\n\"how did you get in there silly kitty? it looks like you need some more food, I needed to go to the store anyway\"\nthe human swipes the keys off the floor, the door opens and shuts and the human is gone!")
                    del mudroom3.actions["keys"]
                elif humanout:
                    print("the human walks in\n\"how did you get in there silly kitty? it looks like you need some more food, if only I could find my keys then I could go buy some more\"")
            if cur == checkfood1:
                humanout = True
                if needfood and canleave:
                    print("the human walks by\"I can see you silly kitty. it looks like you need some more food, I needed to go to the store anyway\"\nthe human swipes the keys off the floor, the door opens and shuts and the human is gone!")
                    counter1.actions["fridge"] = fridge4
                    counter2.actions["fridge"] = fridge4
                    del mudroom3.actions["keys"]
                else:
                    if needfood:
                        print("the human walks by\"I can see you silly kitty. it looks like you need some more food, I'd go get you more but I can't find my keys\"")
                    counter1.actions["fridge"] = fridge3
                    counter2.actions["fridge"] = fridge3

            print("")
            print_options(cur.actions.keys())
            print("")
            print("")

            ##
            inp = input()
    elif inp == "hint":
        if hint_num == len(hints):
            hint_num = 0
        print(hints[hint_num])
        hint_num += 1

        print("")
        print(cur.description)
        print("")
        print_options(cur.actions.keys())
        print("")
        inp = input()
    else:
        print("invalid input, try again\n/ᐠ • ˕ •マ ?\n")
        inp = input()