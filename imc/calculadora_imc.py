# Calculadora imc
# Autor: Henrique Gomes
# Objetivo: praticar lógica de programação em python

peso = float(input('digite seu peso em kg: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura ** 2)
imc = round (imc, 2)

print('seu imc é:  ', str(imc))

if imc < 18:
    print('abaixo do peso')
elif imc < 25:
    print('peso normal')
elif imc < 30:
    print('sobrepeso')
elif imc < 35:
    print('obesidade 1')
elif imc < 40:
    print('obesidade 2')
else:
    print('obesidade mórbida')
