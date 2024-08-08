#crie uma lista com números aleatorios. Ordene a lista em ordeem crescente e depois em ordem decrescente. imprima as listas ordenadas.
listas_númeroaleat= [12,30,40,32,100,50,80]
listas_númeroaleat.sort()
print(listas_númeroaleat)
listas_númeroaleat.reverse()
print(listas_númeroaleat)

print()
#crie duas listas, uma com nomes de frutas e outra com nomes de cores. Concatene as duas listas em uma lista unica e imprima o resultado
listafruta= ['maça','banana','uva']
listacores= ['vermelho','amarelo','roxo']
print(listafruta + listacores)

print()
#crie uma lista com os números de 1 a 5. repita a lista 3 vezes e imprima o resultado.
lista5= [1,2,3,4,5]
print(lista5)
print(lista5)
print(lista5) #OU print(lista5+lista5+lista5)

print()
# crie uma lista com números aleatórios. Conte quantos números pares e quantos números impares existem na lista. imprima os resultados.
listaimparpar= [12,40,11,1,3,9,20,60]
print(listaimparpar)
print('Nesta lista existem 4 números PARES, e 4 números IMPARES')

# crie uma lista com os números de 1 a 10. Imprima os elementos da lista do indice 2 ao 5 (excluindo o 5), utilizando fatiamento.
listanumerosate10= [1,2,3,4,5,6,7,8,9,10]
print(listanumerosate10)
print(listanumerosate10[2])
print(listanumerosate10[3])
print(listanumerosate10[4])
print(listanumerosate10[5])
listanumerosate10.pop(5)
print(listanumerosate10)