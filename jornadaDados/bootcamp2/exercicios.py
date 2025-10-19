'''
Exercícios
Inteiros (int)
1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.
    
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    soma = numero1 + numero2
    print(f'A soma do número {numero1} mais o número {numero2}, é {soma}')

2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

    numero = int(input('Digite um número: '))
    resto = numero%5
    print(f'O resto de {numero} divido por 5 é: {resto} ')

3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    multiplicacao = numero1 * numero2
    print(f'A multiplicação entre {numero1} e o número {numero2}, é {multiplicacao}')

4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    divisao = numero1 / numero2
    print(f'A divisão inteira entre {numero1} e o número {numero2}, é {int(divisao)}')
5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    numero = int(input('Digite um número: '))
    quadrado = numero**2
    print(f'O quadrado do {numero} é {quadrado}')


Números de Ponto Flutuante (float)
1-Escreva um programa que receba dois números flutuantes e realize sua adição.
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    soma = numero1 + numero2
    print(f'A soma do número {numero1} mais o número {numero2}, é {soma}')

2-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    media = (numero1 + numero2)/2
    print(f'A média entre {numero1} e o número {numero2}, é {media}')

3-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

4-Faça um programa que converta a temperatura de Celsius para Fahrenheit.
5-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

Strings (str)
Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
Escreva um programa que concatene duas strings fornecidas pelo usuário.

Booleanos (bool)
Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.


'''

#3-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = int(input('Digite a base para o cálculo da potencia: '))
expoente = int(input('Digite o expoente para o cálculo da potencia: '))
resultado = base**expoente
print(f'O resultado do {base} elevado a {expoente} potênca é: {resultado}')








