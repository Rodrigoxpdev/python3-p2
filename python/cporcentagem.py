#PORCENTAGEM 
p = float(input('Qual é o preço do produto? R$'))

# (PREÇO*5 /100)  PREÇO -5% DE 100% = NOVO PREÇO
np = p - (p*5 /100)
print('O produto que custava R${:.2f}, na promoçao com desconto de 5% vai custar R${:.2f}'.format(p, np))

























