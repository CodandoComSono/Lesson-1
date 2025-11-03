velocidade = float(input('Digite o velocidade atual: '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você pagará R${multa:.2f} de multa!')

else:
    print('Você está dentro do limite!')
