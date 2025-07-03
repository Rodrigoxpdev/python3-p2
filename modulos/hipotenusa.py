# CALCULO DA IPOTENUZA PADRAO
# co = float(input('comprimento do cateto oposto: '))
# ca = float(input('comprimento do cateto adiacente: '))
# hi = (co ** 2 + ca**2)** (1/2)
# print('a hipotenusa vai medir {:.2f}'.format(hi))


#UTILIZANDO A IMPORTAÇÃO DA BLIBIOTECA PARA FAZER O CALCULO
#import math #IMPOTANDO BLIBLIOTECA TODA A BLIBLIOTECA

from math import hypot #IMPORTANDO SOMENTE O HYPOT
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adiacente: '))
#CALCULO DA HYPOTENUSA: BLIBLIOTECA MATH: CALCULO (CO, CA)
# hi = math.hypot(co, ca)

#CALCULO IMPORTANDO SOMENTE O HYPOT
hi = hypot(co, ca)

#MOSTRANDO O RESULTADO
print('a hypotenusa vai medir {:.2f}'.format(hi))















 