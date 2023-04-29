# Global scope
enemies = 1
def increase_enemies():
    # local scope
    enemies = 2
    print(f"enemies inside functions: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


# Global scope
# player_health = 10


# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()