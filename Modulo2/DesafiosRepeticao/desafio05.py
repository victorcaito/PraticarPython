# Programa que mostra a soma de números pares inseridos pelo usuário

soma = 0
par = 0
numero1 = int(input("Insira um número qualquer: "))
numero2 = int(input("Insira um número qualquer: "))
numero3 = int(input("Insira um número qualquer: "))
numero4 = int(input("Insira um número qualquer: "))
numero5 = int(input("Insira um número qualquer: "))
numero6 = int(input("Insira um número qualquer: "))
if numero1 % 2 == 0:
    soma = numero1
if numero2 % 2 == 0:
    soma += numero2
if numero3 % 2 == 0:
    soma += numero3
if numero4 % 2 == 0:
    soma += numero4
if numero5 % 2 == 0:
    soma += numero5
if numero6 % 2 == 0:
    soma += numero6
if soma == 0:
    print("Nenhum número par foi inserido")
print(f"A soma dos números pares é {soma}")
