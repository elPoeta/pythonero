import re

previous = 0
run = True

print('Type q to exit.')


def calculate():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input("0")
    else:
        equation = input(str(previous))

    if equation == 'q':
        print('Bye!!')
        run = False
        return

    equation = re.sub('[a-zA-Z,.:" "]', '', equation)

    previous = eval(equation) if previous == 0 else eval(
        str(previous) + equation)


while run:
    calculate()
