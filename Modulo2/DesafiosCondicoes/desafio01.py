# Computador vai pensar em um número entre zero e cinco e pedir pro usuario acertar, mostrar mensagem de acerto ou não

import random
numero = random.randint(0, 5)
# o randint significa que ele vai gerar um número inteiro entre zero e cinco
#  o random é uma biblioteca que tem funções para gerar números ou elementos aleatórios
cores = {
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'fundovermelho': '\033[0;41m',
    'fundoverde': '\033[0;42m',
    'limpa': '\033[m'
}
numeroUsuario = int(input('Insira um número entre zero e cinco: '))
if numeroUsuario == numero:
    print(f'Oba! Você acertou! o número é {cores['fundovermelho']}{numero} e você inseriu {numeroUsuario}')
else:
    print(f'Infelizmente você errou! o número era {cores['fundoverde']}{numero} e você inseriu {numeroUsuario}')
