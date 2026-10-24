# fibonacci

termos = int(input('Quantos termos você quer mostrar? '))
numero1 = 0
numero2 = 1
print(f'{numero1} -> {numero2} -> ', end='')
contagem = 3
while contagem <= termos:
    numero3 = numero1 + numero2
    # o número 3 vai ser igual a soma do número 1 e o número 2
    print(f'{numero3} -> ', end='')
    contagem += 1
    numero1 = numero2
    numero2 = numero3
    # aqui a contagem vai aumentar e somar o termo com o número anterior
print('FIM')
