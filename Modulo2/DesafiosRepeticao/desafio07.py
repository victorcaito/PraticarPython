#  Ler número inteiro e dizer se é primo

numero = int(input('Insira um número qualquer: '))
if numero > 2 and numero % numero == 0:
    print("O número é primo")
else:
    print("O número não é primo")

# ou

numero2 = int(input('Insira outro número qualquer: '))
total = 0
for contagem in range(1, numero2 + 1):
    # para cada número, ele vai verificar se ele é divisível por ele mesmo
    if numero2 % contagem == 0:
        print('\033[32m', end='' )
        total += 1
        # se o número for divisível, ele vai imprimir em verde
    else:
        print('\033[31m', end='')   
        # se o número não for divisível, ele vai imprimir em vermelho
    print(contagem, end='' )
# o end='' é para que ele não quebra a linha
print(f'- O número foi divido {total} vezes')
