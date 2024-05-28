# Basic Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

choice = int(input('\n Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: '))

num1 = int(input('\n Enter your first number: '))
num2 = int(input('\n Enter your second number: '))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == 3:
    print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == 4:
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Invalid choice')

