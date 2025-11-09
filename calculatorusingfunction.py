



ch ki bu. h nn cc nj. ch ni. ch n









num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))
operations = ['add', 'sub', 'multiply', 'divide']
c = input("Choose Your Operation (addition, subtration, multiply, divide) : ")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    if b == 0:
        return "Error: Division by zero"
    return a / b

result = None
if c in operations:
    if c == 'addition':
        result = add(num1, num2)
    elif c == 'subbtration':
        result = sub(num1, num2)
    elif c == 'multiply':
        result = multiply(num1, num2)
    elif c == 'divide':
        result = divide(num1, num2)
    print(f"The result of {c} is: {result}")
else:
    print("Invalid operation chosen.")
