import random

# --- TUS FUNCIONES VISUALES ---
def hp_bar(current_hp, max_hp, bar_length=20):
    current_hp = max(0, current_hp) # Evita errores si la vida es negativa
    filled = int((current_hp / max_hp) * bar_length)
    empty = bar_length - filled
    bar = "#" * filled + "-" * empty
    return f"[{bar}] {current_hp}/{max_hp} HP"

def damage_generator(min_val=10, max_val=25):
    return random.randint(min_val, max_val)

# --- LÓGICA DEL JUEGO ---
def turn_hero(h_hp, e_hp, p, h_max, e_max):
    # Mostramos el estado antes de pedir la acción
    print(f"\nHERO:  {hp_bar(h_hp, h_max)}")
    print(f"ENEMY: {hp_bar(e_hp, e_max)}")
    
    action = input("Your turn (attack, skill, potion): ").lower()
    
    if action == "attack":
        dmg = damage_generator(10, 25)
        e_hp -= dmg
        print(f"Hero attacks! Damage: {dmg}")
        return h_hp, e_hp, p

    elif action == "skill":
        if random.randint(1, 2) == 1:
            dmg_s = damage_generator(30, 50)
            e_hp -= dmg_s
            print(f"Skill success! Damage: {dmg_s}")
        else:
            print("Hero missed the skill!")
        return h_hp, e_hp, p

    elif action == "potion":
        if p > 0:
            h_hp = min(h_max, h_hp + 20) # No sobrepasa la vida máxima
            p -= 1
            print(f"Hero uses potion! Potions left: {p}")
            return h_hp, e_hp, p
        else:
            print("No potions left! Choose again.")
            return turn_hero(h_hp, e_hp, p, h_max, e_max)

    else:
        print("Invalid option! Choose again.")
        return turn_hero(h_hp, e_hp, p, h_max, e_max)

def turn_enemy(h_hp):
    dmg_e = damage_generator(15, 20)
    h_hp -= dmg_e
    print(f"\nEnemy attacks! Damage received: {dmg_e}")
    return h_hp

def check_result(h_hp, e_hp):
    if e_hp <= 0:
        print(f"\nENEMY: {hp_bar(0, 120)}")
        print("--- YOU WIN ---")
        return True
    elif h_hp <= 0:
        print(f"\nHERO:  {hp_bar(0, 100)}")
        print("--- YOU LOSE ---")
        return True
    return False

# --- CONFIGURACIÓN Y BUCLE ---
hero_hp, hero_max = 100, 100
enemy_hp, enemy_max = 120, 120
potions = 3
game_over = False

while not game_over:
    # Turno Jugador
    hero_hp, enemy_hp, potions = turn_hero(hero_hp, enemy_hp, potions, hero_max, enemy_max)
    game_over = check_result(hero_hp, enemy_hp)
    
    if not game_over:
        # Turno Enemigo
        hero_hp = turn_enemy(hero_hp)
        game_over = check_result(hero_hp, enemy_hp)
