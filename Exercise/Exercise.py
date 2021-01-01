'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def question1_gen(start, end):
    # find 1st number that is divisible by 7
    s1 = start - 1
    s2 = s1 + 7 - (s1 % 7)
    #print(s2)
    for i in range(s2, end, 7):
        if i % 5 == 0:
            continue
        yield i

def question1():
    print(*(i for i in question1_gen(2000, 3201)), sep = ",")

'''
Write a program which can compute the factorial of a given numbers.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''
def factorial(x):
    if x == 1:
        return 1;   

    return x * factorial(x-1)

from functools import reduce
def question2():
    #print(factorial(8))
    print(reduce(lambda factorial, x: factorial * x, range(1, 9)))

#question2()

'''
What is the most efficient way to remove half of the duplicate items in a list. 
For example to go from l = [1, 8, 8, 8, 1, 3, 3, 8] to k=[1,8,8,3]
'''
def remove_half_duplicates(items):
    counter = {}
    li = []
    for i in items:
        if not counter.get(i):
            counter[i] = 1
        else:
            counter[i] += 1

    for key in counter.keys():
        while counter[key] > 0 and counter[key] % 2 == 0:
            li.append(key)
            counter[key] -= 2
    return li

print(remove_half_duplicates([1, 8, 8, 8, 1, 3, 3, 8]))