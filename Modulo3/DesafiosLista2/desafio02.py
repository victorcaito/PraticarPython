# Mostrar a soma dos valores pares, a soma da terceira coluna e o maior valor da segunda linha de uma matriz 3x3

matriz =  [[0,0,0],[0,0,0],[0,0,0]]
somaPar = 0
for linha in range(3):
    # percorre as linhas da matriz
    for coluna in range(3):
        # percorre as colunas da matriz
        matriz[linha][coluna] = int(input(f'Insira um valor para [{linha}, {coluna}]: '))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
        # mostra a matriz completa e o :^5 é para centralizar o valor dentro de 5 espaços
for linha in range(3):
    # usado para analisar cada número na linha
    for coluna in range(3):
        # usado para analisar cada número na coluna
        if matriz[linha][coluna] % 2 == 0:
            # verifica se o valor é par
            somaPar += matriz[linha][coluna]
            # soma os valores pares da matriz, linha e coluna
print(f'A soma dos valores pares da matriz é: {somaPar}')
print(f'A soma da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
# pegando valores apenas da terceira coluna [2]
print(f'Maior valor da segunda linha é: {max(matriz[1])}')
# pegando valores apenas da segunda linha [1] e usando a função max() para pegar o maior valor