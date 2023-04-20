i = input('Expression: ')
i = i.split(' ')
i[0] = int(i[0])
i[2] = int(i[2])
if i[1] == '+':
    print(float(i[0] + i[2]))
elif i[1] == '-':
    print(float(i[0] - i[2]))
elif i[1] == '*':
    print(float(i[0] * i[2]))
elif i[1] == '/':
    print(float(i[0] / i[2]))