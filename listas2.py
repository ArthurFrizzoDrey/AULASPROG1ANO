#listas #definindo as primeiras listas
alunos = ['José','João','Luiz']
notas= [8.5,9.2,6.7]
print(alunos)
print(notas)
lista_vazia= []
print(lista_vazia)

# lista com  itens de diferentes tipos
lista_misturado= [12,15.56, 'Sorveteria',['Baunilha','Chocolate']]
print(lista_misturado)

# Acessando elementos das listas
print(alunos[0])
print(notas[2])
print(lista_misturado[1],lista_misturado[3])

# Modificando elementos de uma lista
print(notas)
notas[2]=7.7
print(notas)