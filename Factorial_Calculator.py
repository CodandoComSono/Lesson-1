n1 = int(input("Enter a number to calculate the factorial: "))
counter = n1
factorial = 1

print(f"{n1}! = ", end="")

while counter > 0:
    print(f"{counter}", end="")
    print(" x " if counter > 1 else " = ", end="")

    factorial *= counter
    counter -= 1

print(f"{factorial}")
