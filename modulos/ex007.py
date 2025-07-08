#SEPARANDO DIGITOS DE UM NUMERO
num =  int(input('informe um numero: '))

n = str(num) #CONVERTENDO NUMERO PARA STRING
u = num // 1 % 10  #UNIDADE
d = num // 10 % 10 #DEZENA
c = num // 100 % 10 #CENTENA
m = num // 1000 % 10 #MILHAR

print('ANALISANDO O NUMERO {} '.format(num))
print('UNIDADE: {} '.format(u))
print('DEZENA: {} '.format(d))
print('CENTENA: {} '.format(c))
print('MILHAR: {} '.format(m))


































