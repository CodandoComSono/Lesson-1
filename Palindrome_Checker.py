phrase = input("Enter a phrase: ").strip().upper()
phrase_no_space = phrase.replace(" ", "")
reversed_phrase = ""

for i in range(len(phrase_no_space) - 1, -1, -1):
    reversed_phrase += phrase_no_space[i]

print("=" * 40)
print(f"Original phrase: {phrase_no_space}")
print(f"Reversed phrase: {reversed_phrase}")
print("=" * 40)

if phrase_no_space == reversed_phrase:
    print("This phrase IS a PALINDROME!")
else:
    print("This phrase is NOT a palindrome.")
