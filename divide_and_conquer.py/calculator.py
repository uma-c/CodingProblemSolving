def atoi(s:str) -> int:
    result = 0
    for c in s:
        result = 10 * result + ord(c) - ord('0')
    return result

class BinaryOperators:
    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

class Calculator:
    def __init__(self):
        pass

    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        for j, c in enumerate(s):            
            if c == ' ' or c == '/' or c == '*' or c == '+' or c == '-' or c == '(' or  c== ')':
                operand = atoi(s[i:j])
                stack.append(operand)
                if c != ' ':
                    stack.append(c)
                i = j + 1
        print(stack)

if __name__ == "__main__":
    #print(atoi('458'))
    calc = Calculator()
    calc.calculate('2 + (3 -4/2 + 1)')