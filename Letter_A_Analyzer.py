# Ask The User For A Phrase
phrase = str(input("Enter A Phrase: ")).strip().upper()

# Count The Occurrences And Find The First And Last Positions Of The Letter 'A'
count_a = phrase.count('A')
first_a = phrase.find('A')
last_a = phrase.rfind('A')

# Display The Results
print(f"The Entered Phrase Was: {phrase}")
print(f'The Phrase Contains {count_a} Letter(s) "A"')
print(f'It First Appears At Position {first_a}')
print(f'It Last Appears At Position {last_a}')
