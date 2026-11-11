# Programa que pede o nome do jogador, a quantidade de partidas e a quantidade de gols em cada partida e mostra resultados expecíficos

placar = {}
gols = [] 

placar['nome'] = str(input('Insira o nome do Jogador: '))
placar['partidas'] = int(input(f'Insira quantas partidas {placar["nome"]} jogou: '))

# loop q vai ler os gols de cada partida
for contador in range(placar['partidas']):
    gols.append(int(input(f'Quantos gols na partida {contador}? ')))
    # adiciona o número de gols na lista gols

# guardando a lista de gols e a soma total dentro do dicionário
placar['gols'] = gols
placar['total'] = sum(gols) 
# sum() soma todos os itens da lista

# resultados
print(f'O jogador {placar["nome"]} jogou {placar["partidas"]} partidas.')

# mostrar os gols de cada partida
for posicao, valor in enumerate(placar['gols']):
    print(f'    -> Na partida {posicao+1}, fez {valor} gols.')

print(f'No total, {placar["nome"]} fez {placar["total"]} gols.')