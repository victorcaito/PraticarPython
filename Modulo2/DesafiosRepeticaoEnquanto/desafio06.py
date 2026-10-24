# Pergunte pro usúario se quer mostrar mais termos, encerra quando ele disser que quer 0 termos

print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contagem = 1
total = 0
mais = 10
while mais != 0:
    # enquanto o usuário não digitar 0, ele vai continuar a digitar quantos termos ele quer a mais
    total = total + mais
    # o total vai ser igual a contagem + o mais
    while contagem <= total:
        # enquanto a contagem for menor ou igual ao total, ele vai continuar a mostrar os termos
        print(f'{termo} ->', end='')
        contagem += 1
        termo += razao
        # aqui a contagem vai aumentar e somar o termo com a razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))