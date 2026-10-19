import colorsys

# a biblioteca colorsys serve para converter cores entre diferentes sistemas de cores
cor = input("Insira uma cor (ex.: #FF0000): ").strip()

# Remove o '#' se houver
if cor.startswith("#"):
    cor = cor[1:]

# o ! serve para verificar se a cor tem 6 caracteres e verificar coisas como se são números ou letras, tipo uma ordem
if len(cor) != 6:
    print("Por favor, insira uma cor Hexadecimal de 6 caracteres (ex: FF0000).")
else:
    r = int(cor[0:2], 16) / 255
    g = int(cor[2:4], 16) / 255
    b = int(cor[4:6], 16) / 255

    h_frac, s_frac, v_frac = colorsys.rgb_to_hsv(r, g, b)

    h = round(h_frac * 360)
    s = round(s_frac * 100)
    v = round(v_frac * 100)

    print(f"Resultado HSV: ({h}°, {s}%, {v}%)")
