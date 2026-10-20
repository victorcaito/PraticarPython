# Programa que aprova emprestimo bancário, pedir valor da casa, salário do comprador e quantos anos ele vai pagar, prestação mensal sabendo que ela não pode exceder 30% do salário do comprador

valorCasa = float(input('Indira o valor da casa que deseja comprar: '))
salarioComprador = float(input('Insira quanto recebe de salário: '))
anosPagar = float(input('Insira quantos anos pretende pagar a casa: '))

prestacao = valorCasa / (anosPagar * 12)
if prestacao > salarioComprador * 30 / 100:
    print(f'Empréstimo negado, a prestação mensal excedeu 30% do salário do comprador {salarioComprador * 30 / 100} R$')
else:
    print(f'Empréstimo aprovado, a prestação mensal não excedeu 30% do salário do comprador {prestacao:.2f} R$')
