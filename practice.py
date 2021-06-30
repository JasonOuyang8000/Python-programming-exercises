
import math
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 1 
def five_seven():
    n_list = []

    for n in range(2000,3201):
        if n % 7 == 0 and not n % 5 == 0:
            n_list.append(str(n))
    return ','.join(n_list)

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def integerMulti(n): 
    new_dict = {}
    for i in range(1, n + 1):
        new_dict[i] = i * i
    return new_dict


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


# def list_tuples(string):
#     l = string.split(',')
#     t = tuple(l)
#     print(t,l)

# list_tuples('2,4,5,6,7,14')


# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180



# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def twod(x,y):
    input_str = y
    dimensions=[int(x) for x in input_str.split(',')]
    rowNum=dimensions[0]
    colNum=dimensions[1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col

    return multilist

print(twod(3,'5'))

