# Programa que pede o sexo do usuário e mostra na tela se é masculino ou feminino

sexo = str(input("Digite seu sexo: [M/F] ")).upper()
while sexo != "M" and sexo != "F":
    print("Sexo inválido. Digite novamente.")
    sexo = str(input("Digite seu sexo: [M/F] ")).upper()
    print('FIM')