print('=-=' * 50)
print('Number Base Converter')
print('=-=' * 50)

num = int(input('Enter an integer: '))

print('''Choose one of the bases for conversion:
[ 1 ] Binary
[ 2 ] Octal
[ 3 ] Hexadecimal''')

option = int(input('Your choice: '))

if option == 1:
    print(f'{num} converted to BINARY is {bin(num)[2:]}')
elif option == 2:
    print(f'{num} converted to OCTAL is {oct(num)[2:]}')
elif option == 3:
    print(f'{num} converted to HEXADECIMAL is {hex(num)[2:].upper()}')
else:
    print('Invalid option! Please try again.')

print('=-=' * 50)
