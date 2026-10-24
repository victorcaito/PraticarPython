soma = 0
for contagem in range(0, 5):
    numero = int(input('Insira um número: '))
    soma += numero
    # aqui é a mesma coisa que soma = soma + numero, ou seja, ele vai somando a cada número digitado
print(f'A soma dos números digitados é: {soma}')