#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
number = num % 10
if num < 0:
    num = num * -1
    number = (num % 10) * -1
    num = num * -1
if number > 5:
    print(f"Last digit of {num} is {number} and is greater than 5")
elif number == 0:
    print(f"Last digit of {num} is {number} and is 0")
else:
    print(f"Last digit of {num} is {number} and is less than 6 and not 0")
