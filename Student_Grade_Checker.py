import time

print('=-=' * 50)
print('Hello, student! Let’s see how you did in each term!')
print('=-=' * 50)

name = input('Enter your name: ').strip().title()
first = float(input("Enter your first term grade: "))
second = float(input("Enter your second term grade: "))
third = float(input("Enter your third term grade: "))
fourth = float(input("Enter your fourth term grade: "))

print('=-=' * 50)

print('PROCESSING', end='', flush=True)
for _ in range(4):
    print('.', end='', flush=True)
    time.sleep(0.6)

print('\n' + '=-=' * 50)

average = (first + second + third + fourth) / 4

if average < 5.0:
    print(f'Average {average:.2f} ➜ \033[1;31mFAILED\033[m: {name}')

elif 5.0 <= average < 7.0:
    print(f'Average {average:.2f} ➜ \033[1;33mRECOVERY\033[m: {name}')

else:
    print(f'Average {average:.2f} ➜ \033[1;32mPASSED\033[m: {name}')

print('=-=' * 50)
