# Ler nome e preço de vários produtos, programa deve perguntar se o usuário quer continuar, mostrar o total gasto, quantos produtos custam mais de mil e qual o nome do produto mais barato

contagem = 0
menorPreco = 0
nomeMenorPreco = ''
# precisa colocar em '' para que o nome do produto seja impresso corretamente
soma = precoGrande = 0
while True:
    nomeProduto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    if preco >= 1000:
        precoGrande += 1

    soma += preco
    contagem += 1

    if contagem == 1:
        menorPreco = preco
        nomeMenorPreco = nomeProduto
        # Primeiro produto digitado será registrado como o mais barato
    else:
        if preco < menorPreco:
            menorPreco = preco
            nomeMenorPreco = nomeProduto
            # Atualizar o menor preço e o nome do menor mais barato

    opcao = input('Deseja continuar? [S/N]').upper()
    if opcao == 'N':
        break
print(f'Foram digitados {precoGrande} produtos com mais de 1000 reais, o total gasto foi de {soma:.2f}')
print(f'Preço do produto {nomeMenorPreco} mais barato: {menorPreco:.2f}')
