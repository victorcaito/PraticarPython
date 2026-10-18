# Programa que le o nome de uma cidade e fala se ela começa com SANTO ou não

cidade = str(input('Digite o nome da sua cidade: '))
print(cidade.find('Santo'))
if cidade.find('Santo') == 0:
    print('Sua cidade está válida!')
else:
    print('Sua cidade não é válida em nosso sistema.')
