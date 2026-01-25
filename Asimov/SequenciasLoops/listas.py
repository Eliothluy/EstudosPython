#Listas são sequencias entre colchetes []
#Listas podem conter outras listas dentro delas.
alunos = ['Ana', 'Bruno', 'Carlos']
print(alunos[0]) #primeiro elemento da lista
print(len(alunos)) # tamanho da lista
print(alunos[-1]) # Último indicie da lista



#Mutabilidade listas

alunos[0] = 'Marcos' # Mudar o primeiro parametro da lista

print(alunos)

#deletar indice na lista
del alunos[0]
print(alunos)
