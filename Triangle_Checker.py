print('=-=' * 25)

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

print('=-=' * 25)

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print("Yes, these sides can form a triangle!")
else:
    print("No, these sides cannot form a triangle.")
