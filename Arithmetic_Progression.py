print("==== ARITHMETIC PROGRESSION ====")

first_term = int(input("Enter the first term of the AP: "))
common_difference = int(input("Enter the common difference: "))

term = first_term
counter = 1

while counter <= 10:
    print(f"{term}", end=" → ")
    term += common_difference
    counter += 1

print("END")
