# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Used to call the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operand in operations:
    print(operand)

operation = input("Pick an operation from the line above: ")

# tap into the dictionary and use [] to pass in the operation symbol and store user input
# Operation: stores the users input
# operations[operation]: This part of the line is using the value stored in the operation variable as a key to look up a value in the operations dictionary
calculation_function = operations[operation]

answer = calculation_function(num1, num2)

print(f"{num1} {operation} {num2} = {answer}")






