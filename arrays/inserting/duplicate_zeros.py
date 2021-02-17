from typing import List

def duplicateZeros(arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        write_pos, n = -1, len(arr)
        for num in arr:
            if num == 0:
                write_pos += 1
            write_pos += 1
        if write_pos == n - 1:
            return
        for read_pos in range(n - 1, -1, -1):
            if write_pos < n:
                arr[write_pos] = arr[read_pos]
            write_pos -= 1
            if arr[read_pos] == 0:
                if write_pos < n:
                    arr[write_pos] = arr[read_pos]
                write_pos -= 1

if __name__ == "__main__":
    #arr = [8,5,0,9,0,3,4,7]
    arr = [8,4,5,0,0,0,0,7]
    duplicateZeros(arr)
    print(arr)