colors = {
    "clear": '\033[m',
    "blue": '\033[1;34m',
    "cyan": '\033[1;36m',
    "yellow": '\033[1;33m',
    "red": '\033[1;31m',
    "green": '\033[1;32m',
    "black": '\033[1;30m',
    "red_bg": '\033[1;41m',
    "bold": '\033[1;m',
    "bg": '\033[1;30;47m',
}

print(f'{colors["blue"]}=-={colors["clear"]}' * 20)
print(f'{colors["cyan"]}Multiplication Table{colors["clear"]}'.center(70))
print(f'{colors["blue"]}=-={colors["clear"]}' * 20)

print(' ')

number = int(input(f'{colors["cyan"]}Enter a number to see its multiplication table:{colors["clear"]}'))

print(' ')

print(f'{colors["blue"]}={colors["clear"]}' * 20)
print(f'{colors["cyan"]}Table of {number}{colors["clear"]}'.center(30))
print(f'{colors["blue"]}={colors["clear"]}' * 20)

for count in range(1, 11):
    print(f'{number} x {count:2} = {number * count}')

print(f'{colors["blue"]}={colors["clear"]}' * 20)
