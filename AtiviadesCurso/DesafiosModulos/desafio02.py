# Ler o comprimento do cateto oposto e adjacente de um triangulo retangulo, calcular o comprimento da hipotenusa

from math import sqrt

catetoOposto = float(input("Insira o comprimeto do cateto oposto: "))
catetoAdjacente = float(input("Insira o comprimeto do cateto adjacente: "))
hipotenusa = sqrt(catetoOposto**2 + catetoAdjacente**2)
print(f"O resultado é {hipotenusa:.2f}")
# aqui o sqrt serve para calcular a raiz quadrada de um número e depois os comprimentos são elevados a 2 (potência 2) e somados
# a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos

# -------------------------------------
# import math, chama toda a biblioteca
# from math import ceil, chama apenas um método da biblioteca
