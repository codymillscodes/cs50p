from sys import exit
import os
from halfling import Halfling
import events
import hud


def start():
    title()
    print("1. Start\n2. Quit")
    choice = input("> ")
    if choice == "1":
        return True
    if choice == "2":
        return False
    print("Invalid input.")
    return start()


def title():
    line_length = 60
    game_name = '" P O T A T O "'
    game_desc = "A pen and paper RPG by Oliver Darkshire"
    game_desc2 = "Coded by Cody Mills"
    plot = f"{'-'*60}\nyou are a halfling, just trying to exist\nmeanwhile, the dark lord rampages across the world\n you do not care about this. you are trying to farm potatoes\n because what could a halfling possibly do about it anyway\n{'-'*60}\n"
    print(
        f"\n{game_name.center(line_length)}\n{game_desc.center(line_length)}\n{game_desc2.center(line_length)}"
    )
    lines = plot.split("\n")
    for line in lines:
        print(line.center(line_length))


def play(player):
    potato_str = "a potato"
    if player.danger_level > 1:
        potato_str = f"{player.danger_level} potatoes"
    print(f"\n1. Advance to the next day.\n2. Hurl {potato_str} at an orc.\n3. Quit")
    choice = input("> ")
    return choice


def game_loop(player, hud_style="basic_interface"):
    while not events.end_state(player):
        print(hud.display(player, hud_style))
        player_input = play(player)
        if player_input == "1":
            events.grass_and_mud(player, events.roll())
            player.turn += 1
        elif player_input == "2":
            hurled = events.hurling_in_the_back_garden(player)
            if hurled:
                player.turn += 1
        elif player_input == "3":
            print("See ya!")
            exit(0)
    print(hud.display(player, hud_style))


def play_again(player):
    choice = input("Play again? (y/n)\n> ")
    if choice[0].lower() == "y":
        print("\n")
        player.reset()
        return
    if choice[0].lower() == "n":
        print("See ya!")
        exit(0)
    print('Invalid input. Please enter "y" or "n".')
    play_again(player)


def main():
    player = Halfling()
    if start():
        hud_style = hud.choose_style()
        while True:
            game_loop(player, hud_style)
            play_again(player)
    else:
        print("See ya!")
        exit(0)


if __name__ == "__main__":
    main()
