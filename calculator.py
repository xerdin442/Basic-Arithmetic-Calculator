import re

print('BASIC ARITHMETIC CALCULATOR')
print('Addition(+) Subtraction(-) Multiplication(*) Division(/) Modulus(%)')
print("Type 'quit' to exit")

run = True


def calculate():
    global run
    previous = 0
    while run:
        if previous == 0:
            equation = input('Enter equation: ')
        else:
            equation = input('Next equation: ')
        
        if equation == 'quit':
            print('Goodbye!')
            run = False
        
        try:
            equation = re.sub('[".:;,!()a-zA-Z]', '', equation)
            previous = eval(equation)
            print('Answer: ', previous)
        except ZeroDivisionError:
            print('ERROR, Division by Zero')

calculate()