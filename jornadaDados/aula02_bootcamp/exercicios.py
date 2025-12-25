import math
# #### Inteiros (`int`)

'''# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"A soma dos números {numero1} mais o número {numero2} é: {soma}")'''

'''# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um número: "))
resto_por_5 = numero % 5
print(f"O resto de {numero} por 5 é: {resto_por_5}")'''


'''# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
multiplicacao = numero1 * numero2
print(f"A multiplicacao dos números {numero1} mais o número {numero2} é: {multiplicacao}")'''
'''# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
divisao_inteira = numero1 // numero2
print(f"A divisao dos números {numero1} mais o número {numero2} é: {divisao_inteira}")'''
'''# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um número: "))
quadrado = numero * numero
print(f"O quadrado de {numero} é: {quadrado}")'''


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"A soma dos números {numero1} mais o número {numero2} é: {soma:.4f}")'''
'''# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
media = (numero1 + numero2)/2
print(f"A média entre {numero1} e {numero2} é {media:.2f}")'''


'''# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = math.pow(base, expoente)
print (resultado)'''

'''# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit = 1.8 * celsius + 32
print(f"O valor de {celsius} celsius, é {fahrenheit} em fahrenheit")'''

'''# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio: "))
area_circulo = math.pi * raio * raio
print(f"A area do cículo é {area_circulo:.2f}")'''

# #### Strings (`str`)

'''# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Digite uma palavra: ")
print(palavra.upper())'''
'''# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
minusculas = nome.lower()
print(minusculas)'''

'''# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espaco = frase.strip()
print(frase_sem_espaco)'''

'''# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data: ")
print(data.split("/"))'''
'''# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
frase1 = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")
print(frase1 + frase2)'''

# #### Booleanos (`bool`)

"""# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite True ou False: ") == "True"
expressao2 = input("Digite True ou False: ") == "True"

logica = expressao1 and expressao2
print(f"O resultado de {expressao1} AND {expressao2} é: {logica}")"""
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''expressao1 = input("Digite True ou False: ") == "True"
expressao2 = input("Digite True ou False: ") == "True"

logica = expressao1 or expressao2
print(f"O resultado de {expressao1} OR {expressao2} é: {logica}")'''
'''# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
entrada = input("Digite um valor booleano (True/False): ").strip()
valor_booleano = entrada.lower() == 'true'
valor_invertido = not valor_booleano
print(valor_invertido)'''
'''# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


sao_iguais = numero1 == numero2


print(f"\nO primeiro número é: {numero1}")
print(f"O segundo número é: {numero2}")
print(f"Os números são iguais? {sao_iguais}")

# Mostrando a expressão booleana completa
print(f"\nExpressão booleana: {numero1} == {numero2} = {sao_iguais}")'''
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

print(math.pi)