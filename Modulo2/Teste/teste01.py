#  Estrutura condicional aninhada

nome = input("Qual seu nome? ")
if nome in ("Victor", "Carlos", "Gabriela"):
    print("Que nome lindo!")
elif nome in ("Ana", "Cláudia", "Bruna", "Silva"):
    print("Que nome diferente!")
elif nome == "Pedro" or nome == "Fabio" or nome == "Henrique":
    print("Que nome lindo, merece um olá!")
else:
    print("Que nome normal!")

print(f"Tenha um bom dia {nome}!")
