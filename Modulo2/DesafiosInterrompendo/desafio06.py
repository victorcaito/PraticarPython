# Simular funcionamento de caixa eletrônico

valorSaque = int(input('Insira o valor do saque: '))
cedula50 = 50
totalCedula = 0

while True:
    if valorSaque >= cedula50:
        # verificar se há cédulas de 50 reais disponíveis
        valorSaque -= cedula50
        # subtrair o valor da cédula do valor do saque
        totalCedula += 1
        # continuar com a mesma cédula se houver suficiente
    else:
        if totalCedula > 0:
            print(f'Foram sacadas {totalCedula} cédulas de {cedula50} reais')
        if cedula50 == 50:
            cedula50 = 20
            # mudar para cédula de 20 reais caso não haja suficiente de 50 reais
        elif cedula50 == 20:
            cedula50 = 10
            # mudar para cédula de 10 reais caso não haja suficiente de 20 reais
        elif cedula50 == 10:
            cedula50 = 1
            # mudar para cédula de 1 reais caso não haja suficiente de 10 reais
        totalCedula = 0
        # reiniciar contador de cédulas
        if valorSaque == 0:
            break
print('Operação concluída!')