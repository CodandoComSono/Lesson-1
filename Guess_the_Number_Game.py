import random
import time

numero_sorteio = random.randint(0, 5)
print('=-=' * 25)
print('🎲 Vou pensar em um número entre 0 e 5... tente adivinhar!')
print('=-=' * 25)

tente = int(input('👉 Em que número eu pensei? '))
print('\nPROCESSANDO...')
time.sleep(1.5)

if tente == numero_sorteio:
    print('🎉 Parabéns, você acertou!')
else:
    print(f'❌ Que pena! Eu pensei no número {numero_sorteio}.')

print('=-=' * 25)
