# Programa que pede a angulo e mostra na tela o valor do seno, cosseno e tangente do angulo
import math

angulo = float(input("Insira o angulo:"))
seno = math.sin(math.radians(angulo))
# sin é o seno do angulo
cosseno = math.cos(math.radians(angulo))
# cos é o cosseno do angulo
tangente = math.tan(math.radians(angulo))
# tan é a tangente do angulo
# radians converte o angulo para radianos
print(f"O seno do angulo {angulo} é {seno:.2f}")
print(f"O cosseno do angulo {angulo} é {cosseno:.2f}")
print(f"A tangente do angulo {angulo} é {tangente:.2f}")
