# First Part: Mathematical Analysis Of The Number

num = int(input("Enter A Number Between 0 And 9999: "))

# Separate The Units, Tens, Hundreds, And Thousands
unit = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

print("=" * 40)
print(f"Analyzing The Number {num}:")
print(f"Unit: {unit}")
print(f"Ten: {ten}")
print(f"Hundred: {hundred}")
print(f"Thousand: {thousand}")
print("=" * 40)

# Second Part: String-Based Digit Position Analysis

num_str = input("Enter A Four-Digit Number: ")

print("=" * 40)
print(f"The Entered Number Was {num_str}")
print(f"Unit: {num_str[3]}")
print(f"Ten: {num_str[2]}")
print(f"Hundred: {num_str[1]}")
print(f"Thousand: {num_str[0]}")
print("=" * 40)
