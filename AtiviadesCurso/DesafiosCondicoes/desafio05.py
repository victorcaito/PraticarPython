# Ler um ano qualquer e dizer se ele é bissexto ou não

ano = int(input('Insira um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # Um ano bissexto é aquele que é divisível por 4, mas não por 100, ou que é divisível por 400
    print(f'Esse ano {ano}, é um ano bissexto')
else:
    print(f'Esse ano {ano}, não é um ano bissexto')