# Wall Paint Calculator

# Ask the user for wall dimensions
width = float(input("Enter the wall width (meters): "))
height = float(input("Enter the wall height (meters): "))

# Calculate wall area and paint needed
area = width * height
paint = area / 2  # 1 liter of paint covers 2 m²

# Display results
print(f"The wall area is {area:.2f} m² and you will need {paint:.2f} liters of paint.")
