senha= str(input('Digite a senha de usuário:'))
if (senha== 'admin'):
    print('Olá, administrador!')
elif senha == 'user':
    print('Olá, usuário!')
else:
    print('Acesso negado, verifique sua senha')
