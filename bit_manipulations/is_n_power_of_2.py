def is_power_of_2(n:int) -> bool:
    return n & (n - 1) == 0

if __name__ == "__main__":
    print(is_power_of_2(20))
    print(is_power_of_2(16))