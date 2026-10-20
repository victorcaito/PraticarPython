# Calcular imc de uma pessoa e dizer informações nutricionais

nome = str(input('Insira o nome da pessoa: '))
peso = float(input('Insira o peso da pessoa: '))
altura = float(input('Insira a altura da pessoa: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Nome: {nome}, IMC: {imc:.2f}, você está abaixo do peso normal.')
elif imc == 18.5 and imc < 25:
    print(f'Nome: {nome}, IMC: {imc:.2f}, você está no peso normal.')
elif imc >= 25 and imc < 30:
    print(f'Nome: {nome}, IMC: {imc:.2f}, você está acima do peso normal.')
elif imc == 30 and imc < 40:
    print(f'Nome: {nome}, IMC: {imc:.2f}, você está obesidade.')
elif imc > 40:
    print(f'Nome: {nome}, IMC: {imc:.2f}, você está em obesidade mórbida.')