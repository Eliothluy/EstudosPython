# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: Não vale usar a função sum() !
# numeros = [3.4, 5, 7.5, 7]
# soma = 0
# for n in numeros:
#     print(n)
#     soma = soma+n
# print(f'A média dos números, é: {soma/4}')

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !
# numeros = [3.4, 5, 7.5, 7]
# maior = numeros[0]
# for n in numeros:
#     if n > maior:
#         maior = n

# print(f'O maior número é: {maior}')
# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.
# palavras = ['amigo', 'companheiro', 'Barzinho']
# print(palavras)


#Resolução

#1- valores = [10, 30, -8, 0, -2, 4]
# soma = 0
# for valor in valores:
#     soma += valor
# media = soma / len(valores)
# print(f'A soma dos valores {valores} é: {soma}')
# print(f'A media dos valores é {media}')

# 2- valores = [10, 30, -8, 0, -2, 4]
# maximo= valores[0]

# for valor in valores:
#     if valor > maximo:
#         maximo = valor
# print(f'O valore maiomo dos {valores}, é {maximo}')

palavras = ['oi', 'python', 'Programaçao', 'xxx']

for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Encontrada palavra com 5+ caracteres: {palavra}')



