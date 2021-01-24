if __name__ == "__main__":
    a, b = 2, 3
    a ^= b
    b ^= a
    a ^= b
    print(a, b)