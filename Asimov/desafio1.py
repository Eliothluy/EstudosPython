# Desafio - Crie um programa que:
#- Pede pelo nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f'Olá, {nome}!')
print(f'Seu nome possui {len(nome)} letras')
print(f'Você terá {idade + 5}')
 
