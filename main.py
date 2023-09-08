import random
import battle
import cave
import rand
import Intro

def path():
    event_chance = 20
    turns = 10

    for _ in range(turns):
    
        if random.randint(1,100) <= event_chance:
            if random.randint(1, 100) <= 45:
                interaction = 1
                event_chance = 20
                event(interaction)
            else:
                interaction = random.randint(2,3)
                event_chance = 20
                event(interaction)
        
        else:
            event_chance += 10
            print("It's all quiet here.")
            input("Press Enter to continue...")
    
def event(interaction):
    if interaction == 1:
        battle.battle
        print("Battle") # HACK
    if interaction == 2:
        cave.cave
        print("Cave") # HACK
    if interaction == 3:
        rand.event
        print("rand Event") # HACK

    input("Press Enter to continue... This was an event") # HACK
    return

debug = 1

if debug == 1:
    Intro.name = "Debug"
    Intro.p_class = "Warrior"
    path()