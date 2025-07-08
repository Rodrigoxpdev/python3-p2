#VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
cidade = str(input('Em que cidade você nasceu? ')).strip()

#.strip() = REMOVE OS ESPAÇOS DO COMEÇO E DO FIM
#upper() = TRANSFORMA TUDO PARA MAIUSCULO
# == 'SANTO' = VERIFICANDO SE TEM A PALAVRA SANTO NO TEXTO DIGITADO
#RESULTADO:
print(cidade[:5].upper() == 'SANTO')




















