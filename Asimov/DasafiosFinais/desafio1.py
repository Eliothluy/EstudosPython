# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.


# letras_minusculas = '''abcdefghijklmnopqrstuvwxyz'''
# letras_maiusculas = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''


# for i in range(3):
#     print(letras_minusculas[i], end='')
# print()  

# chave = 1

# for i in range(3):
#     print(letras_minusculas[i+chave], end='')
# print() 


# for letra in range(5):
#     print(letras_maiusculas[letra], end='')
# print("\n")

# chave = 2

# for letra in range(5):
#     print(letras_maiusculas[letra+ chave], end='')
# print("\n")


# cachorro = 'cachorro'
# chave = -1
# for letra in range(len(cachorro)):
#     print(letras_minusculas[letra+chave], end='')
# print("\n")

def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    # Lidar com situação onde índice está fora dos limites da seq
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

texto = input('Digite o texto: ')
chave = int(input('Digite o texto: '))

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cifra = ''

for caractere in texto:
    if caractere in letras_minusculas:
        caractere_cifra = cifrar_caractere(caractere, letras_minusculas, chave)
        cifra += caractere_cifra
    elif caractere in letras_maiusculas:
        caractere_cifra = cifrar_caractere(caractere, letras_maiusculas, chave)
        cifra += caractere_cifra
    else:
        caractere_cifra = caractere
        cifra += caractere_cifra  

print(cifra)
