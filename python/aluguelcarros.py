#PERGUNTAS
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

#ALUGADOS EM DIAS    VALOR DO KM
pago = (dias * 60) + (km * 0.15)

#RESULTADO
print('o total a pagar é R${:.2f} '.format(pago))































