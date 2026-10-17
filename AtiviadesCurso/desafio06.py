#  Programa para calcular as operações básicas de matemática entre dois números quaisquer


numero1 = int(input('Um valor qualquer: '))
numero2 = int(input('Outro valor qualquer: '))
soma = numero1 + numero2
multiplicacao = numero1 * numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
elevado = numero1 ** numero2
print(f'A soma entre {numero1} e {numero2} é {soma}')
print(f'A multiplicacao entre {numero1} e {numero2} é {multiplicacao}')
print(f'A subtracao entre {numero1} e {numero2} é {subtracao}')
print(f'A divisao entre {numero1} e {numero2} é {divisao:.2f}')
print(f'A elevado entre {numero1} e {numero2} é {elevado:.2f}')

#  o :.2f é para formatar o número com 2 casas decimais (se quiser mais casas, basta alterar o número)
# o /n serve para quebrar linha no código em python
# o end='' serve para não quebrar linha no código em python e as linhas de código ficarem na mesma linha