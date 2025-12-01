adults = 0
men = 0
women_under_20 = 0

while True:
    age = int(input("Enter your age: "))
    gender = input("Enter your gender [M/F]: ").strip().upper()
    
    if age >= 18:
        adults += 1

    if gender == "M":
        men += 1

    if gender == "F" and age < 20:
        women_under_20 += 1

    continue_option = input("Do you want to continue? [Y/N]: ").strip().upper()
    if continue_option == "N":
        break

print(f"Total number of people over 18: {adults}")
print(f"Total number of men: {men}")
print(f"Total number of women under 20: {women_under_20}")
