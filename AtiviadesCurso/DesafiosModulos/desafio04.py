#  Sortear um nome
import random
nomeUm = input('Insira o primeiro nome: ')
nomeDois = input('Insira o segundo nome: ')
nomeTres = input('Insira o terceiro nome: ')
print(f'O nome sorteado foi: {random.choice([nomeUm, nomeDois, nomeTres])}')

