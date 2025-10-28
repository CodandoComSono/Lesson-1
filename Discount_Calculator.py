price = float(input('What is the price of the product? R$: '))

discount = price * 0.05
final_price = price - discount

print(f'The product price is R${price:.2f}, but with a 5% discount it costs only R${final_price:.2f}.')
