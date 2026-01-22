# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha esta incorreta
# - O usuário/senha "corretos" podem ser definidos como
#variáveis dentro do prório código.

USUARIO_CORRETO = 'Elioth'
SENHA_CORRETA = '1977'

nome = input('Digite o nome de usuário: ')
senha = input('Digite sua senha: ')

if nome != USUARIO_CORRETO:
    print("Usuario incorreto")
else:
    if senha != SENHA_CORRETA:
        print('Senha incorreta!')
    else:
        print('Parabéns, você conseguiu logar!')

