# imprimindo só os números pares da sequencia de numeros até 20
for num in range(21):
    if num %2==0:
        print(num)

#Utilize um while para calcular a soma dos números de 1 a 100
soma= 0
n= 1
while n <101:
    print(n)
    n+=n
#crie uma lista de frutas e use um laço for para imprimir cada fruta da lista.
listafrutas= ['banana','maca','uva','pera']
for frutas in listafrutas:
    print(frutas)

# utilize um laço while para encontrar o menor número positivo que é divisível por 5,6 e 7.
#inicializando o número a ser verificado
numero = 1
#usando o laço while para encontrar o menor numero divisível por 5,6 e 7
while not (numero % 5==0 and numero % 6 ==0 and numero % 7 ==0):
    numero +=1
#Exibindo o resultado
print('O menor número positivo divisível por 5, 6 e 7 é:',numero)



