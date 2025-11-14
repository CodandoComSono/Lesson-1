for i in range(1, 6):
    weight = float(input(f"Enter the weight of person {i}: "))

    if i == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight

print(f"\nThe highest weight was {highest:.1f} Kg")
print(f"The lowest weight was {lowest:.1f} Kg")
