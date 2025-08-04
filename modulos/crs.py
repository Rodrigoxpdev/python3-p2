#STYLO  TEXTO  BACKGROUND
#0        30        40     BRANCO     
#1        31        41     VERMELHO   
#4        32        42     VERDE   
#7        33        43     AMARELO  
#         34        44     AZUL       
#         35        45     ROXO
#         36        46     AZUL CLARO
#         37        47     CINZA



#1
# print('\033[1;36;47m TESTANDO CORES NO TERMINAL EM PYTHON \033[m')


#2
# a = 3
# b = 5
# print('Os valores são \033[33m{} \033[m e \033[34m{} \033[m'.format(a, b))



#3
# nome = 'rodrigo'
# print('ola prazer em te conhecer, {}{}{}!!!'.format('\033[33m', nome,'\033[m'))


#4
nome = 'rodrigo'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;40m'
}

print('ola prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

























