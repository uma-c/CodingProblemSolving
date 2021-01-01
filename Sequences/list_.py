import sys

if __name__ == "__main__":
    lst1 = [i for i in range(5)]
    for idx, v in enumerate(lst1):
        print(idx, v)
    #-----------------------------
    if 4 in lst1:
        print(lst1.index(4))
    #-----------------------------
    lst2 = [[], ['1'], [1], [1, 2], ['1', '2']]
    print(sys.getsizeof(lst2))
    for item in lst2:
        print(item, sys.getsizeof(item))
    #-------------------------------------------
    lst3 = [['1', '2', '3']]
    lst3.extend(lst2)
    print(lst3)
    lst4 = lst3.copy()
    print(lst4)

    #------- Create matrix -------------
    rows, cols = 4, 3
    lst5 = [[0 for _ in range(cols)] for _ in range(rows)]
    lst5[2][1] = 1 # 3rd row, 2nd column
    print(lst5)

    # Wrong way, because references are copied
    lst6 = [[0] * cols] * rows
    lst6[2][1] = 1
    print(lst6)

    #----- Transpose matrix (rows -> cols, cols -> rows)
    lst5transpose = list(zip(*lst5))
    print(lst5transpose)
    #----------------------------------
    lst7 = [1, 2, 3] + [4, 5, 6]
    print(lst7)

    