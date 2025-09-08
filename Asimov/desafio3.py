'''
Desafio - Crie um programa que:
- Escolhe um número secreto
- Pede por um chute do usário.
- Indica se o usuário acertou ou não.
- Se não acertou, dá uma dizendo se o número é mais alto ou mais baixo.
- Repete até 3 vezes.

'''
numero_secreto = 15
descobriu = False

if not descobriu:
    chute = int(input('Digite um chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True


if not descobriu:
    chute = int(input('Digite um chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Digite um chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if descobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu: O número secreto era {numero_secreto}')

