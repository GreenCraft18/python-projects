import math

def format_float_with_commas(number):
    return "{:,.2f}".format(result)

print("Hello, Python user! This is a simple Python program to add, subtract, multiply, and divide two numbers. Or, you can raise a number to a power, calculate the square root of a number, or round a number to the nearest integer.")

operation = input("Python user, what type of operation would you like to perform? ")

if operation.lower == "add":
    number1 = input("Python user, please enter the first number you want to add. ")
    number2 = input("Python user, now please enter the second number you want to add. ")
    result = float(number1) + float(number2)
    print(f"The result of adding {number1} and {number2} is {format_float_with_commas(result)}.")
elif operation.lower == "subtract":
    number1 = input("Python user, please enter the first number you want to subtract. ")
    number2 = input("Python user, now please enter the second number you want to subtract. ")
    result = float(number1) - float(number2)
    print(f"The result of subtracting {number2} from {number1} is {format_float_with_commas(result)}.")
elif operation.lower == "multiply":
    number1 = input("Python user, please enter the first number you want to multiply. ")
    number2 = input("Python user, now please enter the second number you want to multiply. ")
    result = float(number1) * float(number2)
    print(f"The result of multiplying {number1} and {number2} is {format_float_with_commas(result)}.")
elif operation == "divide":
    number1 = input("Python user, please enter the first number you want to divide. ")
    number2 = input("Python user, now please enter the second number you want to divide. ")
    if float(number2) == 0:
        print("Python user, you cannot divide by zero. Please try again.")
        exit()
    else:
        result = float(number1) / float(number2)
        print(f"The result of dividing {number1} by {number2} is {format_float_with_commas(result)}.")
elif operation == "power":
    number1 = input("Python user, please enter the base number: ")
    number2 = input("Python user, now please enter the exponent: ")
    result = float(number1) ** float(number2)
    print(f"The result of raising {number1} to the power of {number2} is {format_float_with_commas(result)}.")
elif operation == "round":
    operation_ing = "rounding"
    number = input("Python user, please enter the number you want to round: ")
    roundType = input("Python user, would you like to round down, up, or round to the closest integer nearby? ")
    if roundType.lower() == "down":
        result = math.floor(float(number))
        print(f"The result of rounding {number} down to the nearest integer is {format_float_with_commas(result)}.")
    elif roundType.lower() == "up":
        result = math.ceil(float(number))
        print(f"The result of rounding {number} up to the nearest integer is {format_float_with_commas(result)}.")
    elif roundType.lower() == "closest":
        result = round(float(number))
        print(f"The result of rounding {number} to the nearest integer is {format_float_with_commas(result)}.")
    else:
        print("Python user, you have entered an invalid rounding type. Please try again.")
        exit()
elif operation == "sqrt":
    number1 = input("Python user, please enter the number you want to find the square root of: ")
    result = math.sqrt(float(number1))
    print(f"The result of calculating the sq. rt of {number1} is {format_float_with_commas(result)}.")
else:
    print("Python user, you have entered an invalid operation. Please try again.")
    exit()