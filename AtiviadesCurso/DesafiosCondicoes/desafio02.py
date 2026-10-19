# Mostrar se o veiculo foi multado ou não e dizer a quantia de multa a ser paga

velocidade = float(input('Insira a velocidade do veiculo em [KM]: '))
if velocidade >= 80:
    print(f'Você foi multado por ultrapassar os 80KM/h, você percorreu [{velocidade}KM/h]')
    multa = (velocidade - 80)* 7
    print(f'A multa a ser paga é de R${multa:.2f}')
else:
    print(f'Veiculo não recebeu multa, você percorreu [{velocidade}KM/h]')