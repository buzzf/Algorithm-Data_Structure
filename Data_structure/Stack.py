class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

# 栈测试

# s = Stack()
# print(s.isEmpty())
# s.push('a')
# print(s.peek())
# s.push(4)
# s.push(True)
# print(s.isEmpty())
# s.push(8.6)
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# del s

# 应用一：符号匹配

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
# print(parChecker('((()))'))
# print(parChecker('((()'))
# print(parChecker('())'))


def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            top = s.pop()
            if not matches(top,symbol):
                balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

# print(parChecker2('{{([][])}()}'))
# print(parChecker2('[{()]'))

# 应用二：十进制转换成二进制

def divideBy2(decNumber):
    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())

    return binString

# print(divideBy2(58))

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString

# print(baseConverter(25,2))
# print(baseConverter(25,16))
# print(baseConverter(25,8))

# 应用三： 中缀表达式转换为后缀表达式

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()  # 用于保存运算符
    postfixList = []   # 输出列表
    tokenList = infixexpr.split()  # 输入的中缀字符串标记列表

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G 

# 计算后缀表达式

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))