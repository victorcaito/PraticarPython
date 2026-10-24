# Ler dois valores e mostrar um menu de operações númericas

opcao = 0
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
while opcao != 5:
    print('-----------------')
    print('[1] SOMA')
    print('[2] MULTIPLICAR')
    print('[3] VERIFICAR O MAIOR NÚMERO')
    print('[4] TROCAR POR OUTROS VALORES')
    print('[5] SAIR')
    opcao = int(input("Insira a opção que deseja realizar: "))
    if opcao == 1: 
        print(f"O resultado da soma é {valor1 + valor2}")
    elif opcao == 2:
        print(f"O resultado da multiplicação é {valor1 * valor2}")
    elif opcao == 3:
        if valor1 > valor2:
            print(f"O maior número é {valor1}")
        else:
            print(f"O maior número é {valor2}")
    elif opcao == 4:
        valor3 = int(input("Insira o primeiro valor: "))
        valor4 = int(input("Insira o segundo valor: "))
        valor1 = valor3
        valor2 = valor4
        print(f'Os valores foram trocados para {valor1} e {valor2}')
print('FIM DO PROGRAMA')
