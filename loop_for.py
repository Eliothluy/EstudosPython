'''
Loop for
Loop -> Estrutura de repetição
for -> Uma dessas estruturas


#Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)
print('\n')
#Exemplo de for 2(Iterando sobre uma lista)

for numero in lista:
    print(numero)
print('\n')
#Exemplo de for 2(Iterando sobre um range)
for numero in range(0, 11):
    print(numero)

    for indice, letra in enumerate(nome):
    print(nome[indice])

    for valor in enumerate(nome):
    print(valor, end='')
'''
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]

for letra in nome:
    print(letra, end='')

print('\n')
