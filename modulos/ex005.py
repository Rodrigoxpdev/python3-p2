#MANIPULANDO TEXTO
#FATIAMENTO: PEGAR PEDAÇO PEGA SEMPRE UM A MENOS
# FRASE[2:3:2] COM ESSE MODELO ELE PULA DE 2 EM 2 
# FRASE[:5] COMEÇA NO 0 E VAI ATE O 5 POR NAO IDENTIFICAR O COMEÇO
#FRASE[5:] DO 5 ATE O FINAL 
#FRASE[9::3] DO COMEÇO ATE O FINAL PULANDO DE 3 EM 3
# LISTA
# frase[2:4]
# frase(curso em video)


#-------------ANALISE-------------

#len = PEGA O COMPRIMENTO DA FRASE O TAMANHO TOTAL CADA CARACTERES
#len(frase)

#COUNT = MOSTRA QUNTOS O TEM NA FRASE
#frase.count('o')

#DO 0 AO 13 ELE MOSTRA QUANTOS O TEM NA FRASE: O ULTIMO VALOR NAO CONTA
#frase.count('o',0,13)

#FIND = MOSTRA A POSIÇAO QUE COMEÇOU A TEXTO CITADO: DEO
#frase.find('deo')

#SE A FRASE CITADA NAO EXISTIR ELE MOSTRA -1 OU SEJA NÃO EXISTE
#frase.find('android')

# OPERADOR: PERGUNTANDO SE TEM A FRASE CURSO DENTRO DA LISTA = TRUE
#'CURSO' IN FRASE


#-----------TRANSFORMAÇAO-----------

#replace = DESTE MODO SERA SUBSTITUIDO A FRASE CITADA PELA QUAL DESEJA
#frase.relace('python','andoid')

#upper() = VAI FICAR EM MAIUSCULO TODAS AS LETRAS QUE NAO ESTAO EM MAIUSCULO
#frase.upper()

#lower() = LETRAS EM MAIUSCULOS FICA EM MA MINUSCULOS
#frase.lower()

#frase.capitalize() = SÓ O PRIMEIRO FICA EM MAIUSCULO O RESTANTE EM MINUSCULO
#frase.capitalize()

#frase.title() = VAI ANALISAR QUANTAS PALAVRAS TEM ONDE TIVER ESPAÇO E CONSEGUE IDENTIFICAR
#frase.title()


#frase.strip() = REMOVE ESPAÇOS DO COMEÇO E DO FINAL QUE SAO DESNECESSARIO
#frase.strip()

#frase.rstrip() = REMOVE SOMENTE OS ULTIMOS ESPAÇOS
#frase.rstrip()


#frase.lstrip() = REMOVE ESPAÇOS DA ESQUERDA 
#frase.lstrip()



#-----------------DIVISÃO-----------------

#frase.split() = DIVISAO ONDE ESTIVER ESPAÇO COMO FORMA DE LISTA 
#frase.split()


#'-'.join(frase) = VAI FAZER A JUNÇAO DAS FRASES COM O - 
#'-'.join(frase)
#ex:
#frase[curoso-em-video]



# ------------------CODIGO NA PRATICA------------------
# frase = 'Curso em Video Python'
# print('-'.join(frase))
# print(frase[5:])

#IMPRIMIR UM TEXTO INTEIRO USA 3 VEZEA O """
#print(""" SEU TEXTO AQUI """)

# frase = 'Curso em Video Python'
# Contando quantas letras maiúscula o tem na frase o Usando a função upper() para converter para Maiúsculo E utilizando o count() para fazer A contagem
# print(frase.upper().count('O'))




# frase = 'Curso em Video Python'
# Fazendo contagem de quantas caracteres tem na frase
# print(len(frase))


# frase = '   Curso em Video Python   '
# Remove os espaços do comício e do final Utilizando o strip
# print(len(frase.strip()))


# frase = '   Curso em Video Python   '
# Substituindo uma frase ou uma palavra utilizando o replace Visualmente ou seja ela não fica salvo a não ser você armazene como a string
# print(frase.replace('Curso', 'android'))

# Exemplo
# frase = '   Curso em Video Python   '
# frase = frase.replace('curso','Android')
# print(frase.replace('Curso', 'android'))

# frase = 'Curso em Video Python'
# Perguntando se a palavra curso existe dentro da frase
# print('Curso' in frase)


# frase = 'Curso em Video Python'
# # Perguntando se existe curso no final da frase
# print(frase.find('Python'))


# frase = 'Curso em Video Python'
# Transformou palavra vídeo e minúsculo então ele vai ser verdadeiro
# print(frase.lower().find('video'))

# Pegando o primeiro item da lista
# frase = 'Curso em Video Python'
# dividido = frase.split()
# print(dividido[0])

# Pegando a primeira palavra e pegando uma letra específica com a sua posição
# frase = 'Curso em Video Python'
# dividido = frase.split()
# print(dividido[0][4])
























