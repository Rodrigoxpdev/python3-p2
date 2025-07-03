# ---OPERADORES PY---
# + = ADIÇAO
# - = SUBTRAÇAO
# * = MULTIPLICAÇAO
# / = DIVISAO
# ** = POTENCIA
# // = DIVISAO INTEIRA
# % = RESTO DA DIVISAO

# OPERADOR BINARIO DOIS OPERANDO
# SINAL DE IGUAL E UTILIZADO DOIS SINAIS DE IGUAL ' == ' 
# EX01
# 5+5
# 5-5

# ---ODEM DE PRECEDENCIA---
# 1() PARENTESES 
# 2** POTENCIA
# 3 *, /, //, %  
# 4 +, - 

# ALINHAMENTOS
# EX01
# < CENTRALIZADO A ESQUERDA
# > CENTRALIZADO A DIREITA
# ^ CENTRALIZADO AO CENTRO
# =^ CENTRALIZANDO E COLOCANDO SINAIS DE IGUAIS EM VOLTA ===F===

# nome = input('qual e seu nome? ')
# print('prezer em te conhecer {:=^20}! '.format(nome))

# ---CALCULO DIRETO NO PRINT---
# n1 = int(input('um valor: '))
# n2 = int(input('outro valor: '))
# print('a soma vale {}'.format(n1+n2))


n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
#end=' ' PARA UNIR AS DUAS LINHAS
# \n PARA QUEBRAR LINHAS

print('A soma é {} \no produto é {} \na divisao é {:.3f}'.format(s,m,d), end=' ')
print('divisao inteira é {} e potencia é {}'.format(di,e))
























































