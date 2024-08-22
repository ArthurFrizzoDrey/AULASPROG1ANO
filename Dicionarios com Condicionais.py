#exercicios
#1- Crie um dicionario com chaves ''produto'' e 'preço'. verifique se a chave 'desconto' existe. se não existir, adicione desconto com o valor 10.
#se ja existe, dobre o valor do desconto

dicionario= {'produto': 'maça', 'preço': 5,'desconto':5}
if 'desconto' in dicionario:
    dicionario['desconto']= 10
    print(dicionario)
else:
    dicionario['desconto']=+10
    print(dicionario)

#2- crie um dicionario com informações sobre uma pessoa (nome, idade) verifique se a idade é maior que 18.
#se for, adicione a chave 'maioridade' com o valor True, caso contrario, adicione com o valor false

informacao= {'nome':'Arthur','Idade':18}
if informacao["Idade"] ==18:
    informacao['maioridade']= True
else:
    informacao['maioridade']=False
print(informacao)


#3- Verifique se o dicionario ('a': 1, 'b': 2, 'c': 3) contém a chave d, se não contiver, adiocione d com o valor 4

valoresletras= {'a': 1, 'b': 2, 'c': 3}
if 'd' in valoresletras:
    print('A chave d está no dicionario')
else:
    valoresletras['d'] = 4
    print(valoresletras) 

