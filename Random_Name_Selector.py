'''import random

nomes = ['Thiago', 'Matheus', 'José', 'Gabriel']
num = random.choice(nomes)

print(f'O sorteado para apagar o quadro foi..... {num}!!!') '''


import random

primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')

sorteio = random.choice([primeiro, segundo, terceiro, quarto])

print(f'O aluno sorteado para apagar o quadro foi... {sorteio}!!!')
