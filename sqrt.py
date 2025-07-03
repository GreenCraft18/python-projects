import math

num = input("What number do you want the square root of? ")

if num == "pi":
    print("The square root of pi is approximately:", math.sqrt(math.pi))
elif num == "π":
    print("The square root of π is approximately:", math.sqrt(math.pi))
else:
    try:
        numfloat = float(num)
        if numfloat < 0.0:
            print("Sorry, but negative numbers aren't supported.")
        else:
            result = math.sqrt(numfloat)
            print(f"The square root of {numfloat} is exactly: {result}")
    except ValueError:
        print("Please enter a valid number.")