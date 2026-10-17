# Progra que le a largura e a altura de uma parede em metros, mostra sua area e a quantidade de tinta necessaria para pintala

largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))
area = largura * altura
quantidadeTinta = area / 2
print(f'A área da parede é de {area:.2f} m² e voce vai precisar de {quantidadeTinta:.2f} Litros de tinta para pintar esse espaço.')