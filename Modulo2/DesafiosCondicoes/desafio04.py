# Ler distancia de uma viagem em Km e calcular o preço da passagem de 0,50 por Km para viagens de até 200km e 0,45 por Km para viagens acima

distancia = float(input('Insira a distancia percorrida na viagem [Km]: '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço dessa viagem foi de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O preço dessa viagem foi de R${preco:.2f}')
