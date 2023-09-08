import main

character_stats = {
    'attack': 1,
    'defense': 1,
    'speed': 1,
    'dodge': 1,
    'max_health': 1,
    'current_health': 1,
    'crit_chance': 10
}

def stat_add(stat: str, value: int):
    character_stats[stat] += value

def stat_set(stat, value):
    character_stats[stat] = value

stats = character_stats



# Introduction and character selection phase
def intro():
    print("Welcome Traveler, what is your name? ")

    while True:  # This will loop asking for your name if you say anything other than yes.
        global name

        p_class = ""
        name = str(input("Enter your name: ")).capitalize()

        print(f"Are you certain you would like to be called {name}? ")
        confirm = input("Enter Y or N: ").upper()

        if confirm == "Y" and name == "Debug":
            p_class = "Warrior"
            stat_changer()
            break
        if confirm == "Y":
            class_select()
            break  # Exit the loop if the name is confirmed
        else:
            print("Well, what is your name then? ")

# Class selection phase
def class_select():
    classes = "Warrior, Jester, Artificer"

    print(f"Please select a class, {name}. Available classes are: ")
    print(classes)
    global p_class 
    p_class = str(input("Enter your class: ")).capitalize()

    print(f"Are you certain you would like to be a {p_class}? ")
    confirm = input("Enter Y or N: ").upper()

    if confirm == "Y" and p_class == "Warrior":
       stat_changer()
    else:
        print("Imagine believing in the illusion of choice. ψ(｀∇´)ψ You're a Warrior now.")
        p_class = "Warrior"
        stat_changer()

# Function to change character stats
def stat_changer():
    global stats
    if p_class == "Warrior":
        stat_set('attack', 5)
        stat_set('defense', 5)
        stat_set('speed', 5)
        stat_set('dodge', 5)
        stat_set('max_health', 15)

    stats['current_health'] = stats['max_health']
    begin()

def display():
    print(f"{name}'s Stats:")
    print("Attack:", stats['attack'])
    print("Attack:", stats['crit_chance'])
    print("Defense:", stats['defense'])
    print("Speed:", stats['speed'])
    print("Dodge Chance:", stats['dodge'])
    print("Current Health:", stats['current_health'])
    print("Your class:", p_class)

# Display character stats and information
def begin():
    display()
    input("Press Enter to continue...")
    main.path()
# Start the game by calling the intro function
intro()
