import random

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
draw = random.sample(groups, 4)

print(f'The first group drawn is... {draw[0]}')
print(f'The second group drawn is... {draw[1]}')
print(f'The third group drawn is... {draw[2]}')
print(f'The fourth group drawn is... {draw[3]}')
