valores = []
valores.append(8)
valores.append(4)
valores.append(9)
valores.append(3)
for v in valores:
    print(f' Número: {v}', end=' - ')
    # imprime cada número da lista com os valores adicionados

print('------------------------------')

# TODO // para ler a posição de cada elemento, use enumerate()
for casa, v in enumerate(valores):
    print(f'Na posição {casa}, temos o número {v}')
print('Fim')

#  TODO // ler valores pelo usuario e colocar dentro da lista
valores2 = []
for contagem in range(0, 5):
    valores2.append(int(input('Insira um valor: ')))
for elemento, v, in enumerate(valores2):
    print(f'Na posição {elemento}, temos o número {v}')

# TODO // para criar uma cópia de uma lista, use [:]
listaA = [4, 6, 8, 1]
listaB = listaA
# listaB é uma LIGAÇÂO da listaA (não consegue alterar valores individualmente)
listaB = listaA[:]
# listaB é uma CÒPIA da listaA (consegue alterar valores)
listaB[2] = 5
# a partir do momento em que a listaA foi atribuida a listaB, a listaA também será alterada
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
