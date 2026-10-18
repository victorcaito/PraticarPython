# Ler o nome de uma pessoa e falar se ela tem SILVA no nome

nome = str(input('Insira aqui seu nome completo: '))
if 'Silva' or 'SILVA' in nome:
    print('Nome autorizado!')
else:
    print('Não pode entrar, nome sem Silva.')       