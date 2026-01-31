'''
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. 
Otherwise, return their sum.
'''

number1 = int(input('Write a first number: '))
number2 = int(input('Write a second number: '))
result1 = number1 * number2
result2 = number1 + number2

if result1 > 1000:
    print(f'The result is {result2}')
else:
    print(f'The result is {result1}')
