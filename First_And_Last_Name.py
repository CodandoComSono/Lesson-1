# Ask The User For Their Full Name
full_name = str(input("Enter Your Full Name: ")).strip()

# Split The Name Into Parts
name_parts = full_name.split()

# Display The First And Last Name
print(f"Your First Name Is {name_parts[0]}")
print(f"Your Last Name Is {name_parts[-1]}")
