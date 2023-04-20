def main():
    fraction = input("Fraction: ")
    x, y = check(fraction)
    convert(x, y)
def check(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        return (x, y)

    except (ValueError, ZeroDivisionError):
        main()

def convert(x: int, y: int):
    result = x/y
    if result <= 0.01:
        print("E")
    elif result >= 0.99:
        print("F")
    else:
        print(f"{result*100:.0f}%")

if __name__ == '__main__':
    main()