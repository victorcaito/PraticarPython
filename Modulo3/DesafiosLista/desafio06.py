# Ler uma frase e verificar se a quantidade de parênteses abertos é igual à quantidade de parênteses fechados

frase = str(input('Digite uma frase qualquer usando parenteses: exemplo: (frase)')).strip()
# strip() remove espaços em branco no início e no final da frase
if frase.count('(') == frase.count(')'):
    # verifica se a quantidade de parênteses abertos é igual à quantidade de parênteses fechados
    # se for igual, a expressão está correta
    print('A frase está correta.')
else:
    print('A frase está incorreta.')

# ou

expressao = str(input('Digite uma expressão: '))
pilha = []
# aqui está criando uma lista vazia para armazenar os parênteses abertos
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
        # aqui está adicionando um parêntese aberto na lista, caso a expressão tenha um parêntese aberto
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
            # aqui está removendo o último parêntese aberto da lista, caso a expressão tenha um parêntese fechado
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')