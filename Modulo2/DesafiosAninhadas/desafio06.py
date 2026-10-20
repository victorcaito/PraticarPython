# Ler idade e dizer informações

ano = int(input('Insira seu ano de nascimento: '))
idade = 2026 - ano
if idade <= 9:
    print(f'Você tem {idade} anos e é de nível MIRIM.')
elif idade == 10 or idade <= 14:
    print(f'Você tem {idade} anos e é de nível INFANTIL.')
elif idade == 15 or idade <= 19:
    print(f'Você tem {idade} anos e é de nível JUNIOR.')
elif idade >= 20:
    print(f'Você tem {idade} anos e é de nível SÊNIOR.')
elif idade > 20:
    print(f'Você tem {idade} anos e é de nível MASTER.')
else:
    print('Programa encerrado')
