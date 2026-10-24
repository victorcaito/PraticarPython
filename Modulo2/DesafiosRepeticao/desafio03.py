# Programa que mostra a soma de todos os números ímpares de 1 a 500

soma = 0
for contagem in range(1, 500):
    if contagem % 2 == 1 and contagem % 3 == 0:
        soma += contagem
        # se o número for ímpar, ele vai imprimir ele mesmo e for divisível por 3, ele vai imprimir ele mesmo
        print(soma)
