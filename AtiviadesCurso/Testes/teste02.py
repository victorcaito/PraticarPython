
# para escrever textos grandes, pode utilizar de """ para criar uma string multi linha

print("""lorem ipsum dolor sit amet, consectetur adipiscing elit.
Aliquam erat volutpat. Integer ac nunc a nunc elementum, a auctor nunc.
""")

# ------------------------------------------------------

frase = 'Abobrinha com feijão'
print(frase[::2])

print(frase.count('o'))
print(frase.upper())
print(len(frase))
print(len(frase.strip()))
print(frase.replace('feijão', 'arroz'))

# ------------------------------------------------------

frase2 = 'Goiaba com gergilim'
frase2.replace('Goiaba', 'Melancia')
# para isso funcionar primeiro, é preciso chamar a variavel e dar o método replace
frase2 = frase.replace('Goiaba', 'Melancia')
print(frase2)

# ------------------------------------------------------

frase3 = 'Concha do mar'
print('Concha' in frase3)

# ------------------------------------------------------

frase4 = 'Libras de 430 para Lá'
print(frase4.find('430'))
print(frase4.lower().find('lá'))