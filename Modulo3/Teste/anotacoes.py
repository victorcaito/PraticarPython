
# ! REVISÃO
# [1:] pega todas as variaveis compostas ou simples
# [-1] pega a última variável da lista
# len(lanche) retorna o tamanho da lista, no caso é 4

# for c in lanche:
#     print(c)  -> percorre a lista e imprime cada variável e ao término da lista, encerra o loop

# dentro do python posso fazer tuplas com parenteses ()
# [] colchetes são listas
# () parenteses são tuplas
# {} chaves são dicionários

# TODO \\ as tuplas são imutáveis, logo não posso atribuir novos valores a elas, mas posso alterar os valores dentro delas

bebidas = ('agua', 'coffe', 'tequila', 'vinho')
print(bebidas[1]) 
#aqui está imprimindo a segunda variável da tupla

print('------------------------------')

# pode se formar tuplas sem usar parenteses
lanche = 'hambúrguer', 'suco', 'pizza', 'pudim'
print(lanche)

print('------------------------------')

livros = 'python', 'java', 'c++', 'c#'
print(livros[-2]) 
# aqui está imprimindo a segunda última variável da tupla
# os negativos são para contar de trás para frente

print('------------------------------')

carros = 'volkswagen', 'fiat', 'honda', 'mercedes'
print(carros[1:3]) 
# aqui está imprimindo as variáveis de índice 1 a índice 2 (fiat e honda)
# os índices são inclusivos
# se eu quiser imprimir todas as variáveis, posso usar carros[:]

print('------------------------------')

doces = 'chocolate', 'pudim', 'morango', 'banana'
print(doces[:2]) 
# aqui está imprimindo as variáveis de índice 0 a índice 1 (chocolate e pudim)

print('------------------------------')

roupas = 'camisa', 'jeans', 'blusa', 'calça'
print(roupas[-3:]) 
# aqui está imprimindo as variáveis de índice -3 a índice -1 (jeans, blusa e calça)

print('------------------------------')

# TODO \\ dá o mesmo resultado e é diretamente na variavel composta
salgados = 'pão', 'pão de queijo', 'pão de milho'
for comida in salgados:
    print(f'Eu vou comer {comida}')
print('Eu comi tudo!')

print('------------------------------')

# TODO \\ usando o range é variavel composta
papelaria = 'caneta', 'lapiz', 'cartão', 'caderno', 'livro'
for contador in range(0, len(papelaria)): 
    # percorrendo cada índice da tupla (de 0 a 5)
    print(f'Dessa vez vou comprar {papelaria[contador]}') 
    # está imprimindo cada variável da tupla
    # somente o contador iria mostrar os números de 0 a 4
print('Não sobrou nada do que eu comprei!')

print('------------------------------')

bar = 'cerveja', 'vinho', 'tequila', 'agua', 'coffe'
for bebida in range(0, len(bar)):
    print(f'Bebi {bar[bebida]} na posição {bebida}')

print('------------------------------')

# TODO \\ usando o enumerate é variavel composta também, única diferença é a utilização de duas variáveis
perifericos = 'mouse', 'teclado', 'monitor', 'impressora'
for pos, contador in enumerate(perifericos):
    # o pos é a númeração da tupla
    # enumerate() retorna uma tupla com o índice e o valor da variável (enumerado)
    print(f'Eu vou comprar {contador} na posição {pos}')

print('------------------------------')

# TODO \\ usando o sorted organiza a tupla em ordem alfabética
animais = 'cachorro', 'gato', 'elefante', 'panda'
print(sorted(animais))

print('------------------------------')

a = (2, 5, 9)
b = (1, 3, 4, 6)
c = b + a 
# concatenando as duas tuplas (não confudir com a união e soma)
print(c)

print('------------------------------')

x = (2, 3, 4, 5, 9)
z = (8, 3, 6)
y = x + z
print(y.count(3))
# aqui está imprimindo quantas vezes o número 3 aparece na tupla y
print(len(y))
# aqui está imprimindo o tamanho da tupla y
print(y.index(3),'posição do número 3 na tupla y')
# aqui está imprimindo o índice (posição) do número 3 na tupla y
print(y.index(3, 2),'posição do número 3 na tupla y, começando pelo índice 2')
# aqui está imprimindo o índice (posição) do número 3 na tupla y, começando pelo índice 2 (deslocamento)

nome = 'joao', '183 altura', 'homosexual', 'masculino', '32 anos'
# no python não tem problema de juntar 'str' com 'int' ou 'float'
# ->>> del(nome[2]) 
# não funciona deletar uma variável de uma tupla
# mas pode usar o del para deletar uma tupla inteira
del(nome)
# print(nome)