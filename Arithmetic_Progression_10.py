print("=" * 40)
print("  FIRST 10 TERMS OF AN A.P.")
print("=" * 40)

first_term = int(input("Enter the first term: "))
common_difference = int(input("Enter the common difference: "))

tenth_term = first_term + (10 - 1) * common_difference

for term in range(first_term, tenth_term + common_difference, common_difference):
    print(term, end=" → ")
print("END")

