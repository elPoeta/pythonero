expression = input()
x, y, z = expression.split(' ')

x = int(x)
z = int(z)

if y == '+':
    print(f'{(x + z):.2f}')
elif y == '-':
    print(f'{(x - z):.2f}')
elif y == '*':
    print(f'{(x * z):.2f}')
elif y == '/':
    if z != 0:
        print(f'{(x / z):.2f}')
else:
    print('wrong operstor')
