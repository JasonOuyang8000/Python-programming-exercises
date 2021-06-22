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
