import time

colors = {
    "reset": '\033[m',
    "blue": '\033[1;34m',
    "cyan": '\033[1;36m',
    "yellow": '\033[1;33m',
    "red": '\033[1;31m',
    "green": '\033[1;32m',
    "black": '\033[1;30m',
    "red_bg": '\033[1;41m',
    "bold": '\033[1;m',
    "highlight": '\033[1;30;47m',
}

print(f'{colors["blue"]}=' * 90)
print(f'{colors["cyan"]}You are your best project. Have a day full of energy and health!{colors["reset"]}'.center(100))
print(f'{colors["blue"]}Let’s calculate your BMI and see how your health is doing!{colors["reset"]}'.center(100))
print(f'{colors["blue"]}=' * 90)

name = input(f'{colors["green"]}Enter your name: {colors["reset"]}').strip().title()
weight = float(input(f'{colors["green"]}Enter your weight, {name}: {colors["reset"]}'))
height = float(input(f'{colors["green"]}Enter your height, {name}: {colors["reset"]}'))

print(f'{colors["blue"]}=' * 90)

print('CALCULATING', end='', flush=True)
for _ in range(4):
    print('.', end='', flush=True)
    time.sleep(0.6)

print('\n' + f'{colors["blue"]}={colors["reset"]}' * 90)

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'{colors["yellow"]}ATTENTION! {name}, you are underweight!{colors["reset"]}')
    print(f'{colors["highlight"]}Your BMI is {bmi:.1f}{colors["reset"]}')

elif 18.5 <= bmi < 25:
    print(f'{colors["green"]}CONGRATULATIONS! {name}, you are at an ideal weight!{colors["reset"]}')
    print(f'{colors["highlight"]}Your BMI is {bmi:.1f}{colors["reset"]}')

elif 25 <= bmi < 30:
    print(f'{colors["yellow"]}ATTENTION! {name}, you are overweight!{colors["reset"]}')
    print(f'{colors["highlight"]}Your BMI is {bmi:.1f}{colors["reset"]}')

elif 30 <= bmi < 40:
    print(f'{colors["red"]}HIGH ATTENTION! {name}, you are obese!{colors["reset"]}')
    print(f'{colors["highlight"]}Your BMI is {bmi:.1f}{colors["reset"]}')

else:
    print(f'{colors["red_bg"]}EXTREME ATTENTION! {name}, you are severely obese!{colors["reset"]}')
    print(f'{colors["highlight"]}Your BMI is {bmi:.1f}{colors["reset"]}')
