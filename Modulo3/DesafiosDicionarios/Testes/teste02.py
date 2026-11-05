pessoas = {'nome': 'bruna', 'sexo': 'feminino', 'idade': 20}

# Mostra apenas as chaves
for chave in pessoas.keys():
    print(chave)

print()

# Mostra apenas os valores 
for chave in pessoas.values():
    print(chave)

print()

# Mostra todos os itens
for chave, valor in pessoas.items():
    print(chave, '=', valor)

print()

# Usando delete
del pessoas['sexo']
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

# Pode também trocar de valor
pessoas['idade'] = 21
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

# É possivel adicionar valores
pessoas['peso'] = 76.32
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')
