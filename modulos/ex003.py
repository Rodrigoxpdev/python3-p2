#SORTEANDO UMA ORDEM NA LISTA
from random import shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4] #LISTA DE PERGUNTAS:
shuffle(lista) #shuffle = MISTURAR NA LISTA
print('A ordem de apresentação será ')
print(lista)













