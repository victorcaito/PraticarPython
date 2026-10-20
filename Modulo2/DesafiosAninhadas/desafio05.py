# Ler duas notas e calcular média final

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média final do aluno é {media:.2f}')  
if media < 5:
    print('Aluno reprovado')
elif media >= 5 and media < 6.9:
    print('Aluno aprovado')
elif media >= 7:
    print('Aluno aprovado com honra')
else:
    print('Programa encerrado')
