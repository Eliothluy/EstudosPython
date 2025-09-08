'''
Desafio - crie um programa que:

-Pede por um nome de usuário e uma senha.
-Se ambos forem corretos, exibe uma mensagem de sucesso.
-Caso contrário, Exibe uma mensagem de erro. A mensagem é diferente
quando o usuário está incorreto e diferente quando a senha está incorreta
-O usuártio/senha corretos podem ser definidos como varáveis dentro do proprio código.
'''

print('-------- Criação de usuário/senha --------')

usuario = input('Crie um usuário: ')
senha = input('Crie uma senhha: ')


print('\n-------- Área de login --------')


usuario_login = input('Digite seu usuário ')
senha_login = input('Digite sua senha: ')

if usuario_login == usuario:
    if senha_login == senha:
        print('Sucesso você conseguiu seu login')
    else:
        print('Falha no login. Senha incorreta.')
else:
    print('Falha no login. Usuário incorreto. ')


