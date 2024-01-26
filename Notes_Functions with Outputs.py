# Functions with Outputs - Python Notes

# 1. Defining a Function with Output
def add(a, b):
    return a + b

# 2. Calling a Function with Output
result = add(5, 3)

# 3. Multiple Outputs
def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result_quotient, result_remainder = divide_and_remainder(10, 3)

# 4. Default Return Value
def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"

# 5. Returning Multiple Data Types
def check_number_type(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 6. Returning Lists, Dictionaries, etc.
def create_list_and_dict():
    my_list = [1, 2, 3]
    my_dict = {"key": "value"}
    return my_list, my_dict

result_list, result_dict = create_list_and_dict()

# 7. Using the Return Value
output_message = greet("Alice")
number_type = check_number_type(7)
