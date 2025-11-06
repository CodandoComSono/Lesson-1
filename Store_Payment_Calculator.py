colors = {
    "reset": '\033[m',
    "blue": '\033[1;34m',
    "cyan": '\033[1;36m',
    "yellow": '\033[1;33m',
    "red": '\033[1;31m',
    "green": '\033[1;32m',
}

header = f'{colors["green"]}{"=-="*50}\n{"WELCOME TO THE STORE":^100}\n{"=-="*50}{colors["reset"]}'
divider = f'{colors["green"]}{"=-="*50}{colors["reset"]}'
print(header)

customer_name = input('Please enter your name: ').strip().title()
product_price = float(input('Please enter the product price: $'))
print(divider)

print('Select your preferred payment method')

while True:
    print('''Payment Options:
    [ 1 ] - Cash (10% discount)
    [ 2 ] - Card (5% discount)
    [ 3 ] - Up to 2x on card (no discount)
    [ 4 ] - 3x or more on card (20% interest)''')

    payment_option = int(input('Enter your option: '))
    print(divider)

    if payment_option == 1:
        final_price = product_price * 0.90
        print(f'{colors["blue"]}{customer_name}, your total with a 10% discount is: ${final_price:.2f}{colors["reset"]}')
        break

    elif payment_option == 2:
        final_price = product_price * 0.95
        print(f'{colors["blue"]}{customer_name}, your total with a 5% discount is: ${final_price:.2f}{colors["reset"]}')
        break

    elif payment_option == 3:
        final_price = product_price
        print(f'{colors["blue"]}{customer_name}, your total to pay is: ${final_price:.2f}{colors["reset"]}')
        break

    elif payment_option == 4:
        total_installments = int(input(f'{colors["blue"]}Enter number of installments: {colors["reset"]}'))
        final_price = product_price * 1.20
        installment_value = final_price / total_installments
        print(f'{colors["blue"]}Your purchase will be split into {total_installments}x of ${installment_value:.2f}.{colors["reset"]}')
        print(f'{colors["blue"]}{customer_name}, your total with 20% interest is: ${final_price:.2f}{colors["reset"]}')
        break

    else:
        print(f'{colors["yellow"]}Invalid option. Please select a valid payment method.{colors["reset"]}')

print(f'{divider}')
print(f'{colors["green"]}Thank you for your purchase, {customer_name}!{colors["reset"]}')
