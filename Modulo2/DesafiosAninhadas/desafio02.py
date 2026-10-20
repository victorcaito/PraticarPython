# Ler um número e perguntar qual será a base de conversão, binário, octal ou hexadecimal

numero = int(input('Insira o número que deseja converter: '))
baseConversao = input('Insira a base de conversão, binário, octal ou hexadecimal: ')
if baseConversao == 'binário':
    print(f'Número em binário: {bin(numero)[2:]}')
# o 2: é para remover o prefixo '0b' e o bin é para converter para binário
elif baseConversao == 'octal':
    print(f'Número em octal: {oct(numero)[2:]}')
# o 2: é para remover o prefixo '0o' e o oct é para converter para octal
elif baseConversao == 'hexadecimal':
    print(f'Número em hexadecimal: {hex(numero)[2:]}')
# o 2: é para remover o prefixo '0x' e o hex é para converter para hexadecimal
else:
    print('Base de conversão inválida')
    print('Insira binário, octal ou hexadecimal')
    print('Programa encerrado')