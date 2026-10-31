# Ler 4 números e colocar dentro de uma tupla, mostrar quantas vezes apareceu o número 9, qual a posição do número 3 e os números pares

valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
valor3 = int(input('Digite mais um número: '))
valor4 = int(input('Digite mais um número: '))

tupla = (valor1, valor2, valor3, valor4)
print(f'O número nove apareceu {tupla.count(9)} vezes')
print(f'O número três apareceu na posição {tupla.index(3)}')
for numero in tupla:
    if numero % 2 == 0:
        print(numero)
print('Fim!')
