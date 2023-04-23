import random


def roll():
    r = random.randint(1, 6)
    print(f"\n(You rolled a {r}!)\n")
    return r


def hurling_in_the_back_garden(player):
    if player.orcs < 1:
        print("There are no orcs to hurl potatoes at.\n")
        return False
    if player.potatoes < 1:
        print("You have no potatoes to hurl.\n")
        return False
    if player.potatoes < player.danger_level:
        print("You do not have enough potatoes to hurl.\n")
        return False
    else:
        print("You hurl a potato at an orc.\n")
        player.orcs -= 1
        player.potatoes -= player.danger_level
        return True


def grass_and_mud(player, dice_roll):
    match dice_roll:
        case 1 | 2:
            print("In the garden...")
            in_the_garden(player, roll())
        case 3 | 4:
            print("A knock at the door...")
            knock_at_door(player, roll())
        case 5 | 6:
            print(
                "The world becomes a darker, more dangerous place.\nFrom now on, removing an ORC costs an additional POTATO..\n(+1 DANGER LEVEL)\n"
            )
            dangerous_place(player)


def end_state(player):
    if player.potatoes >= 10:
        print(
            "! POTATO WIN !\nYou have enough potatoes that you can go underground and not return to the surface until the danger is past.\nYou nestle down into your burrow and enjoy your well-earned rest.\n"
        )
        player.state = "win"
        return True
    if player.destiny >= 10:
        print(
            f"! DESTINY WIN !\nAn interfering {random.choice(('bard', 'wizard'))} turns up at your doorstep with a quest,\nand you are whisked against your will on an adventure.\n"
        )
        player.state = "win"
        return True
    if player.orcs >= 10:
        print(
            "! GAME OVER !\nOrcs finally find your potato farm.\nAlas, orcs are not so interested in potatoes as they are in eating you,\nand you end up in a cookpot.\n"
        )
        player.state = "lose"
        return True

    return False


def in_the_garden(player, dice_roll):
    match dice_roll:
        case 1:
            print("You happily root about all day in your garden.\n(+1 POTATO)\n")
            player.potatoes += 1
        case 2:
            print(
                "You narrowly avoid a visitor by hiding in a potato sack.\n(+1 POTATO, +1 DESTINY)\n"
            )
            player.potatoes += 1
            player.destiny += 1
        case 3:
            print(
                "A hooded stranger lingers outside your farm.\n(+1 ORC, +1 DESTINY)\n"
            )
            player.destiny += 1
            player.orcs += 1
        case 4:
            print(
                "Your field is ravaged in the night by unseen enemies.\n(+1 ORC, -1 POTATO)\n"
            )
            player.orcs += 1
            player.potatoes -= 1
        case 5:
            print("You trade potatoes for other delicious foodstuffs.\n(-1 POTATO)\n")
            player.potatoes -= 1
        case 6:
            print(
                "You burrow into a bumper crop of potatoes.\nDo you cry with joy?\nPossibly.\n(+2 POTATOES)\n"
            )
            player.potatoes += 2


def knock_at_door(player, dice_roll):
    match dice_roll:
        case 1:
            print(
                "A distant cousin.\nThey are after your potatoes.\nThey may snitch on you.\n(+1 ORC)\n"
            )
            player.orcs += 1
        case 2:
            print(
                "A dwarven stranger.\nYou refuse them entry.\nGhastly creatures.\n(+1 DESTINY)\n"
            )
            player.destiny += 1
        case 3:
            print(
                "A wizard strolls by.\nYou pointedly draw the curtains.\n(+1 ORC, +1 DESTINY)\n"
            )
            player.orcs += 1
            player.destiny += 1
        case 4:
            print(
                "There are rumors of war in the reaches.\nYou eat some potatoes.\n(-1 POTATO, +2 ORCS)\n"
            )
            player.potatoes -= 1
            player.orcs += 2
        case 5:
            print("It's an elf.\nThey are not serious people.\n(+1 DESTINY)\n")
            player.destiny += 1
        case 6:
            print(
                "It's a sack of potatoes from a generous neighbor.\nYou really must remember to pay them a visit one of these years.\n(+1 POTATO)\n"
            )
            player.potatoes += 1


def dangerous_place(player):
    player.danger_level += 1
