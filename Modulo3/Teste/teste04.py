
# ! Para copiar um dicionário é necessário usar o método copy()

brasil = []
estado = {}
for contador in range(3):
    estado['uf'] = str(input('Insira a [UF]: '))
    estado['sigla'] = str(input('Agora a sigla: '))

    brasil.append(estado.copy())
    # brasil é uma lista, por isso que append funcionou
print(brasil)

# ou

for cada_estado in brasil:
    print(cada_estado)
    # organiza em linha

# para mostrar as chaves com os valores 
for cada_estado in brasil:
    for chave, valor in cada_estado.items():
        print(f'{chave} é {valor}')
    print()
    # para cada posicao e valor dentro de cada_estado imprima

# ou

for cada_estado in brasil:
    for valor in cada_estado.values():
        print(valor, end='') 
        # diz o valor e não quebra linha
        print()
        # organiza em linha para cada valor