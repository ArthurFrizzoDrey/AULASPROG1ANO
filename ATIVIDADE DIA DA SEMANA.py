#faça um programa que leia um número e exiba o dia correspondente da semana.
#(1- domingo, 2- segunda, etc.) se digitar outro valor aparecerá valor inválido
número= int(input('Escreva o número correspondente do dia da semana que deseja:'))
if número== 1:
    print('Você escolheu domingo.')
elif número ==2:
    print('Você escolheu segunda.')
elif número ==3:
    print('Você escolheu terça.')
elif número == 4:
    print('Você escolheu quarta.')
elif número == 5:
    print('Você escolheu quinta.')
elif número == 6:
    print('Você escolheu sexta.')
elif número == 7:
    print('Você escolheu sábado.')
else:
    print('Valor inválido')

