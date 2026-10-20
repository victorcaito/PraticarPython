# Dizer qual tipo de triangulo é de acordo com os segmentos

segmentoUm = float(input('Insira o primeiro segmento: '))
segmentoDois = float(input('Insira o segundo segmento: '))
segmentoTres = float(input('Insira o terceiro segmento: '))
if (segmentoUm < segmentoDois + segmentoTres and segmentoDois < segmentoUm + segmentoTres and segmentoTres < segmentoUm + segmentoDois):
    if segmentoUm == segmentoDois == segmentoTres:
        print('Os segmentos formam um triangulo equilátero')
        # todos os lados iguais
    elif segmentoUm == segmentoDois or segmentoUm == segmentoTres or segmentoDois == segmentoTres:
        print('Os segmentos formam um triangulo isóceles')
        # dois lados iguais
    elif segmentoUm != segmentoDois and segmentoUm != segmentoTres and segmentoDois != segmentoTres:
        print('Os segmentos formam um triangulo escaleno')
        # todos os lados diferentes
else:
    print('Os segmentos não formam um triangulo')
