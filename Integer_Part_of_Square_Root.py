import math

number = float(input('Enter a number: '))
square_root = math.sqrt(number)

print(f'The number {number} has an integer part of {math.trunc(square_root)}.')
