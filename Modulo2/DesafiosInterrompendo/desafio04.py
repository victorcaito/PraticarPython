# Ler idade e sexo de muitas pessoas, a cada pessoa insirida deve perguntar se quer continuar. Mostre no final > 18, quantos homens, quantas mulheres e quantas pessoas com mais de 20 anos

homens = mulheres = maiorIdade = 0
while True:
    # o True serve para repetir o laço até que o usuário digite N
    idade = int(input('Insira a idade da pessoa: '))
    sexo = input('Insira o sexo da pessoa: [M/F] ').upper()
    if idade >= 18:
        print('A pessoa é maior de idade')
        maiorIdade += 1
    else:
        print('A pessoa não é menor de idade')
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade > 20:
        mulheres += 1
    opcao = input('Deseja continuar? [S/N]').upper()
    if opcao == 'N':
        break
print(f'Foram digitados {homens} homens, {mulheres} mulheres com mais de 20 anos e {maiorIdade} pessoas com mais de 18 anos')