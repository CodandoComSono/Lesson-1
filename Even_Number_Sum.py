total = 0

for i in range(1, 7):
    number = int(input(f"Enter the {i}º number: "))
    if number % 2 == 0:
        total += number

print(f"The sum of the even numbers is {total}.")
