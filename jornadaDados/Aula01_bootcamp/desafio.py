# 1) Solicite ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor de um salário
salario = float(input("Digite o seu salário: "))
# Converte a entrada para um número de ponto flutuante
# 3) Solicite ao usuário que digite o valor do bônus recebido
bonus = float(input("Digite o valor do bônus: "))
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
bonus_final = 1000 + salario * bonus
# 5) Imprime a mensagem personalizada incluindo o nome do usuário
print(f"O usuário {nome} possui o bonus de {bonus_final}")
