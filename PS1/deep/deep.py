i = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

i = i.replace('-', '').replace(' ', '').lower()
if i == '42' or i == 'fortytwo':
    print('Yes')
else:
    print('No')