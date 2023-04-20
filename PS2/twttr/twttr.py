def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    tweet = input("Input: ")
    for v in vowels:
        tweet = tweet.replace(v, '')
    print(f"Output: {tweet}")

main()