import sys

def main():
    fraction = input("Fraction: ")
    p = convert(fraction)
    print(p)

def convert(fraction: str):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        return (x/y)*100

    except (ValueError, ZeroDivisionError):
        sys.exit(1)

def gauge(percentage: int):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == '__main__':
    main()