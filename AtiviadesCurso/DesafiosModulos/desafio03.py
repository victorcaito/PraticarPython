# Programa que pede a angulo e mostra na tela o valor do seno, cosseno e tangente do angulo
import math

angulo = float(input("Insira o angulo:"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O seno do angulo {angulo} é {seno:.2f}")
print(f"O cosseno do angulo {angulo} é {cosseno:.2f}")
print(f"A tangente do angulo {angulo} é {tangente:.2f}")
