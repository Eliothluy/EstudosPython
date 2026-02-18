'''
Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
'''
previous_num = 0
for number in range(0, 10):
    sum = previous_num + number
    print(f'Current Number {number} Previous Number {previous_num} Sum: {sum}')
    previous_num = number
