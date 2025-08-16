'''
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
'''

numero = int(input('Digite um número: '))

if numero <0:
    print("Numero inválido: ")
else:
    print(f'A raíz quadrade de {numero} é: {numero**0.5}')

