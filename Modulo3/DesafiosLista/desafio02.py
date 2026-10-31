# Adicionar vários valores a uma lista

lista = []
while True:
# enquanto for True ira rodar
    numero = int(input('Insira o número que quer na lista: '))
    resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    # deixa a resposta maiscula e pega apenas o primeiro caracter
    if resposta == 'N' or resposta == 'n':
        break
    # loop será encerrado com break
    # se for S ou s, irá continuar rodando
    else:
        if numero in lista:
        # se o número já está na lista, irá imprimir a mensagem
            print('Esse valor já está na lista.')
        else:
        # caso não possuir, irá adicionar a lista
            lista.append(numero)
            print('Número adicionado com sucesso.')
lista.sort()
print(f'Sua lista é: {lista}')
# imprimi a lista inserida, ordenada em ordem crescente
