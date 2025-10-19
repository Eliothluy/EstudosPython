"""
DESAFIO: Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
"""

# Solicita o nome do usuário
nome = input('Digite seu nome: ')

# Solicita o valor do salário mensal
salario = float(input('Digite o valor do seu salário mensal: '))

CONSTANTE_BONUS = 1000.0

# Solicita o valor do bônus recebido
bonus = float(input("Digite o seu bonus:"))

percentagem = salario * bonus/100

kpi  = CONSTANTE_BONUS + percentagem + salario

print(kpi)

print(f'O seu nome é: {nome}, seu salário é: {salario} o bonus é de:{bonus}% e o kpi é: {kpi}')

