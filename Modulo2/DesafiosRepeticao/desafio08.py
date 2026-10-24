# Identificar se a frase é um palíndromo

frase = str(input("Insira uma frase qualquer: "))
palavras = frase.split()
# para cada palavra, ele vai remover os espaços em branco
junto = "".join(palavras)
# para cada palavra, ele vai remover os espaços em branco
print(f"Você inseriu a frase: {frase}")
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    # vai começar pelo último caractere
    # aqui vai pegar o primeiro caractere
    # passo de -1, vai voltar
    # para cada letra, ele vai inverter a posição
    inverso += junto[letra]
    print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("Não temos palíndromo")
    # o len é para pegar a quantidade de caracteres na string
