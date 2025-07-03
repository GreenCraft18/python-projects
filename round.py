import math
num = input("What number do you want the round to the nearest integer of? ")
numFloat = float(num)
up_or_down = input("Which way do you want to round? Up, Down, or Nearest? ")
if up_or_down.lower() == "up":
    result = math.ceil(numFloat)
    print(f"The number {numFloat} rounded up to the nearest integer is: {result}")
elif up_or_down.lower() == "down":
    result = math.floor(numFloat)
    print(f"The number {numFloat} rounded down to the nearest integer is: {result}")
elif up_or_down.lower() == "nearest":
    result = round(numFloat)
    print(f"The number {numFloat} rounded to the nearest integer is: {result}")
else:
    print("Please enter a valid option: Up, Down, or Nearest.")