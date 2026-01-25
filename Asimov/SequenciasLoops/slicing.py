#slicing ou fatiamento

pessoas = ['João', 'Paulo', 'Clara', 'Maria']

print(pessoas[1]) #imprimir Paulo, da lista

print(pessoas[1:3]) #Fazer um fatiamento da lista de pessoas vai do indicie 1 e imprime até o 2

print(pessoas[0:len(pessoas)]) # vai do primeiro elemento, até o último da lista.

print(pessoas[1:]) # Vai do segundo elemento até o final da lista

print(pessoas[:3]) # vai do primeiro elemento da lista, excluindo o último.

print(pessoas[:]) #Percorre toda a lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[0:len(numeros):2]) # Pula um elemento da lista
print(numeros[0:len(numeros):3]) # Pula dois elementos da lista
print(numeros[1::2]) # Começa com o segundo indice, e vai pulando 1 lista
print(numeros[::1]) # [início:fim:passo], vai imprimir a lista inteira.
print(numeros[::-1]) #Vai inverter a lista
print(numeros[::-2]) # vai inverter a lista pulando 1 número dela.


#Funciona com qualquer sequencia, inclusive uma string.