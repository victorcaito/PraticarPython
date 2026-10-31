numero = (1, 2, 3, 4, 5)
# numero[3] = 2
print(numero)
# não vai ser executado pois tuplas são imutáveis

numero2 = [1, 2, 3, 4, 5]
numero2[3] = 2
print(numero2)
# vai ser executado pois list são mutáveis
print('------------------------------')

# TODO // agora, se quiser adicionar valores a lista o ideal é usar o método append()
numero2.append(6)
print(numero2)
print('------------------------------')

# TODO // agora, organizar os números em ordem crescente use o método sort()
numero3 = [4, 3, 2, 1, 5]
numero3.sort()
print(numero3)
print('------------------------------')

# TODO // para inverter a ordem use sort(reverse=True)
numero3.sort(reverse=True)
print(numero3)
print('------------------------------')

# TODO // para ler a quantidade, use len()
print(len(numero3))
print('------------------------------')

# TODO // para inserir um valor em uma posição específica, use insert()
numero4 = [10, 3, 8, 4, 6, 8, 10]
numero4.insert(3, 5)
# na posição 3, insere o número 5
print(numero4)
print('------------------------------')

# TODO // a remoção de um elemento é feita com o método pop()
# sem parametro dentro do pop, ele sempre irá remover o último elemento
print(numero4.pop())
print(numero4)
print('------------------------------')
# com paramentro dentro do pop, ele irá remover o elemento na posição especificada
print(numero4.pop(3))
print(numero4)
print('------------------------------')

# TODO // para remover o primeiro elemento da lista use o remove()
print(numero4.remove(10))
print(numero4)
print()
if 13 in numero4:
    numero4.remove(13)
    print(numero4)
    # remove o primeiro elemento 13
    # se houver mais de um elemento 13, ele irá remover o primeiro
else:
    print('Número não encontrado na lista.')
print('------------------------------')
