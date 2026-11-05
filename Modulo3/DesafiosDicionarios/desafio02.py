# Mostrar os resultados do jogo e colocação dos jogadores

import random

resultados = {}

for contador in range(4):
    resultados[f'jogador{contador + 1}'] = random.randint(1, 6)
    # adiciona +1 para diferenciar jogadores

for chave, valor in resultados.items():
    print(f'{chave} tirou {valor} no dado.')
    print()
if valor == 10 or valor == 9:
    print(f'{chave} é um jogador vencedor! [1]')
    print()
elif valor == 8 or valor == 7:
    print(f'{chave} Ficou em segundo lugar! [2]')
    print()
elif valor == 6:
    print(f'{chave} Ficou em terceiro lugar! [3]')
    print()
else:
    print(f'{chave} Ficou em quarto lugar! [4]')
    print()