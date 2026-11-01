# Adicionar vários valores a uma lista em ordem crescente sem uso de sort()

lista = []
for contagem in range(0, 5):
    numeros = (int(input('Insira um número: ')))
    if contagem == 0 or numeros > lista[-1]:
        # se for o primeiro número ou for maior que o último número da lista, insere no final [-1] é a posição do último elemento da lista
        # se não, insere na posição correta
        # se houver mais de um elemento igual, insere no primeiro lugar
        lista.append(numeros)
    else:
        posicao = 0
        # posicao começa com 0, para não usar a posição 0
        while posicao < len(lista):
            # lendo a lista até encontrar a posição correta
            if numeros <= lista[posicao]:
                lista.insert(posicao, numeros)
                # se o número for menor que ou igual ao número na posição atual, insere na posição atual
                break
            posicao += 1
            # posicao aumenta em 1, para não perder a posição atual na próxima iteração
print(f'Os números em ordem crescente são: {lista}')