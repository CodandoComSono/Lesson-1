import time
from datetime import date

print('\033[1;34m=-=' * 20)
print('\033[1;36m WELCOME TO THE CATEGORY CLASSIFIER '.center(60))
print('\033[1;34m=-=' * 20 + '\033[m')

name = input("\033[1;mEnter your name: \033[m").strip().title()
birth_year = int(input("\033[1;mEnter your year of birth: \033[m"))

current_year = date.today().year
age = current_year - birth_year

print('\033[1;34m=-=\033[m' * 20)

print('PROCESSING', end='', flush=True)
for _ in range(4):
    print('.', end='', flush=True)
    time.sleep(0.6)

print('\n' + '\033[1;34m=-=\033[m' * 20)

if age <= 9:
    print(f'{name}, you are {age} years old.')
    print(f'{name}, you belong to the \033[1;33mMIRIM\033[m category!')

elif age <= 14:
    print(f'{name}, you are {age} years old.')
    print(f'{name}, you belong to the \033[1;33mCHILD\033[m category!')

elif age <= 19:
    print(f'{name}, you are {age} years old.')
    print(f'{name}, you belong to the \033[1;33mJUNIOR\033[m category!')

elif age <= 25:
    print(f'{name}, you are {age} years old.')
    print(f'{name}, you belong to the \033[1;33mSENIOR\033[m category!')

else:
    print(f'{name}, you are {age} years old.')
    print(f'{name}, you belong to the \033[1;33mMASTER\033[m category!')

print('\033[1;34m' + '=-=' * 20)
