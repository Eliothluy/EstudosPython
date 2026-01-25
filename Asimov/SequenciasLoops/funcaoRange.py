#Função range aceita um valor, e vai gerar uma sequencia cmo esse valor

print(range(10))

print(list(range(10))) # Gera uma sequencia de 10 numeros, em uma lista

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros[1:5]) # vai do indice 1 da lista, até o 5, mas sem imprimir o último indice

print(list(range(1, 5))) #Cria uma lista, de 1 até 4

print(numeros[0:10:2]) # Vai do indice 0 até o 10, mas sem imprimir o ultimo indice, pulando de 2 em 2.

print(list(range(0, 10, 2))) # Cria uma lista do indice 0 até o 10, mas sem imprimir o ultimo indice, pulando de 2 em 2.
