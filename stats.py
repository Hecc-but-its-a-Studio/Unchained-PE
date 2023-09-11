import random

class EnemyStats:
    def __init__(self, attack, defense, speed, dodge_chance, max_health, crit_chance):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.dodge_chance = dodge_chance
        self.max_health = max_health
        self.current_health = self.max_health
        self.crit_chance = crit_chance


bat = EnemyStats(3,2,7,10,10,5)
snail = EnemyStats(10,5,1,1,15,1)
enemy_stats = EnemyStats(1,1,1,1,1,1)

def area_1():
    global enemy_stats
    if random.randint(1,2) == 1:
        enemy_stats = bat
    else:
        enemy_stats = snail

character_stats = {
    'attack': 1,
    'defense': 1,
    'speed': 1,
    'dodge': 1,
    'max_health': 1,
    'current_health': 1,
    'crit_chance': 10,
    'crit_damage': 1.5
}

def stat_add(stat: str, value: int):
    character_stats[stat] += value

def stat_set(stat: str, value: int):
    character_stats[stat] = value

stats = character_stats

p_class = ""
name = ""