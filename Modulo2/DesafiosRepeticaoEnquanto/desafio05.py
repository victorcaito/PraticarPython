# Ler o primeiro termo e a razão de uma PA, mostrar os 10 primeiros termos com while

print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contagem = 1
while contagem <= 10:
    print(f'{termo} ->', end='')
    contagem += 1
    termo += razao
    # aqui a contagem vai aumentar e somar o termo com a razao
print('FIM')