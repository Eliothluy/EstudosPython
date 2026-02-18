'''
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. 
Otherwise, return their sum.
'''
# number1 = int(input('Write a first number: '))
# number2 = int(input('Write a second number: '))
# result1 = number1 * number2
# result2 = number1 + number2

# if result1 > 1000:
#     print(f'The result is {result2}')
# else:
#     print(f'The result is {result1}')


def sum_or_product(num1, num2):
    multiply = num1 * num2

    if multiply <= 1000:
        return multiply
    else:
        sum = num1 + num2
        return sum
    
number1 = int(input('Write a first number: '))
number2 = int(input('Write a second number: '))

print(f'Result is: {sum_or_product(number1, number2)}')
