#AUMENTO MÚLTIPLOS 

salario = float(input('qual é o salario do funcionario? '))
if salario <= 1250:   #15% DO SALARIO
    novo = salario + (salario * 15 / 100)
else:                 #10% DO SALARIO
    novo = salario + (salario * 10 /100)


print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))











