#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rest = number%2
if (rest > 5):
    printf(f'Last digit of {number} is {rest} and is greater than 5')
elif rest == 0:
    printf(f'Last digit of {number} is {rest} and is 0')
else :
    printf(f'Last digit of {number} is {rest} and is less than 6 and not 0')
