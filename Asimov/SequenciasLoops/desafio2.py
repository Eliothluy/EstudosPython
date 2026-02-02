# Dado duas listas, printe todos os valores que aparecem
# duplicados nas duas listas
# lista1 = ['cachorro', 'gato', 'periquito', 'leão', 'macaco']
# lista2 = ['macaco', 'gato', 'lobo', 'tubarão', 'orca']

# for animal in lista1:
#     for animal2 in lista2:
#         if animal == animal2:
#             print(f'O {animal} parace nas duas listas')


#     if lista1 == lista2:
#         print(f'os duplicados são: {animal}')
# valores1 = [2, 4, 6]
# valores2 = [1, 2, 6,8]

# for valor1 in valores1:
#     for valor2 in valores2:
#         if valor1 == valor2:
#             print(f'valor {valor1} aparece nas duas listas')



#Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.
lista1 = [10.0, 'xx', True]
lista2 = [0, False, 'xx']

elemento_em_comum = False
for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_em_comum = True

if elemento_em_comum:
    print(f'As listas {lista1} e {lista2} possuem elementos em comum ')
else:
    print(f'As listas {lista1} e {lista2} NÃO possuem elementos em comum ')

