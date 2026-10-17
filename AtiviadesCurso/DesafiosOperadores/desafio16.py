# Calcular o aluguel de um carro

quilometros = float(input('Insira a distancia percorrida em quilometros: '))
dias = int(input('Agora a quantidade de dias usado: '))
precoPagar = quilometros * 0.15 + dias * 60
print(f'O total para se pagar nesse aluguel é: {precoPagar:.2f}')