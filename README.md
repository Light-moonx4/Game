# Game
juego avanced
This is a console-based turn-based combat game. 
The player controls a "Hero" (100 HP) against an "Enemy" (120 HP). The game ends when either combatant's health reaches zero.
Core Functions
hp_bar(current_hp, max_hp): Generates a visual bar (using # and -) to represent current health. It ensures the value never drops below 0.
damage_generator(min, max): Uses the random library to calculate an integer damage value within the provided range.
turn_hero(h_hp, e_hp, p, h_max, e_max):
Manages player choices: Attack (steady damage), Skill (50% chance for massive damage), and Potion (heals 20 HP).
Uses recursion (calls itself) if the player picks an invalid option or has no potions, preventing them from losing their turn.
turn_enemy(h_hp): Calculates and subtracts enemy damage from the hero's health.
check_result(h_hp, e_hp): Checks if either combatant has died to stop the main loop.
Loop Structure
The game runs inside a while not game_over loop. The hero's turn executes first, followed by a victory check; if the game continues, the enemy's turn executes, followed by a defeat check.
