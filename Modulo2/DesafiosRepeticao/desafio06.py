primeiroTermo = int(input("Insira o primeiro termo da sequência: "))
razao = int(input("Insira a razão da sequência: "))
for contagem in range(1, 11):
    print(primeiroTermo, end='->')
    # para imprimir a sequência, ele vai imprimir o primeiro termo e a razão
    primeiroTermo += razao
print('FIM')
