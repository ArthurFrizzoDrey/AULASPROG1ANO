#Definindo nossa primeira tupla
tupla1= ('Gato','Cachorro','Papagaio','Tartaruga')
print(tupla1)

#Acessando um elemento da tupla: mesmo formato das listas, com colchetes
print(tupla1[2])

#Pegando um intervalo de uma tupla
print(tupla1[1:3])

#criando uma tupla vazia
tupla_vazia= ()
print(tupla_vazia)

#se tentar adicionar um item a tupla, dará um erro:
#tupla1[1] = 'Elefante'

#para apagar uma tupla, usa-se del()
#del(tupla1)
#print(tupla1)

#Alguma funções para se trabalhar com Tuplas
tupla2= (8.3,9.4,3.3,7.5,7.6)
print(max(tupla2))
print(min(tupla2))
print(len(tupla2))

#Transformando uma tupla em lista ou vice versa
lista1= list(tupla1)
print(lista1)
lista2= ['José','Afonso','Carlos','Luiz']
tupla3= tuple(lista2)
print(tupla3) 