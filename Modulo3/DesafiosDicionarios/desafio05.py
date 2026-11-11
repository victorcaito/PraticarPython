# Lista de informações pessoais de uma pessoa

cadastro = {}
pessoas = []

while True:
    cadastro['nome'] = input('Insira o nome: ')
    cadastro['sexo'] = input(f'Insira o sexo de {cadastro["nome"]}, [M ou F]: ')
    cadastro['idade'] = int(input(f'Insira a idade de {cadastro["nome"]}: '))
    resposta = input('Deseja continuar? [S ou N]: ').upper()
    if resposta == 'S':
        pessoas.append(cadastro.copy())
        for pessoa in pessoas:
            cadastro['total'] += pessoa['idade']
            # para cada pessoa, some a idade na variável total
    else:
        break
print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {cadastro["total"] / len(pessoas):.2f} anos.')
