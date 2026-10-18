# Ler número e separalo em unidade, dezena, centena, milhar

numero = int(input('Insira um número inteiro de 0 a 9999:'))
print(str(numero)[0], "unidade")
print(str(numero)[1], "dezena")
print(str(numero)[2], "centena")
print(str(numero)[3], "milhar")
#  aqui ele mostra cada dígito do número separado utilizando o [] para armazenar cada dígito em uma variável, junto com a palavra que representa o dígito

