#PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING

frase = str(input('digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(frase.find('A')+1))
print('A ultima letra apareceu na poiçao {}'.format(frase.rfind('A')+1))



























