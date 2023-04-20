import random
# Prompts the user for a level, n
# If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
# n digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

def main():
    tries = 3
    problems = 10
    score = 0
    level = get_level()
    while problems > 0 and tries > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        correct = False

        while tries > 0 and not correct:
            i = input(f'{x} + {y} = ')
            try:
                if int(i) != (x + y):
                    tries -= 1
                    print('EEE')
                    if tries == 0:
                        print(f'{x} + {y} = {x + y}')
                        problems -= 1
                        tries = 3
                        break
                else:
                    tries = 3
                    score += 1
                    problems -= 1
                    correct = True
            except ValueError:
                tries -= 1
                print('EEE')
    print('Score:', score)

def get_level():
    # wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
    got_level = False
    while not got_level:
        l = input("Level: ")
        try:
            level = int(l)
            if level < 1 or level > 3:
                raise ValueError
            else:
                got_level = True
        except ValueError:
            continue

    return level

def generate_integer(level):
    # generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()