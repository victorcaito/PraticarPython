numero = soma = 0

while True:
    numero = int(input('Insira um número: '))
    if numero == 999:
        break
    # vai parar o loop se o usuário digitar 999
    soma += numero
    # vai somar a cada número digitado
print(f'A soma dos números digitados é: {soma}')