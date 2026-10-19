# Computador vai pensar em um número entre zero e cinco e pedir pro usuario acertar, mostrar mensagem de acerto ou não

import random
numero = random.randint(0, 5)
# o randint significa que ele vai gerar um número inteiro entre zero e cinco
#  o random é uma biblioteca que tem funções para gerar números ou elementos aleatórios
numeroUsuario = int(input('Insira um número entre zero e cinco: '))
if numeroUsuario == numero:
    print(f'Oba! Você acertou! o número é {numero} e você inseriu {numeroUsuario}')
else:
    print(f'Infelizmente você errou! o número era {numero} e você inseriu {numeroUsuario}')