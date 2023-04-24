# Potato
#### Video Demo:  https://youtu.be/gNQm9_jIPJY
### Description:
#### Introduction:

Welcome to my project, "Potato", a pen and paper RPG coded in Python. The game revolves around a halfling player who attempts to grow potatoes while defending them from orcs. The game has a turn-based structure, and the player's goal is to accumulate as many potatoes as possible while keeping the danger level low.

#### Files:

main.py: This file is the main driver for the game. It contains functions to start, play, and restart the game. The game_loop function is the core of the game, which runs the game's main loop.

halfling.py: This file contains the Halfling class, which initializes the game's player and has methods to get and set various player attributes such as destiny, potatoes, orcs, and danger level. The class also has a reset method to reset the game state.

events.py: This file contains functions that simulate the events that occur in the game. The functions include grass_and_mud, knock_at_door, and in_the_garden. These functions are called by the game_loop function.

hud.py: This file contains functions to display the game's status to the player. It includes four different HUD styles: basic_style, minimal_style, emoji_style, and fancy_style. The choose_style function allows the player to select the preferred HUD style.

#### Explanation of Functions:

start() function: This function displays the game's title and prompts the player to start or quit the game. If the player chooses to start, the function returns True, and the game begins. If the player chooses to quit, the function returns False, and the game ends.

title() function: This function displays the game's title and description, followed by the game's plot.

play(player) function: This function prompts the player to choose an action and returns the player's choice.

game_loop(player, hud_style) function: This function runs the main loop of the game. It displays the player's status using the HUD style selected by the player and prompts the player to select an action. The function then calls the appropriate event function based on the player's choice.

play_again(player) function: This function prompts the player to play again or quit the game. If the player chooses to play again, the function resets the game state and returns. If the player chooses to quit, the function exits the game.

Halfling class: This class initializes the player's attributes and has methods to get and set the player's attributes. The class also has a reset method to reset the game state.

get_stats(player) function: This function returns a dictionary containing the player's attributes.

display(player, style) function: This function displays the player's status using the HUD style selected by the player.

choose_style() function: This function prompts the player to select a HUD style and returns the selected style.

roll() function: This function simulates a dice roll and returns the result.

hurling_in_the_back_garden(player) function: This function simulates the player hurling potatoes at orcs in the garden. It checks if the player has enough potatoes and returns True if the potatoes are hurled successfully.

grass_and_mud(player, dice_roll) function: This function simulates events that occur in the garden, at the door, or in dangerous places. The function calls the appropriate event function based on the dice roll.

end_state(player) function: This function returns True if the game ends due to the player winning or losing.

