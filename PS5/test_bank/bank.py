def main():
    greeting = input("Greeting: ")
    v = value(greeting)
    print(f'${v}')

def value(greeting: str):
    g = greeting.lower().strip()
    if g[0] == 'h':
        if g.startswith('hello'):
            return 0
        else:
            return 20
    if g[0] != 'h':
        return 100

if __name__ == '__main__':
    main()