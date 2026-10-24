# Ler número e dizer seu fatorial

from math import factorial

numero = int(input('Insira um número qualquer: '))
fatorial = factorial(numero)
# o factorial é uma função do Python que calcula o fatorial de um número
print(f'O fatorial de {numero} é {fatorial}')

# ou

fatorial = 1
numero2 = int(input('Insira outro número qualquer: '))
contagem = numero2
print(f'Calculando {numero2}! = ', end='')
while contagem > 0:
    print(f'{contagem}', end='')

    print(' x ' if contagem > 1 else '=', end='')
    # irá colocar o x como espaço entre os números e o igual se a contagem for maior que 1
    fatorial *= contagem
    contagem -= 1
    # aqui a contagem vai diminuir
    # e a multiplicação irá continuar
print(f'O fatorial de {numero2} é {fatorial}')
