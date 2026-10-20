# Ler ano de nascimento e dar informações de alistamento militar

nome = str(input('Insira seu nome para começar: '))
dataNascimento = int(input('Insira seu ano de nascimento: '))
idade = 2026 - dataNascimento
if idade < 18:
    print(f'Nome: {nome}, atualmente você está com {idade} e ainda vai se alistar ao serviço militar.')
    falta = 18 - idade
    print(f'Faltam {falta} anos para você se alistar ao serviço militar.')
elif idade == 18 or idade == 17:
    print(f'Nome: {nome}, atualmente você está com {idade} e deve se alistar ao serviço militar.')
elif idade >= 19: 
    print(f'Nome: {nome}, atualmente você está com {idade} e seu tempo de alistamento passou.')
    passou = idade - 18
    print(f'Você passou {passou} anos do seu alistamento ao serviço militar.')
