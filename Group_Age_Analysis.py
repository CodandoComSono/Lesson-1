total_age = 0
women_under_20 = 0
oldest_man_name = None
oldest_man_age = 0

for i in range(1, 5):
    name = input(f"Enter the name of person {i}: ").strip().title()
    age = int(input("Enter the age: "))
    gender = input("Enter the gender [M/F]: ").strip().upper()

    total_age += age

    if gender == "F" and age < 20:
        women_under_20 += 1

    # check oldest man
    if gender == "M":
        if oldest_man_name is None or age > oldest_man_age:
            oldest_man_name = name
            oldest_man_age = age

average_age = total_age / 4

print("\n" + "=" * 40)
print(f"Average age of the group: {average_age:.1f} years")

if oldest_man_name:
    print(f"The oldest man is {oldest_man_name} at {oldest_man_age} years old")
else:
    print("No men were registered.")

print(f"Number of women under 20: {women_under_20}")
print("=" * 40)
