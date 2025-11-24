total_sum = 0
count = 0
continue_flag = "S"

largest = smallest = 0

while continue_flag == "S":
    number = int(input("Enter a number: "))
    total_sum += number
    count += 1

    if count == 1:
        largest = smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    continue_flag = input("Do you want to continue? [S/N]: ").strip().upper()

average = total_sum / count

print(f"\nYou entered {count} numbers.")
print(f"The average value is {average:.2f}.")
print(f"The highest value was {largest}.")
print(f"The lowest value was {smallest}.")
