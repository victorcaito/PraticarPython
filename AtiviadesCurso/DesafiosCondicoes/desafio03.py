# Ler um número e dizer se é par ou impar

numero = int(input('Olá, insira um número para começar: '))
if numero % 2 == 0:
    print(f'Esse número {numero}, é aceito como par')
elif numero == 0:
    print(f'Esse número {numero}, o zero também é aceito como par')
else:
    print(f'Esse número {numero}, é aceito como ímpar')