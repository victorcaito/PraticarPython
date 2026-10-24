# Programa que mostra a maior idade, a media das idades e quantas mulheres tem menos de 20 anos

somar = 0
nomeMaiorIdade = ''
mulheresMenores = 0
maiorIdade = 0

for pessoa in range(1, 5):
    nome = input(f"Insira o nome da {pessoa}ª pessoa: ")
    idade = int(input(f"Insira a idade da {pessoa}ª pessoa: "))
    sexo = input(f"Insira o sexo da {pessoa}ª pessoa: [M/F] ").upper()
    somar += idade
    # vai somar a idade a cada pessoa digitada
    if sexo == "F" and idade < 20:
        mulheresMenores += 1
        # se for mulher e for menor que 20, ele vai ser contado
    if pessoa == 1 and sexo == "M":
        maiorIdade = idade
        nomeMaiorIdade = nome
        # se for o primeiro homem digitado, ele vai ser o maior
    elif sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaiorIdade = nome
        # se for homem e for maior que a maior idade, ele vai ser o maior

    media = somar / 4
        
print(f"o {nomeMaiorIdade} tem a maior idade com {maiorIdade} anos")
print(f"a media das idades é {media:.2f}")
print(f"tem {mulheresMenores} mulheres com menos de 20 anos")
