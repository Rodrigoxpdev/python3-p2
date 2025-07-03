#PROGRAMA PARA SORTEAR UM NOME ALEATORIO
from random import choice

#PERGUNTANDO NOMES DOS ALUNOS: 
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

#LISTA:
lista = [n1,n2,n3,n4]
#BLIBIOTECA DE NUMEROS ALEATORIOS RANDOM:
escolhido = choice(lista)
#MOSTRANDO RESULTADO:
print('O aluno escolhido foi {}'.format(escolhido))

























