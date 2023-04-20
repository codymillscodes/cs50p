g = input('Greeting: ')
g = g.lower().strip()
if g[0] == 'h':
    if g.startswith('hello'):
        print('$0')
    else:
        print('$20')
if g[0] != 'h':
    print('$100')