#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = repr(number)
last_digit_str = string[-1]
last_digit = int(last_digit_str)
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit < 6:
       if last_digit != 0:
            print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
else last_digit = 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
