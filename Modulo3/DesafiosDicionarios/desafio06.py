jogadores = {}
nomes = []
total = []
copia_gol = []

while True:
    gols = []
    jogadores['nome'] = input('Insira o nome do jogador: ').title()
    nomes.append(jogadores['nome'])

    jogadores['partidas'] = int(input(f'Quantidade de partidas que {jogadores["nome"]} jogou: '))
    for partida in range(jogadores['partidas']):
        gols.append(int(input(f'Quantos gols na partida {partida}? ')))
        # vai repetir essa pergunta até completar todas as partidas inseridas
        
    copia_gol.append(gols.copy())
    # cria uma cópia da lista gols para a lista copia_gol
    # a cópia é necessário porque se não fizermos, a lista original gols será alterada em todas as cópias
    print()

    resposta = str(input('Deseja continuar? [S ou N]: ')).upper()[0]
    total.append(sum(gols))
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Insira apenas as letras S ou N: ')).upper()[0]          
    if resposta == 'N':
        print('Finalizando programa...')
        print('Carregando tabela...')
        print()
        break

print(f'{"No.":<4}{"NOME":<10}{"GOLS":>15} {"TOTAL":>10}')
# cabeçalho
for posicao, jogador in enumerate(nomes):
    print(f'{posicao+1:<4}{jogador:<10}{str(copia_gol[posicao]):>15}{total[posicao]:>10}')    
    # mostra a posição em ordem, nome, número de gols e total de gols

print()

print(f'{"No.":<4}{"PARTIDA":<10}{"GOLS":>8}')

for partida, gol in enumerate(copia_gol[posicao]):
    print(f'{partida:<10}{gol:>8}')
    # mostra a posição em ordem, número de gols e cada partida
