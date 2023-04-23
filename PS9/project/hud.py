def get_stats(player):
    return {
        "potatoes": player.potatoes,
        "max_potatoes": player.max_potatoes,
        "destiny": player.destiny,
        "max_destiny": player.max_destiny,
        "orcs": player.orcs,
        "max_orcs": player.max_orcs,
        "turn": player.turn,
        "danger_level": player.danger_level,
    }


def display(player, style):
    if style == "basic_style":
        return basic_style(player)
    if style == "minimal_style":
        return minimal_style(player)
    if style == "emoji_style":
        return emoji_style(player)
    if style == "fancy_style":
        return fancy_style(player)


def choose_style():
    print("Choose a HUD style:")
    print("1. Basic")
    print("2. Minimal (for small screens)")
    print("3. Emoji (for small screens)")
    print("4. Fancy (for large screens)")
    choice = input("> ")
    if choice == "1":
        return "basic_style"
    if choice == "2":
        return "minimal_style"
    if choice == "3":
        return "emoji_style"
    if choice == "4":
        return "fancy_style"
    print("Invalid choice")
    return choose_style()


def fancy_style(player):
    h_length = 88
    turn_danger_spacing = 91
    stats = player.stats

    turn_danger = f"| Turn {stats['turn']} | Danger Level: {stats['danger_level']}"
    return (
        f"+-{' ' * h_length}-+\n{turn_danger}{' ' * (turn_danger_spacing - len(turn_danger))}|\n"
        f"| Potatoes: [{'|' * stats['potatoes']}{' ' * (stats['max_potatoes'] - stats['potatoes'])}] ({stats['potatoes']}/10) | "
        f"Destiny: [{'|' * stats['destiny']}{' ' * (stats['max_destiny'] - stats['destiny'])}] ({stats['destiny']}/10) | "
        f"Orcs: [{'|'*stats['orcs']}{' '*(stats['max_orcs'] - stats['orcs'])}] ({stats['orcs']}/10) |\n+-{' ' * h_length}-+"
    )


def minimal_style(player):
    stats = player.stats
    return f"T: {stats['turn']} | D: {stats['danger_level']}\nP: {stats['potatoes']}/{stats['max_potatoes']} | D: {stats['destiny']}/{stats['max_destiny']} | O: {stats['orcs']}/{stats['max_orcs']}"


def basic_style(player):
    stats = player.stats
    return f"Turn: {stats['turn']} | Danger Level: {stats['danger_level']}\nPotatoes: {stats['potatoes']}/{stats['max_potatoes']} | Destiny: {stats['destiny']}/{stats['max_destiny']} | Orcs: {stats['orcs']}/{stats['max_orcs']}"


def emoji_style(player):
    stats = player.stats
    return f"🔄: {stats['turn']} | ☠️: {stats['danger_level']}\n🥔: {stats['potatoes']}/{stats['max_potatoes']} | ⚔️: {stats['destiny']}/{stats['max_destiny']} | 🤢: {stats['orcs']}/{stats['max_orcs']}"
