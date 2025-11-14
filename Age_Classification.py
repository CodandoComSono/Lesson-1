from datetime import date

current_year = date.today().year
adults = 0
minors = 0

for i in range(1, 8):
    birth_year = int(input(f"Enter the birth year of person {i}: "))
    age = current_year - birth_year

    if age >= 18:
        adults += 1
    else:
        minors += 1

print(f"\nIn total, we have {adults} people who are adults.")
print(f"And we also have {minors} people who are minors.")
