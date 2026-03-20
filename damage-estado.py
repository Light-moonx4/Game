import random

def damage_generator(min_val=10, max_val=25):
    attack = random.randint(min_val, max_val)
    return attack

def hp_bar(current_hp, max_hp, bar_length=20):
    filled = int((current_hp / max_hp) * bar_length)
    empty = bar_length - filled
    bar = "#" * filled + "-" * empty
    return f"[{bar}] {current_hp}/{max_hp} HP"

def show_status(hero_name, hero_hp, hero_max_hp, enemy_name, enemy_hp, enemy_max_hp):
    damage_to_hero  = damage_generator()
    damage_to_enemy = damage_generator()

    hero_hp_remaining  = max(0, hero_hp  - damage_to_hero)
    enemy_hp_remaining = max(0, enemy_hp - damage_to_enemy)

    print(f"\n  COMBAT STATUS")
    print(f"{'─' * 35}")
    print(f" {hero_name}")
    print(f"   {hp_bar(hero_hp_remaining, hero_max_hp)}")
    print(f"   Damage received: -{damage_to_hero}")
    print(f"{'─' * 35}")
    print(f" {enemy_name}")
    print(f"   {hp_bar(enemy_hp_remaining, enemy_max_hp)}")
    print(f"   Damage received: -{damage_to_enemy}")
    print(f"{'─' * 35}")

    return (hero_name, hero_hp_remaining), (enemy_name, enemy_hp_remaining)


hero, enemy = show_status("Goku", 100, 100, "Freezer", 120, 120)   
    
    
    
    