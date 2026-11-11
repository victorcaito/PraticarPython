# Lista de informações pessoais de uma pessoa

cadastro = {}
pessoas = []
mulheres = []
homens = []
idade_acima = []
idadeteste = ''
media = 0
soma = 0

while True:
    cadastro['nome'] = input('Insira o nome: ')
    cadastro['sexo'] = input(f'Insira o sexo de {cadastro["nome"]}, [M ou F]: ').upper()[0]
    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        cadastro['sexo'] = input(f'Insira o sexo de {cadastro["nome"]}, somente [M ou F]: ').upper()[0]

    cadastro['idade'] = int(input(f'Insira a idade de {cadastro["nome"]}: '))
    while not idadeteste.isnumeric():
        idadeteste = input(f'Insira a idade [Somente números inteiros] de {cadastro["nome"]}: ')
    cadastro['idade'] = int(idadeteste)

    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro.copy())
    else:
        homens.append(cadastro.copy())

    if cadastro['idade'] > 20:
        idade_acima.append(cadastro.copy())
    else:
        pessoas.append(cadastro.copy())

    soma = soma + cadastro['idade']
    
    resposta = input('Deseja continuar? [S ou N]: ').upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = input('Insira apenas as letras S ou N: ').upper()[0]
    if resposta == 'N':
        print('Finalizando... Calculando resultados...')
        break

media = soma / len(pessoas)
print(f'A quantidade de pessoas cadastradas foi de: {len(pessoas)}\n')
print(f'A média de idade entre as pessoas cadastradas foi de: {media:.2f}\n')

print('-----------------')
print('Mulheres')
print('-----------------')
for posicao, valor in enumerate(mulheres):
    print(f'    -> {posicao+1}ª mulher: {valor["nome"]}')
print()
print('-----------------')
print('Homens')
print('-----------------')
for posicaoM, valorM in enumerate(homens):
    print(f'    -> {posicaoM+1}ª homem: {valorM["nome"]}')
print()
print('-----------------')
print('Pessoas com mais de 20 anos')
print('-----------------')
for posicaoI, valorI in enumerate(idade_acima):
    print(f'    -> {posicaoI+1}ª pessoa: {valorI["nome"]}')