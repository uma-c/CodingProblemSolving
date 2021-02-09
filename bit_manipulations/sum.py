'''
11
10

^ = 01
& = 100 + 01
101 
'''
def sum_of_nums(a:int, b:int) -> int:
    if b == 0:
        return a
    if a == 0:
        return b
    return sum_of_nums(a ^ b, (a & b) << 1)

if __name__ == "__main__":
    print(sum_of_nums(2, 3))