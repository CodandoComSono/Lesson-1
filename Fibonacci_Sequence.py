print("==== FIBONACCI SEQUENCE ====")

n = int(input("How many terms would you like to display? "))

t1 = 0
t2 = 1
counter = 3

print(f"{t1} → {t2}", end="")

while counter <= n:
    t3 = t1 + t2
    print(f" → {t3}", end="")
    t1 = t2
    t2 = t3
    counter += 1

print(" → END")
