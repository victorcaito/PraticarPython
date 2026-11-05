
# ! Usando dicionários

# para começar use 
dados = dict()
dados = {'nome': "Leonardo", 'idade': 20}

# ! No dicionário o append não existe

# TODO // Para adicionar um elemento:
dados['sexo'] = 'Masculino'
print(dados)

# TODO // Para deletar um elemento:
del dados['sexo']
print(dados)

# Pode abrir um dicionário desta forma também:
filme = {
    'titulo': 'Avatar',
    'ano': 2009,
    'diretor': 'James Cameron',
}
# O importante é abrir e o fechamento das chaves (keys)

# Keys -> (titulo, ano, diretor)
# Values -> ('Avatar', 2009, 'James Cameron')
# Items -> É todo o conteúdo do dicionário

# TODO // Para retornar os valores de um dicionário: (values())
print(filme.values())

# Pode usar em loops
for keys, values in filme.items():
    # para cada chave e valor dentro de filme imprima:
    print(f'O {keys} é {values}')

# TODO // Posso também criar uma estrutura de lista com dicionarios dentro

# ex: Locadora de filmes
    # Cada filme é um dicionário
    # Cada filme tem um título, um ano e um diretor

locadora = {
    'filme': [
        {
            'titulo': 'Coringa',
            'ano': 2019,
            'diretor': 'Todd Phillips',
        }
    ],
    'filme2': [
        {
            'titulo': 'Avatar',
            'ano': 2009,
            'diretor': 'James Cameron',
        }
    ]
}
print(locadora['filme'][0]['diretor'])
print(locadora['filme2'][1]['ano'])
# Aqui está chamando a lista 2, o ano do filme Avatar, que é 2009
