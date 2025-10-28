days = int(input('Number of days rented: '))
km_driven = float(input('How many kilometers driven? '))

days_cost = days * 60
km_cost = km_driven * 0.15
total_cost = days_cost + km_cost

print(f'You rented the car for {days} days, totaling R${days_cost:.2f},')
print(f'and drove {km_driven:.2f} km, costing R${km_cost:.2f}.')
print(f'Total cost: R${total_cost:.2f}.')
