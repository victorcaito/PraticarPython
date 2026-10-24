# Programa que le o peso de cinco pessoas, mostrando o maior e o menor peso

maior = 0
menor = 0
for contagemPessoa in range(1, 6):
    peso = float(input(f"Insira o peso da {contagemPessoa}ª pessoa: "))
    if contagemPessoa == 1:
        maior = peso
        menor = peso
        # se for a primeira pessoa, ele vai atribuir o peso a maior e menor
    else:
        if peso > maior:
            maior = peso
            # se o peso for maior que maior, ele vai atribuir o peso a maior
        if peso < menor:
            menor = peso
            # se o peso for menor que menor, ele vai atribuir o peso a menor
print(f"O maior peso lido foi {maior} e o menor foi {menor}")
