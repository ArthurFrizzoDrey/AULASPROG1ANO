#Declarando variável
idade= int(input('Digite uma idade:'))
#deixar linha em branco
print()
if idade <12:
    print('Você é criança, sua idade é:',idade ,'anos')
elif idade <18:
    print('Você é Adolescente, sua idade é:',idade, 'anos')
elif idade <60:
    print('Você é Adulto, sua idade é:',idade ,'anos')
else:
    print('Você é Idoso, sua idade é:',idade ,'anos')

#faça um programa que calcule sua aprovação com seguintes configurações:
A1= float(input('Qual foi sua nota na avaliação 1?'))
A2= float(input('Qual foi sua nota na avaliação 2?'))
A3= float(input('Qual foi sua nota na avaliação 3?'))
A4= float(input('Qual foi sua nota na avaliação 4?'))
nota= (A1+A2+A3+A4/4)
if nota >7:
    print('Aprovado')
elif nota >5:
    print('Recuperação')
else:
    print('Reprovado') 