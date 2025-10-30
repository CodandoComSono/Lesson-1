import math

# ask for the angle
angle = float(input('Enter the angle in degrees: '))

# convert to radians
rad = math.radians(angle)

# calculate sine, cosine, and tangent
sine = math.sin(rad)
cosine = math.cos(rad)
tangent = math.tan(rad)

# display the results
print(f'The angle of {angle}° has:')
print(f'Sine = {sine:.2f}')
print(f'Cosine = {cosine:.2f}')
print(f'Tangent = {tangent:.2f}')
