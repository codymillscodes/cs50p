import inflect

def main():
    bid_adieu = 'Adieu, adieu, to '
    names = []
    inf = inflect.engine()
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        if len(names) == 1:
            print(f'{bid_adieu}{names[0]}')
        elif len(names) > 1:
            print(f'{bid_adieu}{inf.join(names)}')

main()