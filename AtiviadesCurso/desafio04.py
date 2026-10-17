texto = str(input('Insira algo: '))
print(texto.isnumeric(), 'É um número')# diz se o que foi digitado é um número
print(texto.isalnum(), 'É um alfanumérico')
print(texto.isalpha(), 'É uma letra')
print(texto.isdigit(), 'É um número inteiro')
print(texto.isdecimal(), 'É um número decimal')
print(texto.isspace(), 'É um espaço em branco')
print(texto.islower(), 'É uma letra minúscula')
print(texto.isupper(), 'É uma letra maiúscula')
