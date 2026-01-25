# Desafio - Crie um programa que:
# - Escolhe um número secreto
# - Pede por um chute do usuário
# - indica se o usuário acertou ou não
# - Se não acertou, dá uma dica, dizendo
# - Se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes:

NUMERO_SECRETO = 100
descobriu = False
chute = int(input('Chute um número de 0 a 100: '))



if not descobriu:
    chute = int(input('Chute um número de 0 a 100: '))
if chute == NUMERO_SECRETO:
    print('Parabéns, você acertou!')
    descobriu = True
else:
    if chute < NUMERO_SECRETO:
        print('Você chutou um número menor')
    else:
        print('Você chutou um número maior!')


if not descobriu:
    chute = int(input('Chute um número de 0 a 100: '))
if chute == NUMERO_SECRETO:
    print('Parabéns, você acertou!')
    descobriu = True
else:
    if chute < NUMERO_SECRETO:
        print('Você chutou um número menor')
    else:
        print('Você chutou um número maior!')


if not descobriu:
    chute = int(input('Chute um número de 0 a 100: '))
if chute == NUMERO_SECRETO:
    print('Parabéns, você acertou!')
    descobriu = True
else:
    if chute < NUMERO_SECRETO:
        print('Você chutou um número menor')
    else:
        print('Você chutou um número maior!')



if descobriu:
    print('Você ganhou o jogo')
else:
    print(f'Você perdeu, o número secreto era: {NUMERO_SECRETO}')
