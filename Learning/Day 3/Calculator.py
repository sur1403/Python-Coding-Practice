# Define functions for different operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Create a dictionary mapping operators to functions
switcher = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Get user input for operation and numbers
operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on user input
if operator in switcher:
    result = switcher[operator](num1, num2)
    print("Result:", result)
else:
    print("Invalid operator")





#2 way

# import operator

# a = float(input("Enter first number:"))
# b = float(input("Enter first number:"))

# switcher = {
#     '+': operator.add,
#     '-': operator.sub,
#     '/': operator.truediv,
#     '*': operator.mul
# }

# def operator_func(operation):
#     operator_func = switcher.get(operation)

#     if operator_func is None:
#         return "Invalid case"
#     return operator_func(a,b)

# print(operator_func('+'))
# print(operator_func('-'))
# print(operator_func('/'))
# print(operator_func('*'))
