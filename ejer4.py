#consiga el numero mayor de una lista

lista= [1,3,4,3]

mayor = lista[0]
for i in lista:
    if i> mayor:
        mayor=i
print(mayor)