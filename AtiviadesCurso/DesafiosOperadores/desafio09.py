# Ler um valor qualquer em metros e exibir convertido em centimetros e milimetros

valor = float(input('Insira um valor: '))
centimetro = valor * 100
milimetro = valor * 1000
print(f'O valor {valor} em milimetros é {milimetro:.3f} mm e em centimetros é {centimetro:.3f} cm')
