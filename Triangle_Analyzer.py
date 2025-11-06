print('\033[1;34m=-=\033[m' * 20)
print('\033[1;36mTRIANGLE ANALYZER\033[m'.center(60))
print('\033[1;34m=-=\033[m' * 20)

side1 = float(input('\033[1mFirst segment: '))
side2 = float(input('Second segment: '))
side3 = float(input('Third segment: '))

print('\033[1;34m=-=\033[m' * 20)

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('\033[1;32mThe segments can form a triangle!\033[m')

    if side1 == side2 == side3:
        print('Type: \033[1;33mEQUILATERAL\033[m (all sides equal)')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Type: \033[1;33mISOSCELES\033[m (two sides equal)')
    else:
        print('Type: \033[1;33mSCALENE\033[m (all sides different)')
else:
    print('\033[1;31mThe segments CANNOT form a triangle.\033[m')

print('\033[1;34m=-=\033[m' * 20)
