# Mostrar tabuada de vários números um de cada vez, até que um número negativo for colocado

numero = 0
while numero >= 0:
    numero = int(input('Insira um número: '))
    for numeroAleatorio in range(1, 11):
        print(f'{numero} x {numeroAleatorio} = {numero * numeroAleatorio}')
        if numero < 0:
            break