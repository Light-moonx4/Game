import random

# --- VISUAL FUNCTIONS 🎨 ---
def hp_bar(current_hp, max_hp, bar_length=20):
    current_hp = max(0, current_hp)  # Prevent negative HP errors
    filled = int((current_hp / max_hp) * bar_length)
    empty = bar_length - filled
    bar = "🟦" * filled + "-" * empty
    return f"[{bar}] {current_hp}/{max_hp} HP"

def damage_generator(min_val=10, max_val=25):
    return random.randint(min_val, max_val)

# --- CRITICAL HIT SYSTEM 💥 ---
def crit(damage):
    if random.randint(1, 10) == 1:  # 10% chance 🎲
        print("💥 CRITICAL HIT! x2 DAMAGE 🔥")
        return damage * 2
    return damage

# --- GAME LOGIC 🎮 ---
def turn_hero(h_hp, e_hp, p, h_max, e_max):
    # Show current status before action 👀
    print(f"\n🧙 HERO:  {hp_bar(h_hp, h_max)}")
    print(f"👾 ENEMY: {hp_bar(e_hp, e_max)}")
    
    action = input("Your turn (attack, skill, potion): ").lower()
    
    if action == "attack":
        # Basic attack with possible critical ⚔️
        dmg = crit(damage_generator(10, 25))
        e_hp -= dmg
        print(f"⚔️ Hero attacks! Damage: {dmg}")
        return h_hp, e_hp, p

    elif action == "skill":
        # 50% chance to hit 🎯
        if random.randint(1, 2) == 1:
            dmg_s = crit(damage_generator(30, 50))  # Stronger attack 💣
            e_hp -= dmg_s
            print(f"✨ Skill success! Damage: {dmg_s}")
        else:
            print("❌ Hero missed the skill!")
        return h_hp, e_hp, p

    elif action == "potion":
        # Heal if potions are available 🧪
        if p > 0:
            h_hp = min(h_max, h_hp + 20)  # Do not exceed max HP
            p -= 1
            print(f"🧪 Hero uses potion! Potions left: {p}")
            return h_hp, e_hp, p
        else:
            print("🚫 No potions left! Choose again.")
            return turn_hero(h_hp, e_hp, p, h_max, e_max)

    else:
        print("⚠️ Invalid option! Choose again.")
        return turn_hero(h_hp, e_hp, p, h_max, e_max)

def turn_enemy(h_hp, e_hp, e_max, enemy_healed):
    # Enemy heals once when HP is low ❤️‍🩹
    if e_hp <= 24 and not enemy_healed:
        heal = 30
        e_hp = min(e_max, e_hp + heal)
        enemy_healed = True
        print(f"\n👾 Enemy heals {heal} HP! (ONLY ONCE) ❤️‍🩹")
    else:
        # Enemy attacks with possible critical 💥
        dmg_e = crit(damage_generator(15, 20))
        h_hp -= dmg_e
        print(f"\n👾 Enemy attacks! Damage received: {dmg_e}")
        
    return h_hp, e_hp, enemy_healed

def check_result(h_hp, e_hp):
    # Check win/lose conditions 🏁
    if e_hp <= 0:
        print(f"\n👾 ENEMY: {hp_bar(0, 120)}")
        print("🏆 --- YOU WIN --- 🎉")
        return True
    elif h_hp <= 0:
        print(f"\n🧙 HERO:  {hp_bar(0, 100)}")
        print("💀 --- YOU LOSE ---")
        return True
    return False

# --- GAME SETUP ⚙️ ---
hero_hp, hero_max = 100, 100
enemy_hp, enemy_max = 120, 120
potions = 3
game_over = False
enemy_healed = False  # Tracks if enemy already healed 🔁

# --- MAIN GAME LOOP 🔄 ---
while not game_over:
    # Player turn 🧙
    hero_hp, enemy_hp, potions = turn_hero(hero_hp, enemy_hp, potions, hero_max, enemy_max)
    game_over = check_result(hero_hp, enemy_hp)
    
    if not game_over:
        # Enemy turn 👾
        hero_hp, enemy_hp, enemy_healed = turn_enemy(hero_hp, enemy_hp, enemy_max, enemy_healed)
        game_over = check_result(hero_hp, enemy_hp)