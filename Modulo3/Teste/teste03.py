
# TODO // CÓPIA 
teste = []
teste.append('Victor')
teste.append(20)
outro = []
# outro.append(teste) #ligação
outro.append(teste[:]) #cópia
teste[0] = 'Maria'
teste[1] = 30
outro.append(teste[:]) #cópia
print(outro)
# dessa forma muda o nome e idade de teste, mas não muda o outro, pois foi feita uma cópia da lista teste e não uma ligação

# TODO // Localizar dados dentro de uma lista
pessoas = [['Victor', 20], ['Maria', 30], ['João', 25], ['Ana', 22]]
print(pessoas[2]) # mostra todo o conteúdo do indice 2, que é João 25 
print(pessoas[0]) # mostra o conteúdo do indice 0, que é Victor 20
print(pessoas[2][0]) # mostra somente o nome, que é João, que é João
print(pessoas[3][1]) # mostra somente a idade do indice 3, que é 22

# ou

for cada in pessoas:
    print(cada[0]) # mostra somente os nomes
    print(cada[1]) # mostra somente as idades
    print(f'Nome: {cada[0]} Idade: {cada[1]}') # mostra o nome e idade juntos

# ou também

galera = []
dado = [] #estrutura temporária para armazenar os dados
totalMaior = totalMenor = 0
for cada in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # cópia da lista dado
    dado.clear() # limpa a lista dado para receber novos dados
print(galera)
for cada in galera:
# para cada pessoa na lista galera, verifica se a idade é maior ou menor de idade 
    if cada[1] >= 21:
        print(f'{cada[0]} é maior de idade.')
        # cada[0] é o nome da pessoa, cada[1] é a idade da pessoa
        # mostra o nome de cada pessoa e se ela é maior ou menor de idade
        totalMaior += 1
    else:
        print(f'{cada[0]} é menor de idade.')
        totalMenor += 1
print(f'Total de maiores de idade: {totalMaior}')
print(f'Total de menores de idade: {totalMenor}')