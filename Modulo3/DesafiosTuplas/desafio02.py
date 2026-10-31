# Mostrar ordem de competição com tupla

colocados = ('Maria', 
'João', 
'Carlos', 
'Ana', 
'Pedro', 
'Felipe', 
'Roberta', 
'Diego', 
'Sebastiam', 
'Victor',
'Bruna', 
'Joaquina',
'Kaique',
'Gustavo',
'Joaquim',
'Daniela',
'Petrique',
'Lohaine',
'Gael',
'Enzo',
)

print('Os primeiros 5 colocados são: ')
print(colocados[:5])
print()
print('Agora os últimos 4 colocados são: ')
print(colocados[-4:])
print()
print('Os colocados em ordem alfabética são: ')
print(sorted(colocados))
# sorted organiza
print()
print('Qual posição na colocação está o time Joaquim? ')
print(colocados.index('Joaquim'))
# index retorna o índice da variável
print()