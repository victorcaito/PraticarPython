# Ler vários números e mostrar a soma deles

numero = 0
contagem = 0
soma = 0

while numero != 999:
    numero = int(input('Insira um número: '))
    contagem += 1
    if numero == 999:
        break
    print(f'Você digitou o número {numero} e a quantidade de números digitados até agora é {contagem}')
    soma += numero
    # mesma coisa que a contagem porém vai somando o números digitados e não a quantidade de números digitados
    print(f' soma dos números digitados até agora é {soma}')
