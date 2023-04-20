def main():
    try:
        grocery_list = {}
        while True:
            item = input()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    except EOFError:
        for x in sorted(grocery_list):
            print(grocery_list[x], x.upper())

if __name__ == '__main__':
    main()