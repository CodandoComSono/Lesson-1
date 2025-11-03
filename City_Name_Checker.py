city = str(input("Enter The Name Of The City: ")).strip()

starts_with_santo = city[:5].upper() == "SANTO"

print(f'Does The City Name Start With "Santo"? {starts_with_santo}')
