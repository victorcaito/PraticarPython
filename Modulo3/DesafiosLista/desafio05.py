# Programa que lê vários números e os separa em listas de pares e ímpares, além de mostrar a lista completa

lista = []
listaPares = []
listaImpares = []
while True:
    numero = int(input('Insira um número qualquer: '))
    lista.append(numero)
    print('Número adicionado com sucesso.')
    if numero % 2 == 0:
        listaPares.append(numero)
    elif numero % 2 == 1:
        listaImpares.append(numero)
        # verifica se o número é par ou ímpar e adiciona na lista correspondente
    resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resposta == 'N':
        break
listaPares.sort()
listaImpares.sort()
lista.sort()
print(f'Os números pares estão na lista: {listaPares}')
print(f'Os números ímpares estão na lista: {listaImpares}')
print(f'Os números digitados estão na lista: {lista}')

# ou

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Insira um número qualquer: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
for indice, valor in enumerate(numeros):
    # com o for e o enumerate, é possível ler a posição (indice) e o valor de cada elemento da lista
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
pares.sort()
impares.sort()
numeros.sort()
print(f'Os números pares estão na lista: {pares}')
print(f'Os números ímpares estão na lista: {impares}')
print(f'Lista completa: {numeros}')