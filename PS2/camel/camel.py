def main():
    x = input("camelCase: ")
    print(f"snake_case: {convert(x)}")

def convert(camel):
    snake = ''
    for count, c in enumerate(camel):
        if c.isupper():
            c = f"_{c}"
            c = c.lower()
        snake = snake + c

    return snake

main()