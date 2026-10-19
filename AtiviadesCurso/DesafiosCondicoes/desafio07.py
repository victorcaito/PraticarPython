# Ler salario e calcular o valor de aumento de 10% e 15%

salario = float(input("Insira o salario atual: R$"))
if salario >= 1250.00:
    aumento = salario + (salario * 0.10)
    print(f"O aumento será de R${aumento:.2f}")
else:
    aumento = salario + (salario * 0.15)
    print(f"O aumento será de R${aumento:.2f}")
