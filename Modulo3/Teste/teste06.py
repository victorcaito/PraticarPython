
# ! Dicionários dentro de uma lista

brasil = []
estado = {
    'uf': 'São Paulo',
    'sigla': 'SP',
    'populacao': 45000000,
    'capital': 'São Paulo',
    'area': 1531200,
    'regiao': 'Sudeste',
}

estado2 = {
    'uf': 'Minas Gerais',
    'sigla': 'MG',
    'populacao': 21000000,
    'capital': 'Belo Horizonte',
    'area': 351600,
    'regiao': 'Sudeste',
}

brasil.append(estado)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
# Mostra apenas o estado de São Paulo do dicionário 1