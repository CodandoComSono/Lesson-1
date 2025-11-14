n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += 1

if total == 2:
    print(f"The number {n} is PRIME!")
else:
    print(f"The number {n} is NOT prime.")
