

import random
indice = 0
quantidade = int(input("Digite a quantidade de jogos que pretende jogar: "))
for indice in range(quantidade):
    print(f'Jogo {indice + 1}: {random.randint(1, 61), random.randint(1, 61), random.randint(1, 61), random.randint(1, 61), random.randint(1, 61), random.randint(1, 61)}')
print(f'Foram gerados {quantidade} jogos de 6 números aleatórios entre 1 e 60.')
print('Boa sorte!')
print('Fim do programa.')