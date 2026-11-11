print("**Programa registador de itens**")

valorTotalCarrinho = 0

escolha = int(input("Escolha uma opção:\n1 - Selecionar item\n0 - Sair\n"))

match escolha:
    case 0:
        print("Saindo...")
    case 1:
        while True:
            print("Itens disponíveis:")
            print("1 - Mouse gamer\nR$ 150,00")
            print()
            print("2 - Memória RAM\nR$ 13000,00")
            print()
            print("3 - Cadeira\nR$ 200,00")
            print()

            item = int(input("Escolha um item (1, 2 ou 3) ou 0 para sair: "))

            match item:
                case 0:
                    print("Saindo...")
                    break
                case 1:
                    print("Você selecionou o item Mouse gamer")
                    preco = 150.00
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case 2:
                    print("Você selecionou o item Memória RAM")
                    preco = 13000.00
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case 3:
                    print("Você selecionou o item Cadeira")
                    preco = 200.00
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case _:
                    print("Opção inválida")

print(f"Total do carrinho: R$ {valorTotalCarrinho:.2f}")