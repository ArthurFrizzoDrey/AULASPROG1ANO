#criando lista com 5 frutas e imprimindo
lista_frutas= ['maça','banana','uva','maracuja','jabuticaba']
print(lista_frutas)

#criando lista com números de 1 a 10 e imprimindo o primeiro, o terceiro e o ultimo elemento
lista_numeros10= [1,2,3,4,5,6,7,8,9,10]
print(lista_numeros10[0])
print(lista_numeros10[2])
print(lista_numeros10[9])

#crie uma lista vazia, adicione os numeros 5,10 e 15 a lista. remova o numero 10 da lista e imprima a lista
lista_vazia= []
lista_vazia.append(5)
lista_vazia.append(10)
lista_vazia.append(15)
lista_vazia.remove(10)
print(lista_vazia)

#crie uma lsita com os dias da semana. imprima o numero de elementos (dias) na tela.
semana= ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
print(semana.__len__())

#Crie uma lista com os nomes de 5 países. verifique se o brasil esta presente na lista e imprima uma mensagem informando o resultado
lista_5paises= ['russia','eua','brasil','china','alemanha']
if 'brasil' in lista_5paises:
    print('brasil' in lista_5paises)
    #(ambos os jeitos estão certos)
    print('O brasil está na lista')








