n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))


if n1 >= n2:
    maior = n1
else:
    maior = n2

if n3 >= maior:
    maior = n3

if n1 <= n2:
    menor = n1
else:
    menor = n2

if n3 <= menor:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
