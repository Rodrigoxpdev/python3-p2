#ANALISANDO TEXTOS
nome = str(input('Qual seu nome completo? ')).strip()


print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) -nome.count(' '))) 
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))








































