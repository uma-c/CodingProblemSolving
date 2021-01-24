def multiply(num1:str, num2:str) -> str:
    ans = ['0'] * (len(num1) + len(num2))
    m = -1
    for i in range(len(num2) - 1, -1, -1):        
        n = m
        for j in range(len(num1) - 1, -1, -1):
            part = (ord(num1[j]) - ord('0')) * (ord(num2[i]) - ord('0'))  
            p = n
            carry_over = 0
            while part != 0:
                digit = part % 10
                part //= 10
                pos_digit = ord(ans[p]) - ord('0') + digit + carry_over
                ans[p] = str(pos_digit % 10)
                carry_over = pos_digit // 10
                p -= 1
            while carry_over > 0:
                pos_digit = ord(ans[p]) - ord('0') + carry_over
                ans[p] = str(pos_digit % 10)
                carry_over = pos_digit // 10
                p -= 1
            n -= 1
        m -= 1
    leading_0s = 0
    for c in ans:
        if c == '0':
            leading_0s += 1
        else:
            break
    if leading_0s == len(ans):
        return '0'
    return ''.join(ans[leading_0s:])

if __name__ == "__main__":
    # print(multiply('43', '125'))
    # print(multiply('123', '456'))
    print(multiply('999', '999'))