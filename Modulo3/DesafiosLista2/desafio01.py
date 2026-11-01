# Ler nome e peso e dizer qual o maior e menor peso e o nome do paciente

dados = []
contagem = 0
while True:
    nome = str(input('Insira o nome do paciente: '))
    peso = float(input('Insira o peso do paciente: '))
    dados.append([nome, peso])
    # adiciona o nome e o peso do paciente na lista dados
    contagem += 1
    resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resposta == 'N':
        break
print(f'Você cadastrou {contagem} pacientes.')
print(f'O maior peso foi de {max(peso for nome, peso in dados)} kg.', end='')
print()
print(f'O menor peso foi de {min(peso for nome, peso in dados)} kg.', end='')

# ou

maior = max(dados, key=lambda paciente: paciente[1])
menor = min(dados, key=lambda paciente: paciente[1])
# lambda é uma função anônima que recebe um paciente e retorna o peso do paciente, que é o segundo elemento da lista paciente
print(f'O paciente mais pesado é {maior[0]} com {maior[1]} kg.')
print(f'O paciente mais leve é {menor[0]} com {menor[1]} kg.')
# mostrando o nome do paciente mais pesado e mais leve, que é o primeiro elemento da lista paciente
print('FIM')