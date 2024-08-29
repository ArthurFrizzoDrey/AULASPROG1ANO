#Escreva um loop while que conta de 1 a 10
loop10= 1
while loop10 < 11:
    print(loop10)
    loop10 +=1
else:
    print('O loop acabou!')

# modifique o loop para contar apenas números pares até 20
looppar20= 0
while looppar20 <20:
    looppar20 +=1
    if looppar20 % 2 == 0:
       print(looppar20)

# Solicite uma senha ao usuario e valida ate que ele digita a senha correta.
senha_correta = '123'
tentativa= input('Digite a senha: ')
while tentativa != senha_correta:
    print('Senha incorreta. Tente novamente')
    tentativa= input('Digite a senha:')
    if tentativa != senha_correta:
        print('Senha incorreta, tente novamente')
        tentativa=input('Digite a senha: ')
    if tentativa != senha_correta:
        print('A entrada no sistema foi bloqueado por muitas tentativas')
        break

else:
    print('Senha correta. Acesso concedido')

