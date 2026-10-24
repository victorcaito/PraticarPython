# Jogo de jokenpo com o computador

from random import randint

# o randint() gera um número aleatório entre 1 e 3

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
#  o ''' é usado para imprimir uma string em várias linhas
jogador = int(input('Qual é a sua jogada? '))
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('\033[33mEmpate\033[m')
    elif jogador == 1:
        print('\033[32mJogador vence\033[m')
    elif jogador == 2:
        print('\033[31mComputador vence\033[m')
    else:
        print('\033[31mJogada inválida\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mComputador vence\033[m')
    elif jogador == 1:
            print('\033[33mEmpate\033[m')
    elif jogador == 2:
            print('\033[32mJogador vence\033[m')
    else:
        print('\033[31mJogada inválida\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mJogador vence\033[m')
    elif jogador == 1:
            print('\033[31mComputador vence\033[m')
    elif jogador == 2:
            print('\033[33mEmpate\033[m')
    else:
        print('\033[31mJogada inválida\033[m')


# print(f'O computador jogou {itens[computador]}')
