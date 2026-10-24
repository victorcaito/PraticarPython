# Ler números inteiros mostrar a média entre eles e dizer qual o menor e maior. No final perguntar se quer continuar a digitar números

soma = 0
media = 0
contagem = 0
menor = 0
maior = 0
continuar = 'SIM'

cores = {
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "fundovermelho": "\033[0;41m",
    "fundoverde": "\033[0;42m",
    "limpa": "\033[m",
    }

while continuar in 'SIM':
    numero = int(input('Insira um número: '))
    soma += numero
    contagem += 1
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Seja continuar? SIM/NÃO')).upper().strip()[0]
media = soma / contagem
# só faz a média se o usuário digitar não
print(f'{cores["azul"]}{soma}  e {cores["fundoverde"]}{contagem} {cores["limpa"]} e {cores["azul"]}{media} {cores["limpa"]} | {cores["amarelo"]}{menor} e {maior}{cores["limpa"]}')
