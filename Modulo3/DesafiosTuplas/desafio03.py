# Gerar 5 números aleatórios e colocar dentro da tupla, listar e mostrar o maior e menor valor

import random

numeros = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
# gerar números aleatórios
print(numeros)
# mostra os números escolhidos
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')
# o max e o min são para encontrar o maior e menor número da tupla
print("Fim!")