def main():
    tweet = input("Input: ")

def shorten(word: str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for v in vowels:
        word = word.replace(v, '')
    return word

if __name__ == '__main__':
    main()