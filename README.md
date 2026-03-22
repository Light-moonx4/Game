# Game
⚔️ Documentation: RPG Battle System (Python)
This program is a turn-based combat simulator between a Hero and an Enemy. It includes random damage mechanics, critical hits, resource management (potions), and simple artificial intelligence logic for the enemy.
🛠️ Function Structure
1. Visual and Calculation Functions
hp_bar(current_hp, max_hp, bar_length): Generates a visual representation of health using emojis (🟦) and characters. It normalizes the value so it never drops below 0.
damage_generator(min_val, max_val): Uses the random library to return an integer within a defined damage range.
crit(damage): Probability system. It has a 10% chance to double the damage received.
2. Turn Logic
turn_hero(...): Manages user interaction. It allows three actions:
attack: Constant damage with a chance for a critical hit.
skill: High-risk attack (50% chance to hit) but with much higher damage.
potion: Healing system (+20 HP) limited by an inventory counter.
turn_enemy(...): Automated logic.
Healing Priority: If the enemy's health is ≤ 24, it heals automatically once per game.
Attack: If it doesn't heal, it performs a standard attack against the hero.
3. Game Control
check_result(...): Evaluates if either combatant has reached 0 HP to stop the game loop and declare a winner.
🎮 Execution Flow (Main Loop)
The game uses a while not game_over loop that follows this order:
Current Status: Updated health bars are displayed.
Player Action: Input pauses the game until the user chooses a valid action.
Verification: Checks if the enemy died.
Enemy Action: The enemy attacks or heals.
Final Verification: Checks if the hero died.
📋 Technical Specifications
Attribute	Hero	Enemy
Max HP	100 HP	120 HP
Base Damage	10 - 25	15 - 20
Special Skill	30 - 50 (50% accuracy)	N/A
Healing	3 Potions (+20 HP each)	Once (+30 HP) if HP < 25
Crit Chance	10% (x2 Damage)	10% (x2 Damage)
