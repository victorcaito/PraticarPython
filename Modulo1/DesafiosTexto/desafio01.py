# Ler nome completo da pessoa e mostrar informações diferentes

nome = str(input("Insira seu nome completo a seguir: "))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
# aqui ele conta quantos caracteres tem na frase, mas não conta os espaços em branco
print(len(nome.split()[0]))
# aqui ele conta quantos caracteres tem no primeiro nome
