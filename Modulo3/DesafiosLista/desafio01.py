# Ler 5 valores númericos e guardar na lista, ao final mostrar qual o numero maior e menor e suas posições na lista

valores = []
for contagem in range(1, 6):
    # contagem começa em 1, para não usar a posição 0
    valores.append(int(input('Insira um valor: ')))
    for elemento, v, in enumerate(valores):
        # usando o enumerate para imprimir a posição e o valor
        print(f'Na posição {elemento}, temos o número {v}')
print(f'O maior número é {max(valores)}')
print(f'O menor número é {min(valores)}')

