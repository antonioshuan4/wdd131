import math

print("python boxes.py")

number1 = int(input("the number of items: "))
number2 = int(input("the number of items per box: "))

answer = math.ceil(number1 / number2)

print(f"for {number1} items, packing {number2} in each box, you will need {answer} boxes.")
