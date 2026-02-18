'''
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''
#range(start, stop, step)

#originalString = 'PYnative'

originalString = input('write a word: ')

print(f'Original String is {originalString}')

size = len(originalString)

print('Printing only even index chars')
for i in range(0, size-1, 2):
    print(originalString[i])
