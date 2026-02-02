#Associar dados 
#Criando o dicionário de capitais 
capitais = {'Brasil':'Brasília', 
            'França':'Paris', 
            'Japão':'Tóquio'}
#imprimindo o dicionário
print(capitais)

#Imprimindo uma capital especifica de uma chave
print(capitais['Brasil'])

#Dicionário são mutaveis, então estamos adicionando mais uma chave e um valor ao dicionário
capitais['Inglaterra'] = 'Londres'

print(capitais)
#Deletendo o valor no dicionário
del capitais['Inglaterra']

print(capitais)
#iterando sobre o dicionário
for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')

print('Brasil' in capitais)