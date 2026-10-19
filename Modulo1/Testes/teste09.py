numero1 = float(input("Insira a primeira nota: "))
numero2 = float(input("Insira a segunda nota: "))
media = (numero1 + numero2) / 2
print(f"A média das duas notas é {media:.2f}")
if media >= 7:
    print(f"Aluno aprovado {media:.2f}")
else:
    print(f"Aluno reprovado {media:.2f}")
