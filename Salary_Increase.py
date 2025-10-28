name = input('What is your name? ')
salary = float(input('Enter your salary: '))

increase = salary * 0.15
new_salary = salary + increase

print(f'Congratulations {name}, your new salary is now R${new_salary:.2f}!')
