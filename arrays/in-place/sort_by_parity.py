from typing import List

def sortArrayByParity(A: List[int]) -> List[int]:
    e, o = 0, len(A) - 1
    while e < o:
        if A[e] % 2 != 0:
            A[e], A[o] = A[o], A[e]
            o -= 1
        else:
            e += 1
    return A

if __name__ == "__main__":
    A = [3,1,2,4]
    print(sortArrayByParity(A))