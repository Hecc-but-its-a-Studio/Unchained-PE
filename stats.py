class EnemyStats:
    def __init__(self, attack, defense, speed, dodge_chance, current_health, max_health, crit_chance):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.dodge_chance = dodge_chance
        self.current_health = current_health
        self.max_health = max_health
        self.crit_chance = crit_chance