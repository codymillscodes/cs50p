from random import randint

def main():
    not_guessed = True
    level = 0
    n = 0
    while not_guessed:
        while level == 0:
            l = input("Level: ")
            try:
                level = int(l)
                n = randint(1, level)
            except ValueError:
                continue
        g = input("Guess: ")
        try:
            guess = int(g)
        except ValueError:
            continue

        if guess > n:
            print('Too large!')
        elif guess < n:
            print('Too small!')
        elif guess == n:
            print('Just right!')
            not_guessed = False

if __name__ == '__main__':
    main()