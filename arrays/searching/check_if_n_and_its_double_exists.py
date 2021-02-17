from typing import List

def check_if_exists_num_and_its_double(arr:List[int]) -> bool:
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and (num // 2) in seen):
            return True
        else:
            seen.add(num)
    return False

if __name__ == "__main__":
    print(check_if_exists_num_and_its_double([10, 2, 5, 3]))