while True:
    n = int(input('Digite um número para ver a tabuada (-1 para parar): '))

    if n == -1:
        print('Programa encerrado!')
        break

    print('=-=' * 5)
    print(f'Tabuada do {n}')
    print('=-=' * 5)

    print('N x Resultado')
    print('=-=' * 5)

    for i in range(1, 11):
        resultado = n * i
        print(f'{i} x {resultado}')

    print('=-=' * 5)
