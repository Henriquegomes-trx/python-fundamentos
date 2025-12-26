# programa utilizado para calcular lucros ou prejuizo na venda de carro
# autor: Henrique Gomes
valor_pago = float(input('valor pago: '))
valor_investido = float(input('valor investido: '))
valor_venda = float(input('valor da venda: '))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

print('custo total: R$ ', str(custo_total))
print('lucro obtido: R$ ', str(lucro))


if lucro > 0:
    print('resultado: lucro na venda!')
elif lucro < 0:
    print('resultado: prejuizo na venda!')
else:
    print('resultado: sem prejuizo e sem lucro!')
