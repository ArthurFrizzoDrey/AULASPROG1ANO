#criação e impressão: crie uma tupla com os nomes de 5 frutas. Imprima a tupla na tela
tuplafrutas= ('maça','banana','uva','morango','maracuja')
print(tuplafrutas)

#acesso a elementos: crie uma tupla com os números de 1 a 10. imprima o primeiro, o terceiro e o ultimo número da tupla.
tupla1a10= (1,2,3,4,5,6,7,8,9,10)
print(tupla1a10[0])
print(tupla1a10[2])
print(tupla1a10[9])

#concatenação: crie duas tuplas, uma com nomes de frutas e outra com nomes de cores. Concatene as duas tupals em uma tupla unica e imprima
corestupla= ('amarelo','vermelho','laranja','azul')
print(tuplafrutas+corestupla)


#comprimentoi da tupla: crie uma tupla com os dias da semana, e imprima a quantidade de dias
semanatupla= ('Domingo','Segunda','Quarta','Quinta','Sexta','Sábado')
print(len(semanatupla))

#Verificação de pertencimento: crie uma tupla com os nomes de 5 paises, e verifique se o brasil stá presente e imprima o resutlado
tuplapaises= ('Russia','China','Canada','Brasil')
print(tuplapaises)
if 'Brasil' in tuplapaises:
    print('O Brasil está na tupla') 