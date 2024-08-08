#criando uma lista de frutas
frutas= ['Maça','banana','uva']

#append: adicionando um item a lista
frutas.append('Morango')

#Imprimindo a lista atualizada
print(frutas)

#remove: removendo a banana
frutas.remove('banana')

#imprimindo a lista novamente
print(frutas)

#insert: colocando um item no índice desejado
frutas.insert(0,'maracuja')
print(frutas)

#pop: remove e retorna o item do indice especificado.
frutas.pop(0)
print(frutas)

#sort(): Ordena a lista em ordem crescente.
frutas.sort()
print(frutas)

#reverse(): inverte a ordem dos elementos da lista.
frutas.reverse()
print(frutas) 