gender = None

while gender not in ["M", "F"]:
    gender = input("Enter your gender (M/F): ").upper().strip()

    if gender == "M":
        print("You are Male.")
    elif gender == "F":
        print("You are Female.")
    else:
        print("Please enter only M or F!")

print("Thank you for using the program!")
