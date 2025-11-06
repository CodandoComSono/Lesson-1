from datetime import date

name = input('Please enter your name: ').strip().title()
birth_year = int(input('Enter your year of birth: '))

current_year = date.today().year
age = current_year - birth_year
enlistment_year = current_year + (18 - age)

if age == 18:
    print(f'Candidate {name}, it is time for your enlistment! Please report to a military office.')

elif age < 18:
    print(f'Candidate {name}, there are still {18 - age} year(s) left until enlistment!')
    print(f'Candidate {name}, your enlistment year will be {enlistment_year}.')

else:
    print(f'Candidate {name}, you should have enlisted {age - 18} year(s) ago! Please report to a military office.')
    print(f'Candidate {name}, the year you should have enlisted was {enlistment_year}.')
