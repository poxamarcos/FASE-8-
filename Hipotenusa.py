from math import hypot
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
hipo = hypot(co, ca)

print('O valor da hipotenusa é {:.2f}'.format(hipo))