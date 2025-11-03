viagem = float(input('Qual é a distância da sua viagem: '))

if viagem <= 200:
    calculo = viagem * 0.50
    print(f'O valor que devera ser pago é de R${calculo:.2f}')

else:
    calculo = viagem * 0.45
    print(f'O valor que devera ser pago é de R${calculo:.2f}')
