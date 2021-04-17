from typing import List

def generate(numRows: int) -> List[List[int]]:
    tr = [[1]]
    prev_row = tr[0]
    for r in range(2, numRows + 1):
        new_row = []
        for c in range(r):
            if c == 0 or c == r - 1:
                new_row.append(1)
            else:
                new_row.append(prev_row[c - 1] + prev_row[c])
        prev_row = new_row
        tr.append(new_row)
    return tr

if __name__ == "__main__":
    print(generate(5))