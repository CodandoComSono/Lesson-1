# Check the characteristics of user input

a = input('Type something: ')

print('The primitive type of this value is', type(a))
print('Only spaces?', a.isspace())
print('Is it a number?', a.isnumeric())
print('Is it alphabetic?', a.isalpha())
print('Is it alphanumeric?', a.isalnum())
print('Is it in uppercase?', a.isupper())
print('Is it in lowercase?', a.islower())
print('Is it capitalized?', a.istitle())
print('Contains only ASCII characters?', a.isascii())

# Método         | O que verifica                                                        | Exemplo                       | Resultado |
#| ------------- | --------------------------------------------------------------------- | ----------------------------- | --------- |
#| `isalnum()`   | Se só tem letras e números (sem espaços ou símbolos)                  | `"Thiago".isalnum()`          | `True`    |
#| `isalpha()`   | Se só tem letras                                                      | `"Python".isalpha()`          | `True`    |
#| `isdigit()`   | Se só tem números decimais (sem sinais ou pontos)                     | `"1980".isdigit()`            | `True`    |
#| `isnumeric()` | Se só tem caracteres numéricos (inclui frações e números romanos)     | `"Ⅻ".isnumeric()`            | `True`    |
#| `isupper()`   | Se todas as letras estão em maiúsculas                                | `"PYTHON".isupper()`          | `True`    |
#| `islower()`   | Se todas as letras estão em minúsculas                                | `"python".islower()`          | `True`    |
#| `istitle()`   | Se está capitalizada (primeira letra maiúscula de cada palavra)       | `"Banco do Brasil".istitle()` | `True`    |
#| `isspace()`   | Se contém apenas espaços, tabulação ou quebras de linha               | `"   ".isspace()`             | `True`    |
#| `isascii()`   | Se contém apenas caracteres ASCII (sem acentos ou símbolos especiais) | `"hello123".isascii()`        | `True`    |

