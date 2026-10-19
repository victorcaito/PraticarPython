# Ler tres retas e dizer se forma um triangulo ou não

segmentoUm = float(input('Insira o primeiro segmento: '))
segmentoDois = float(input('Insira o segundo segmento: '))
segmentoTres = float(input('Insira o terceiro segmento: '))
if segmentoUm < segmentoDois + segmentoTres and segmentoDois < segmentoUm + segmentoTres and segmentoTres < segmentoUm + segmentoDois:
#  se os segmentos formam um triangulo, ele será maior que a soma dos outros dois
#  se os segmentos não formam um triangulo, ele será menor que a soma dos outros dois
    print('Os segmentos formam um triangulo')
else:
    print('Os segmentos não formam um triangulo')