#---SENO COSENO E TANGENTE---

#import math
from math import sin, cos, tan, radians

#PERGUNTA:
angulo = float(input('digite o angolo que voce deseja: '))

#CALCULO COM TODA A BLIBLIOTECA
# sen = math.sin(math.radians(angulo))
# cos = math.cos(math.radians(angulo))
# tan = math.tan(math.radians(angulo))

#CALCULO COM FUNÇOES ESPECIFICAS DA BLIBLIOTECA
sen = sin(radians(angulo)) #SENO
cos = cos(radians(angulo)) #COSSENO
tan = tan(radians(angulo)) #TANGENTE

#RESULTADOS:
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('o angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan))





















