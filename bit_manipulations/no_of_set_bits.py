if __name__ == "__main__":
    n = 7
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1
    print(count)