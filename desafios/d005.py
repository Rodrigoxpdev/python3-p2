#ANO BISSEXTO 
from datetime import date
ano = int(input('QUE ANO QUER ANALISAR? COLOQUE 0 PARA ANALISAR O ANO ATUAL: '))

#PEGANDO ANO ATUAL
if ano == 0:
    ano = date.today().year


if ano % 4 == 0 and ano  % 100 != 0 or ano % 400 == 0: 
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

















