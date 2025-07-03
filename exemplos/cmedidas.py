medida = float(input('uma medida em metros '))

# PARA NUMEROS FRACIONADOS NAO UTILIZA-SE O * 
m = medida * 100 # METROS
cm = medida * 100 #CENTIMETROS
mm = medida * 1000#MILIMETROS
km = medida * 1000 #QUILIMETROS
hm = medida * 100 #HEQUITOMETROS
dam = medida * 10 #DECAMETROS
dm = medida * 10 #DECIMETROS

# MEDIDA DE 1 METRO
print(
'A medida de {:.0f}m corresponde a {:.0f}cm CENTIMETROS'  
'\nA medida de {:.0f}m corresponde a {:.0f}mm MILIMETROS' 
'\nA medida de {:.0f}km corresponde a {:.0f}m QUILIMETROS' 
'\nA medida de {:.0f}hm corresponde a {:.0f}m HEQUITOMETROS' 
'\nA medida de {:.0f}dam corresponde a {:.0f}m DECAMETROS' 
'\nA medida de {:.0f}m corresponde a {:.0f}dm DECIMETROS'.format(medida, cm, medida, mm, medida,km ,medida,hm  ,medida,dam ,medida,dm))













