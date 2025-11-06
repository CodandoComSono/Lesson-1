print('\033[1;33m=-=' * 50)
print('\033[32m Number Comparator\033[m')
print('\033[1;33m=-=' * 50)

num1 = float(input('\033[1;32m Enter a number = \033[m'))
num2 = float(input('\033[32m Enter another number = \033[m'))

if num1 > num2:
    print(f'\033[32m The number {num1} is greater than {num2}!\033[m')

elif num2 > num1:
    print(f'\033[32m The number {num2} is greater than {num1}!\033[m')

else:
    print(f'\033[32m The numbers {num1} and {num2} are equal!\033[m')

print('\033[1;33m=-=' * 50)
