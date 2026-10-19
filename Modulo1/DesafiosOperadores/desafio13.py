# Ler o preço de um produto e mostrar seu novo preço com 5% de desconto

precoProduto = float(input('Insira o preço do produto: '))
novoPrecoDesconto = precoProduto * 0.95
print(f'O novo preço com desconto é de {novoPrecoDesconto:.2f}')
