# Várias palavras e mostrar a vogal (sem assento)

palavras = 'Laranja', 'Brasil', 'Carro', 'Dado', 'Elefante'
print('------------------------------')
for palavra in palavras:
    # Mostrar a palavra e analisar cada elemento da tupla
    print(f'\nNa palavra {palavra} temos ', end='')
    # Mostrar as vogais
    for letra in palavra:
        # separar cada letra da palavra
        if letra.lower() in 'aeiou':
            # mostras vogal sempre em minusculo
            print(letra, end='')
