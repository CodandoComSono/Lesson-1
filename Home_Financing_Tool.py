print('=-='*50)
print(' ')
print('Welcome to the Loan Simulator!')
print(' ')
print('=-='*50)

property_value = float(input('\033[1;32mPlease enter the property value: $'))
salary = float(input('\033[1;32mPlease enter your salary: $'))
years = int(input('\033[1;32mPlease enter how many years you wish to pay: \033[m'))

import time

print('\033[1;34mAnalyzing your proposal', end='', flush=True)
for i in range(4):
    print('.', end='', flush=True)
    time.sleep(0.6)
print('\033[0m\n')

installments = years * 12
monthly_payment = property_value / installments
limit = salary * 0.30

if monthly_payment <= limit:
    print(f'\033[1;32mLoan APPROVED! Monthly payment: ${monthly_payment:.2f}')
else:
    print(f'\033[1;31mLoan DENIED! The payment of ${monthly_payment:.2f} exceeds 30% of your salary.')
