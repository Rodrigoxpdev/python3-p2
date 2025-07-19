from random import randint #SORTEA NUMEROS ALEATORIOS
from time import sleep #COLOCA UM TEMPO ANTES DE MOSTRAR A FUNÇAO

#NUMEROS ALEATORIOS
computador = randint(0, 5) #FAZ O COMPUTADOR "PENSAR"
print('---' * 20)#ADICIONANDO TRAÇOS PARA SEPARAR COMO LINHA TOTAL DE 20 
print('Vou pensar em um numero entre 0 e 5 tente advinhar...')
print('---' * 20)#ADICIONANDO TRAÇOS PARA SEPARAR COMO LINHA TOTAL DE 20 

#PERGUNTA AO JOGADOR EM QUE NUMEO O COMPUTADOR PENSOU
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3) #ESPERA 3 SEGUNDOS PARA MOSTRAR O RESULTADO DA CONDIÇÃO

#CONDIÇÂO:
if jogador == computador:
    print('Parabéns você acertou! ')
else:
    print('Sinto muito você errou, eu pensei no numero {} e não no {} !'.format(computador, jogador))





































