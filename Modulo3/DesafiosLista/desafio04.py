# Ler números e colocar na lista e verificar se o número 5 está na lista, caso esteja, imprimir uma mensagem de sorte

lista = []
contagem = 0
while True:
    numero = int(input('Insira um número qualquer: '))
    if numero in lista:
        print('Esse valor já está na lista.')
        # se o número já está na lista, irá imprimir a mensagem
    else:
        lista.append(numero)
        contagem += 1
        # contagem aumenta em 1, para contar quantos números foram adicionados
        print('Número adicionado com sucesso.')
    resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resposta == 'N':
        break
lista.sort(reverse=True)
# ordena a lista em ordem decrescente
print(f'Os números digitados em ordem decrescente são: {lista}')
print(f'Você adicionou {contagem} números.')
if 5 in lista:
    # verifica se o número 5 está na lista
    print('O número 5 está na lista! É o número da sorte!')
else:
    print('O número 5 não está na lista.')