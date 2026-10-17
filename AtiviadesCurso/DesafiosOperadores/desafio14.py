# Programa que le o salário de um colaborador e mostra seu novo salário com desconto

nome = str(input('Olá, digite seu nome: '))
salarioAtual = float(input('Coloque aqui seu salário atual sem aumento: '))
salarioNovo = salarioAtual + (salarioAtual * 12 /100)
print(f'Calculo realizado, {nome}. Seu salário antigo é {salarioAtual:.2f} agora com aumento de 12%, está: {salarioNovo:.2f}')

