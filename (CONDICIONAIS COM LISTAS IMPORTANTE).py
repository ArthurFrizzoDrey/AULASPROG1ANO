
#exercicios
#1- crie uma lista com os números de 1 a 10. Verifique se o numero 7 esta presente. se estiver remova-o, caso não estiver, adicione-o:
lista10= [1,2,3,4,5,6,8,9,10]
if 7 in lista10:
    print('O número 7 está na lista')
else:
     lista10.insert(6,7)
print(lista10)

#2- Verifique se a lista ["maça",'banana','laranja'] contém a fruta 'uva', se não tiver, adicione-a
listafrutas= ["maça",'banana','laranja']
if 'uva' in listafrutas:
    print('A fruta uva está na lista')
else:
    listafrutas.append('uva')
print(listafrutas)

#3- Crie uma lista de 4 números. Verifique se o primeiro número é par. Se for, substitua-o pelo dobro do valor. caso contrario substitua-o pela metade
lista4= [2,3,4,5]
if lista4[0] % 2 == 0:
    index = lista4.index(lista4[0])
    lista4[index] = lista4[0]*2
else:
    lista4.pop(lista4[0])
    lista4.insert(0, lista4[0]/2)
print(lista4)




