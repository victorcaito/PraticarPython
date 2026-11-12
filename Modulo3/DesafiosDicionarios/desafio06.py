jogadores = {}
nomes = []
gols = []
total = []

jogadores['nome'] = input('Insira o nome do jogador: ').title()
nomes.append(jogadores['nome'])
jogadores['partidas'] = int(input(f'Quantidade de partidas que {jogadores["nome"]} jogou: '))
for partida in range(jogadores['partidas']):
    gols.append(int(input(f'Quantos gols na partida {partida}? ')))
    
    resposta = str(input('Deseja continuar? [S ou N]: ')).upper()[0]
    total.append(sum(gols))
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Insira apenas as letras S ou N: ')).upper()[0]          
    if resposta == 'N':
        print('Finalizando programa...')
        print('Carregando tabela...')
        break
print('-'*30)
for posicao, jogador in enumerate(nomes):
    print(f'{posicao+1}: {jogador} fez {total[posicao]}')
