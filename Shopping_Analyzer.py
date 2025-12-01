continuar = 'S'
total = 0
contador = 0
menor_preco = 0
menor_nome = ''

while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o valor do produto: '))

    total += preco_produto

    if preco_produto >= 1000:
       contador += 1

    if menor_preco == 0 or preco_produto < menor_preco:
        menor_preco = preco_produto
        menor_nome = nome_produto

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        print('Finalizado')
        break

print(f'O total da compra deu {total:.2f}')
print(f'Existem {contador} itens que custam mais de R$1000')
print(f'O nome do produto mais barato é {menor_nome} custando R${menor_preco:.2f}')
