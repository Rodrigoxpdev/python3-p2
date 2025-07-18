#ANALISE DE NOME

n = str(input('qual seu nome completo? ')).strip()
nome = n.split() #VAI PEGAR O NOME INTEIRO E FATIAR EM PEDAÇOS 
#.format(nome[0]) PEGA A POSIÇAO 0 DO NOME
#.format(nome[len(nome)-1]) LER TODAS AS POSIÇOES DO NOME E PEGA O ULTIMO NOME

#RESULTADO:
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))


#COM ESSE PROGRAMA PODEMOS ANALISAR NOMES E PEGAR A POSIÇAO DE CADA PARTE DO NOME!















