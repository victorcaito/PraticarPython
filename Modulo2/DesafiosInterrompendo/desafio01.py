# Programa vai ler números inteiros e só vai parar ao digitar o 999
# No final, ele vai mostrar quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999)

numero = soma = 0
contagem = 0
while True:
    numero = int(input('Insira um número: '))
    contagem += 1
    if numero == 999:
        break
    # vai parar o loop se o usuário digitar 999
    soma += numero
    # vai somar a cada número digitado
print(f'A soma dos números digitados é: {soma} e {contagem} números foram digitados')