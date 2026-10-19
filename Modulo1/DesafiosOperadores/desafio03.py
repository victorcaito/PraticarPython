#  Programa para calcular a soma de dois números quaisquer

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número "))
soma = numero1 + numero2
# print('A soma dos números', numero1, 'e', numero2, 'números é igual a: ', soma) esse é o antigo
print(f"A soma entre {numero1} e {numero2} vale {soma}")
# a mascara {} serve para substituir os valores dentro do texto, simplificando a leitura e digitação
# int é todos os números inteiros sendo eles negativos ou não, sem virgulas
# float é todos os números com virgula sendo eles negativos ou não
# str é todos os caracteres com aspas simples ou duplas, sendo eles letras, números ou símbolos
# bool é todos os valores booleanos, sendo eles True ou False (verdadeiro ou falso)
