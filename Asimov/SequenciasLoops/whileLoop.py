n = 0

# while n < 3:
#     print(f'O valor de n é: {n}')
#     n = n+1


#Uso do Break

while n < 10:
    print(f'O valor de n é: {n}')
    n += 1
    if n == 5:
        break


#loop infinito

while True:
    entrada = input('Digite qualquer coisa (q para sair) ')
    print(f'O valor digitado foi: {entrada}')
    if entrada == 'q':
        break

print('Programa finalizado')
