# Pedir nome, média do aluno e informar se ele está aprovado ou reprovado

aluno = {}
aluno['nome'] = str(input('Insira o nome do aluno: '))
aluno['media'] = float(input('Insira a média do aluno: '))
print(f'Nome é {aluno["nome"]}')
print(f'Média de {aluno["media"]}')
if aluno['media'] >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')