total = 0
count = 0

number = int(input("Enter a number (999 to stop): "))

while number != 999:
    total += number
    count += 1
    number = int(input("Enter a number (999 to stop): "))

print(f"You entered {count} numbers and their total sum is {total}.")
