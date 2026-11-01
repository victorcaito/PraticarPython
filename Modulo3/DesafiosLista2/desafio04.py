
# indice, nome, média e situação de 4 alunos
informacoes = []
while True:
    nome = str(input("Digite o nome do aluno: ")).title()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    informacoes.append([nome, [nota1, nota2], media])
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# exibe o cabeçalho da tabela com os títulos "No.", "NOME" e "MÉDIA"
for i, aluno in enumerate(informacoes):
    # para cada aluno na lista de informações, exibe o índice, o nome e a média
    # enumerate é usado para obter o índice e o valor ao mesmo tempo
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
    # aqui está sendo exibido o índice, o nome e a média de cada aluno
    # o <4, <10 e >8.1f são formatações para alinhar os dados na saída