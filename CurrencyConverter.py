real = float(input('How many reais do you have in your wallet? R$: '))
usd_rate = 5.38
eur_rate = 6.27
clp_rate = 0.0057

usd = real / usd_rate
eur = real / eur_rate
clp = real / clp_rate

print('=' * 80)
print(f'With R${real:.2f}, you can buy US${usd:.2f} today.')
print(f'With R${real:.2f}, you can buy €{eur:.2f} today.')
print(f'With R${real:.2f}, you can buy CLP${clp:,.0f} today.')
print('=' * 80)
