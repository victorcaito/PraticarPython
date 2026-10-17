# Programa que le o salário de um colaborador e mostra seu novo salário com desconto

nome = str(input('Olá, digite seu nome: '))
salarioAtual = float(input('Coloque aqui seu salário atual sem aumento: '))
salarioNovo = salarioAtual + (salarioAtual * 12 /100)
print(f'Calculo realizado, {nome}. Seu salário antigo é {salarioAtual:.2f} agora com aumento de 12%, está: {salarioNovo:.2f}')

# o ceil faz arredondamento para cima
# o floor faz arredondamento para baixo
# o trunc tira a parte decimal do número
# o pow eleva um número a uma potência
# sqrt calcular a raiz quadrada de um número
# factorial calcular o fatorial de um número

# import math, chama toda a biblioteca
# from math import ceil, chama apenas um método da biblioteca