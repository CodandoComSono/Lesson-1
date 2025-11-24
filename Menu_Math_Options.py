n1 = float(input("Enter a value: "))
n2 = float(input("Enter another value: "))

option = 0

while option != 5:
    print("""
[ 1 ] = ADD
[ 2 ] = MULTIPLY
[ 3 ] = GREATER NUMBER
[ 4 ] = NEW NUMBERS
[ 5 ] = EXIT PROGRAM
""")

    option = int(input("Choose an option: "))

    if option == 1:
        total = n1 + n2
        print(f"The sum of {n1} and {n2} is {total}")

    elif option == 2:
        product = n1 * n2
        print(f"The product of {n1} and {n2} is {product}")

    elif option == 3:
        if n1 > n2:
            print(f"{n1} is greater than {n2}")
        elif n1 < n2:
            print(f"{n2} is greater than {n1}")
        else:
            print("Both numbers are equal.")

    elif option == 4:
        print("Enter new numbers:")
        n1 = float(input("Enter a value: "))
        n2 = float(input("Enter another value: "))

    elif option == 5:
        print("Thank you for using the program.")

    else:
        print("Invalid option! Please try again.")
