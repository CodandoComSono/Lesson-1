import time

colors = {
    "clear": '\033[m',
    "blue": '\033[1;34m',
    "cyan": '\033[1;36m',
    "yellow": '\033[1;33m',
    "red": '\033[1;31m',
    "green": '\033[1;32m',
    "black": '\033[1;30m',
    "red_background": '\033[1;41m',
    "bold": '\033[1;m',
    "background": '\033[1;30;47m',
}

print(f'{colors["blue"]}=-={colors["clear"]}' * 20)
print(f'{colors["cyan"]}COUNTDOWN TIMER{colors["clear"]}'.center(70))
print(f'{colors["blue"]}=-={colors["clear"]}' * 20)

for c in range(10, -1, -1):
    print(f'{colors["green"]}{c}{colors["clear"]}')
    time.sleep(1)

print(f'{colors["red"]}FIREWORKS!{colors["clear"]}')
