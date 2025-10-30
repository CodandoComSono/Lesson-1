import random

apresentacao = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4',]
sorteio = random.sample(apresentacao, 4)

print(f'O primeiro grupo sorteado foi... {sorteio[0]}')
print(f'O segundo grupo sorteado foi... {sorteio[1]}')
print(f'O terceiro grupo sorteado foi... {sorteio[2]}')
print(f'O quarto grupo sorteado foi... {sorteio[3]}')
