# Ler valores e dizer qual é o maior e menor

numeroUm = int(input('Insira o primeiro número: '))
numeroDois = int(input('Insira o segundo número: '))
numeroTres = int(input('Insira o terceiro número: '))
numeroQuatro = int(input('Insira o quarto número: '))
menor = numeroUm
maior = numeroUm
if numeroDois < numeroUm and numeroDois < numeroTres and numeroDois < numeroQuatro:
    # Se o segundo número for menor que todos os outros, ele será o menor
    menor = numeroDois
elif numeroTres < numeroUm and numeroTres < numeroDois and numeroTres < numeroQuatro:
    menor = numeroTres
elif numeroQuatro < numeroUm and numeroQuatro < numeroDois and numeroQuatro < numeroTres:
    menor = numeroQuatro
elif numeroUm > numeroDois and numeroUm > numeroTres and numeroUm > numeroQuatro:
    # Se o primeiro número for maior que todos os outros, ele será o maior
    maior = numeroUm
elif numeroDois > numeroUm and numeroDois > numeroTres and numeroDois > numeroQuatro:
    maior = numeroDois
elif numeroTres > numeroUm and numeroTres > numeroDois and numeroTres > numeroQuatro:
    maior = numeroTres
elif numeroQuatro > numeroUm and numeroQuatro > numeroDois and numeroQuatro > numeroTres:
    maior = numeroQuatro
print(f'Os números digitados foram: {numeroUm}, {numeroDois}, {numeroTres}, {numeroQuatro}')
print(f'O maior número é {maior} e o menor é {menor}')  