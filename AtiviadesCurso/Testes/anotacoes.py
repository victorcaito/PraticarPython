# # fatiamento e manipulando texto
# ? Fatiamento
# ! frase[0:21]
# Farba em Gaiol Uitjon
# * pega todas as letras

# ! frase[:5]
# Farba em Gaiol Uitjon
# * aqui ele pega do começo até a posição 5

# ! frase[15:]
# Farba em Gaiol Uitjon
# * aqui ele pega da posição 15 até o fim

# ! frase[9::3]
# Farba em Gaiol Uitjon
# * aqui ele pega a partir da posição 9 e pula de 3 em 3

# ! len[frase]
# Farba em Gaiol Uitjon
# * o len serve para contar quantos caracteres tem na frase, aqui no caso é 21

# ! frase.count('o')
# Farba em Gaiol Uitjon
# * aqui ele conta quantas vezes a letra 'o' aparece na frase, aqui no caso é 2

# ! frase.count('o', 0, 13)
# Farba em Gaiol Uitjon
# * aqui ele conta quantas vezes a letra 'o' aparece na frase entre a posição 0 e a posição 13, aqui no caso é 1

# ! frase.find('iol')
# Farba em Gaiol Uitjon
# * aqui ele encontra a posição da primeira vez que a string 'iol' aparece na frase, aqui no caso é 12

# ! frase.find('android')
# Farba em Gaiol Uitjon
# * vai tentar achar a posição de android, porem não existe, então ele vai retornar -1

# ! 'Farba' in frase
# Farba em Gaiol Uitjon
# * aqui ele verifica se a string 'Farba' está na frase, aqui no caso é True (não é uma funcionalidade e sim um operador)

# ? Transformação
# ! frase.replace('Farba', 'Android')
# Farba em Gaiol Uitjon
# * aqui ele substitui a string 'Farba' por 'Android' na frase, aqui no caso é 'Android em Gaiol Uitjon'

# ! frase.upper()
# Farba em Gaiol Uitjon
# * aqui ele converte todas as letras para maiúsculas, aqui no caso é 'ANDROID EM GAIOL UITJON'

# ! frase.lower()
# Farba em Gaiol Uitjon
# * aqui ele converte todas as letras para minúsculas, aqui no caso é 'android em gaiol uitjon'

# ! frase.capitalize()
# Farba em Gaiol Uitjon
# * aqui ele capitaliza a primeira letra da frase, aqui no caso é 'Android em gaiol uitjon'

# ! frase.title()
# Farba em Gaiol Uitjon
# * aqui ele capitaliza cada palavra da frase, aqui no caso é 'Android Em Gaiol Uitjon'

# ! frase.strip()
# Farba em Gaiol Uitjon
# * aqui ele remove os espaços em branco do COMEÇO e do FIM da frase

# ! frase.rstrip()
# Farba em Gaiol Uitjon
# * aqui ele remove os espaços em branco do FIM da frase

# ! frase.lstrip()
# Farba em Gaiol Uitjon
# * aqui ele remove os espaços em branco do COMEÇO da frase

#  ? Divisão
# ! frase.split()
# Farba em Gaiol Uitjon
# * aqui ele divide a frase em palavras, ficando ['Android', 'em', 'Gaiol', 'Uitjon'], refazendo também a numeração das palavras, começando do zero. 
# * Além de separar em cadeias em lista

# ! '-'.join(frase)
# Farba em Gaiol Uitjon
# * aqui ele une as palavras da frase com um hífen, ficando 'Android-em-Gaiol-Uitjon'

#  ------------------------------
# o ceil faz arredondamento para cima
# o floor faz arredondamento para baixo
# o trunc tira a parte decimal do número
# o pow eleva um número a uma potência
# sqrt calcular a raiz quadrada de um número
# factorial calcular o fatorial de um número