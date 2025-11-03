salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250.00:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)

print(f'O seu salário agora é de R${novo_salario:.2f}')
