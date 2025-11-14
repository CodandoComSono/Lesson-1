total = 0

for n in range(1, 501, 2):
    print(n)
    if n % 3 == 0:
        total += n

print(f"The sum of all odd numbers that are multiples of 3 between 1 and 500 is {total}.")
