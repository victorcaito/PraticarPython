# Lista de informações pessoais de uma pessoa

cadastro = {}
pessoas = []
mulheres = []
homens = []
idade_acima = []
idadeteste = ''
# guarda a idade provisória do usuário
media = 0
soma = 0

while True:
# enquanto for verdadeiro
    cadastro['nome'] = input('Insira o nome: ')

    cadastro['sexo'] = input(
        f'Insira o sexo de {cadastro["nome"]}, [M ou F]: ').upper()[0]

    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        # enquanto sexo for diferente de m e f 
        cadastro['sexo'] = input(
            f'Insira o sexo de {cadastro["nome"]}, somente [M ou F]: ').upper()[0]
        # digite novamente o sexo

    idadeteste = input(f'Insira a idade de {cadastro["nome"]}: ')

    while not idadeteste.isnumeric():
        # enquanto a idade não for numérica
        # digite novamente a idade
        idadeteste = input(
            f'Insira a idade [Somente números inteiros] de {cadastro["nome"]}: ')

    cadastro['idade'] = int(idadeteste)

    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro.copy())
        # se for mulher adiciona na lista de mulheres 
    else:
        homens.append(cadastro.copy())
        # se for homem adiciona na lista de homens 

    if cadastro['idade'] > 20:
        idade_acima.append(cadastro.copy())
        # pessoas com idade acima de 20, adiciona na lista maior de idade

    pessoas.append(cadastro.copy())
    # adiciona na lista de pessoas todos os usuários

    soma = soma + cadastro['idade']
    # soma a idade da pessoa ao total

    resposta = input('Deseja continuar? [S ou N]: ').upper()[0]

    while resposta != 'S' and resposta != 'N':
        resposta = input('Insira apenas as letras S ou N: ').upper()[0]
        # confirmação

    if resposta == 'N':
        print('Finalizando... Calculando resultados...')
        break

quantidade = len(pessoas)
# lê a quantidade total de pessoas cadastradas

if quantidade > 0:
    # se houver pessoas cadastradas
    media = soma / quantidade

    print(f'A quantidade de pessoas cadastradas foi de: {quantidade}')
    print(f'A média de idade entre as pessoas cadastradas foi de: {media:.2f}')

    print('-----------------')
    print('Mulheres')
    print('-----------------')
    for posicao, valor in enumerate(mulheres):
        # percorre a lista de mulheres
        # e imprime cada mulher
        # com sua posição na lista
        print(f'    -> {posicao+1}ª mulher: {valor["nome"]}')
        # adiciona mais um para cada posição na lista

    print()
    print('-----------------')
    print('Homens')
    print('-----------------')
    for posicaoM, valorM in enumerate(homens):
        # percorre a lista de homens
        # e imprime cada homem
        # com sua posição na lista
        print(f'    -> {posicaoM+1}º homem: {valorM["nome"]}')

    print()
    print('-----------------')
    print('Pessoas com mais de 20 anos')
    print('-----------------')
    for posicaoI, valorI in enumerate(idade_acima):
        print(f'    -> {posicaoI+1}ª pessoa: {valorI["nome"]}')
else:
    print('Nenhuma pessoa foi cadastrada.')
