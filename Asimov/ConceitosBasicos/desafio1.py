#Desafio - crie um programa que:
#  - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui 
# - Fala quantos anos você terá daqui a 5 anos

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f"Oi, {nome}!")
print(f'Seu nome possui {len(nome.replace(" ",""))} letras')

idadeFuturo = idade + 5

print(f'Daqui a 5 anos você terá: {idadeFuturo} anos')
