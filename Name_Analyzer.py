# Ask the user for their full name
name = str(input("Enter your full name: ")).strip()

print("Analyzing your name...")

# Display the name in uppercase and lowercase
print(f"Your name in uppercase: {name.upper()}")
print(f"Your name in lowercase: {name.lower()}")

# Count total letters excluding spaces
total_letters = len(name) - name.count(' ')
print(f"Your name has a total of {total_letters} letters.")

# Extract and analyze the first name
first_name = name.split()[0]
print(f"Your first name is {first_name} and it has {len(first_name)} letters.")
