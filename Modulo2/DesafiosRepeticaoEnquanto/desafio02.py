# Jogo onde o computado pense em um número de 0 a 10 e o usuário tenta adivinhar qual é o número
import random

cores = {
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "fundovermelho": "\033[0;41m",
    "fundoverde": "\033[0;42m",
    "limpa": "\033[m",
    }

contagem = 0
print("Vamos jogar um jogo de adivinhação. Eu vou pensar em um número de 0 a 10. ")
print("Vamos começar!")

numero = random.randint(0, 10)
# o randint significa que ele vai gerar um número inteiro entre zero e dez

numeroUsuario = int(input("Insira um número entre zero e dez: "))
while numeroUsuario != numero:
    print('Tente novamente: ')
    contagem += 1
    numeroUsuario = int(input("Insira um número entre zero e dez: "))

if numeroUsuario == numero:
    print(f'Oba! Você acertou! o número é {cores["azul"]}{numero}{cores["limpa"]} e você inseriu {cores["amarelo"]}{numeroUsuario}{cores["limpa"]}')

print(f"Você errou {cores["fundovermelho"]}{contagem} {cores["limpa"]} vezes")

print("FIM")
