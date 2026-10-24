# Tabuada usando o for in range com qualquer número

numero = int(input('Insira um número qualquer: '))
for contagem in range(1, 11):
    # tabuda do 1 até 10
    print(f'{numero} x {contagem} = {numero * contagem}')