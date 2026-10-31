# Ler número entre 0 a 20 por número e apresentar por extenso

resposta = int(input("Qual número você quer saber por extenso [DE 0 A 20]? "))
numero = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
print("Você digitou o número: ")
if resposta < 20:
    print(numero[resposta])
    print("Fim!")
else:
    print("Número inválido!")
    print("Fim!")
