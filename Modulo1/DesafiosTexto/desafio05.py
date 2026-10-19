# Ler uma frase e mostrar informações diferentes

frase = str(input('Insira aqui uma frase qualquer: ').upper().strip())
# aqui deixa todas as letras maiúsculas e remove os espaços em branco
print(frase.count('A'))
print(frase.find('A')+1)
# o +1 serve para contar a posição 0 como uma posição, na primeira palavra
print(frase.rfind('A')+1)
# aqui é na ultima palavra