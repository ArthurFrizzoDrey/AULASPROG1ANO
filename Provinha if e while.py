#crie um programa que imprime os números de 1 a 20, indicando se cada número é dívisivel por 3.
contador= 0
while contador < 21:
    if contador % 3 ==0:
        print(f'{contador} é divisível por 3')
    else:
        print(f'{contador} não é divisível por 3')
    contador +=1

#Escreva um programa que pede ao usuário um número e diz se ele é primo ou não. O programa deve continuar continuar pedindo
#números até o usuário inserir um número negativo






#implemente um contador que mostra os números de 1 a 50, mas interrompe o laço se o número for divisível por 7
contador2= 1
while contador2 < 51:
    if contador2 % 7 ==0:
        print(f'INTERROMPENDO O LAÇO,  {contador2} ESTE NÚMERO É DIVISÍVEL POR 7!')
        break
    else:
        print(contador2)
        contador2 += 1





