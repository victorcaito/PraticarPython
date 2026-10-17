# Programa que le o dinheiro atual de uma pessoa em sua carteira e mostra quantos dólares ela pode comprar

nome = str(input('Para começar, insira seu nome: '))
dinheiroAtual = float(input('Insira o dinheiro atual em sua carteira: '))
dolar = 3.27
quantidadeDolarares = dinheiroAtual / dolar
print(f'Olá, {nome}! Você pode comprar {quantidadeDolarares:.2f} dólares com {dinheiroAtual:.2f} reais em sua carteira.')
