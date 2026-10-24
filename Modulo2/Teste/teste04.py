inicio = int(input('Insira um número:'))
fim = int(input('Insira outro número:'))
passo = int(input('Insira um número de passo:'))
for contagem in range(inicio, fim+1, passo):
    # aqui o fim+1 é para que o fim seja incluido no contador (então se colou 12 o sistema vai contar até 12)
    print(contagem)
print('FIM')