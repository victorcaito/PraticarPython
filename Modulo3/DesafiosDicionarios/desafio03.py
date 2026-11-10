# Mostrar dados de aposentadoria de um trabalhador

trabalhador = {}
trabalhador['nome'] = str(input('Insira o nome: '))
trabalhador['nascimento'] = int(input('Insira o ano de nascimento: '))
trabalhador['carteira_trabalho'] = int(input('Insira o número da carteira de trabalho: [0] para não tem: '))
idade = 2026 - trabalhador['nascimento']
# descobrir a idade atual
if trabalhador['carteira_trabalho'] != 0:
    trabalhador['ano_contrato'] = int(input('Insira o ano de contratação: '))
    trabalhador['salario'] = float(input('Insira o salário: '))
    trabalhador['aposentadoria'] = idade + ((trabalhador['ano_contrato']) + 35) - 2026
    # para calcular a aposentadoria, some a idade com 35 anos (padrão) de trabalho e subtrair o ano de contratação

for chave, valor in trabalhador.items():
    print(f'{chave} é {valor}')
print(f'A idade é: {idade}')