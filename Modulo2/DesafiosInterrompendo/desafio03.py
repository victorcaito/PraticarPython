
# Jogo do par ou ímpar

from random import randint

contagem = 0
opcao = 'S'

itens = ('Par', 'Impar')

while opcao == 'S':
    print('[ 0 ] Par')
    print('[ 1 ] Impar')

    jogador = int(input('Insira sua escolha: [0/1] '))
    computador = randint(0, 1)
    # computador vai escolher se é par ou impar
    jogadorNumero = int(input('Insira o número que você quer jogar: '))
    computadorNumero = randint(0, 100)

    print(f'Computador escolheu {itens[computador]}')
    print(f'Computador escolheu o número {computadorNumero}')
    print(f'Jogador escolheu {itens[jogador]}')
    print(f'Jogador escolheu o número {jogadorNumero}')

    soma = jogadorNumero + computadorNumero

    if soma % 2 == 0:
        resultado = 0
        # se a soma for par, o jogador venceu ou perde
    else:
        resultado = 1
        # se a soma for ímpar, o jogador venceu ou perde

    print(f'A soma dos números {computadorNumero} e {jogadorNumero} resulta em {soma}.')

    if jogador == resultado:
        # se o jogador venceu
        contagem += 1
        print(f'Parabéns, você venceu {contagem} vez(es)!')
    else:
        print('Que pena, você perdeu!')
        break

    opcao = input('Quer continuar a jogar? [S/N] ').upper()

print(f'Você venceu {contagem} vezes!') 
print('FIM DO JOGO!')
