#Calculator

from Art import logo
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  operation_symbol = input("Pick an operation: ")
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")

  more_operations = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")

  should_continue = True
  while should_continue == True:

    operation_symbol = input("Pick an operation: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    more_operations = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' starting a new calculation: ")
    first_answer = second_answer

    if more_operations == 'y':
      num1 = second_answer
    else:
      should_continue = False
      calculator()


calculator()

