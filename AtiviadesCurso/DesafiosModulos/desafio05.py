# Sortear ordem de apresentação
import random

nomeUm = str(input('Insira o primeiro nome: '))
nomeDois = str(input('Insira o segundo nome: '))
nomeTres = str(input('Insira o terceiro nome: '))
nomeQuatro = str(input('Insira o quarto nome: '))
lista = [nomeUm, nomeDois, nomeTres, nomeQuatro]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
#  o choice serve para sortear um nome aleatório de uma lista
#  o shuffle serve para embaralhar uma lista