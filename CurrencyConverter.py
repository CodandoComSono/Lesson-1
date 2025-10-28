real = float(input('Quanto reais você tem na carteira? R$: '))
dolar = 5.38
euro = 6.27
pesochileno = 0.0057

condolar = real / dolar
coneuro = real / euro
conchileno = real / pesochileno

print('=' * 80)
print(f'Com R${real:.2f} você consegue comprar US${condolar:.2f} dólares hoje.')
print(f'Com R${real:.2f} você consegue comprar EUR€{coneuro:.2f} euros hoje.')
print(f'Com R${real:.2f} você consegue comprar CLP${conchileno:,.0f} pesos chilenos hoje.')
print('=' * 80)
