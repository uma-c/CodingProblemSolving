def addBinary(a: str, b: str) -> str:
    def add(c1, c2, c):
        if c1 == '0' and c2 == '0':
            return [c, '0']
        elif c1 == '1' and c2 == '1':
            return [c, '1']
        elif c1 == '1' or c2 == '1':
            if c == '1':
                return ['0', '1']
            else:
                return ['1', '0']
    result = []
    i, j = len(a) - 1, len(b) - 1
    c = '0'
    while i >= 0 and j >= 0:
        d, c = add(a[i], b[j], c)
        result.append(d)
        i -= 1
        j -= 1
    while i >= 0:
        d, c = add(a[i], '0', c)
        result.append(d)
        i -= 1
    while j >= 0:
        d, c = add('0', b[j], c)
        result.append(d)
        j -= 1
    if c == '1':
        result.append('1')
    result.reverse()
    return ''.join(result)

def addBinary(a: str, b: str) -> str:
    return '{0:b}'.format(int(a, 2) + int(b, 2)) 

if __name__ == "__main__":
    # a = "11"
    # b = "1"
    a = "1010"
    b = "1011"
    print(addBinary(a, b))