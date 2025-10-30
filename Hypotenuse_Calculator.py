import math

opposite = float(input('Enter the length of the opposite side (a): '))
adjacent = float(input('Enter the length of the adjacent side (b): '))

hypotenuse = math.hypot(opposite, adjacent)

print(f'The hypotenuse is: {hypotenuse:.2f}')
