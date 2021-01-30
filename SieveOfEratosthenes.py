'''
Finds primes in range [2, n]
Time complexity: O(n * loglogN), Space complexity: O(N)
'''
def get_no_of_primes(n:int) -> int:
    isPrime = [True for _ in range(n+1)]
    for i in range(2, n + 1):
        for j in range(i*i, n + 1, i):
            isPrime[j] = False

    count = 0
    for i in range(2, n + 1):
        count += isPrime[i]
    return count

if __name__ == "__main__":
    print(get_no_of_primes(100))