#RADAR ELETRONICO
from time import sleep
velocidade = float(input('Qual a velocidade atual do carro? '))
print('ANALISANDO...')
sleep(2)

#CONDIÇAO:
if velocidade > 80:
    print('MULTADO! você exedeu o limite permitido que é de 80km/h' )
    multa = (velocidade-80) *7
    print('você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia dirija com segurança!')

































