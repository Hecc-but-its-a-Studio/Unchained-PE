import stats
import random

player = stats.character_stats

stats.area_1()

def player_attack(enemy):
    damage = player['attack']
    if random.randint(1,100) < player['crit_chance']:
        damage *= 2  # Critical hit

    if random.randint(1,100) < enemy.dodge_chance:
        print("Enemy dodged your attack!")
        return 0  # No damage dealt
    else:
        damage_dealt = max(0, damage - enemy.defense)
        enemy.current_health -= damage_dealt
        return damage_dealt

def enemy_attack(player, enemy):
    damage = enemy.attack

    if random.randint(1,100) < player['dodge_chance']:
        print("You dodged the enemy's attack!")
        return 0  # No damage dealt
    else:
        damage_dealt = max(0, damage - player.defense)
        player.current_health -= damage_dealt
        return damage_dealt

# Example usage:
while player['current_health'] > 0 and stats.enemy_stats.current_health > 0:
    # Player's turn
    print("Player's turn:")
    choice = input("Choose an action (1: Attack, 2: Block): ")
    if choice == '1':
        damage = player_attack(stats.enemy_stats)
        print(f"You dealt {damage} damage to the enemy.")
    elif choice == '2':
        player['defense']*= 1.5

    # Enemy's turn
    print("Enemy's turn:")
    damage = enemy_attack(stats.enemy_stats)
    print(f"Enemy dealt {damage} damage to you.")

# Check the outcome of the battle
if player['current_health'] <= 0:
    print("You were defeated!")
elif stats.enemy_stats.current_health <= 0:
    print("You defeated the enemy!")

