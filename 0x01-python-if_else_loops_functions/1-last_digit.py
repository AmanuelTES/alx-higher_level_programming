#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = repr(number)
last_digit = int(string[-1])
if number > 0:
    if last_digit > 5:
        print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif number < 0:
    if last_digit != 0:
        last_digit = last_digit * -1
        print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
