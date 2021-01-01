from collections import namedtuple

if __name__ == "__main__":
    tup = tuple()
    tup1 = ('crack',)
    tup2 = tuple('crack') # interpreted as tuple of list (string)
    print(tup, tup1, tup2)
    record = namedtuple("Computer_Science", "name id score")
    record1 = record('Bob', id=12345, score=56)
    print(record1)