#CUSTO DA VIAGEM
distancia = float(input('qual é a distancia da sua viagem? '))
print('você está prestes a começar uma viagem de {}km '.format(distancia))

#FORMA SIMPLIFICADA
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print('e o preço da sua passagem será de R${:.2f}'.format(preço))


#FORMA COMPLEXA
if distancia <= 200:
    preço = distancia * 0.50
    print('e o preço da sua passagem será de R${:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('e o preço da sua passagem será de R${:.2f}'.format(preço))




























