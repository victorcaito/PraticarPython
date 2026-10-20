# Ler dois número e verificar se é menor, maior ou iguais

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
if numero1 < numero2:
    print(f'O número {numero1} é menor que o número {numero2}')
elif numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}')
elif numero2 < numero1:
    print(f'O número {numero2} é menor que o número {numero1}')
elif numero2 > numero1:
    print(f'O número {numero2} é maior que o número {numero1}')
else:
    print('Os números são iguais')
    print('Programa encerrado')