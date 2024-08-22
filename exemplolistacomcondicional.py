lista= [1,2,3,4,5]
if 3 in lista:
    index= lista.index(3)
    lista[index] = 33
else:
    lista.append(3)
print(lista) 