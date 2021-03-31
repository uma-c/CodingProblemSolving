'''
Recursion approach
'''
def fib(n: int):
    cache = {}
    def recur_fib(n: int):
        if n in cache:
            return cache[n]
        if n < 2:
            return n
        result = recur_fib(n - 1) + recur_fib(n - 2)
        cache[n] = result
        return result
    return recur_fib(n) 

def fib1(n: int):
    if n < 2:
        return n
    prev, result = 0, 1
    for i in range(1, n):
        prev, result = result, prev + result
    return result

if __name__ == "__main__":
    print(fib1(7)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55