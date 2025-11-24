print("====== ARITHMETIC PROGRESSION ======")

first_term = int(input("First term: "))
common_difference = int(input("Common difference: "))

term = first_term
total = 0
more = 10

while more != 0:
    counter = 0
    while counter < more:
        print(f"{term}", end=" → ")
        term += common_difference
        counter += 1
        total += 1
    print("PAUSE")

    more = int(input("How many more terms would you like to show? "))

print(f"Progression finished with {total} terms displayed.")
