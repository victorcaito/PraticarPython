# Ler ano de nascimento e dizer quem é maior de idade ou não

maior = 0
menor = 0
for contagem in range(1, 8):
        ano = int(input('Insira o ano de nascimento da próxima pessoa: '))
        idade = 2026 - ano
        if idade >= 18:
            maior += 1
        else: 
            menor += 1
print(f'Existem {menor} menores de idade e {maior} maiores de idade')
