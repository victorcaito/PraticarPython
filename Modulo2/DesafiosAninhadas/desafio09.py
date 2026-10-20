# Calcular desconto de um produto de acordo com a forma de pagamento

precoProduto = float(input('Insira o preço do produto em reais [R$]: '))
formaPagamento = str(input('Insira a forma de pagamento: [Cartão Crédito], [Cartão Débito], [PIX (a vista)]: '))
if formaPagamento == 'Cartão Crédito' or formaPagamento == 'Crédito':
    parcela = int(input('Insira o número de parcelas [3x] ou [2x]: '))
    if parcela >= 3:
        juros = precoProduto + (precoProduto * 20 / 100)
        print(f'O resumo dessa compra foi de: R${juros:.2f}')
    elif parcela == 2:
        juros = precoProduto / 2
        print(f'O resumo dessa compra foi de: R${juros:.2f} 2x')
elif formaPagamento == 'Cartão Débito' or formaPagamento == 'Débito':
    desconto = precoProduto * 5 / 100
    print(f'O resumo dessa compra foi de: R${precoProduto - desconto:.2f} você pagará com desconto de R${desconto:.2f}')
elif formaPagamento == 'PIX (a vista)' or formaPagamento == 'PIX':
    desconto = precoProduto * 10 / 100
    print(f'O resumo dessa compra foi de: R${precoProduto - desconto:.2f} você pagará em vista e recebeu um desconto de R${desconto:.2f}')
else:
    print('Forma de pagamento inválida.')