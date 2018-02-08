
# python实现Deque

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRight(self, item):
        self.items.append(item)

    def addLeft(self, item):
        self.items.insert(0,item)

    def removeRight(self):
        return self.items.pop()

    def removeLeft(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# d = Deque()
# print(d.isEmpty())
# d.addRight(43)
# d.addLeft('A')
# d.addRight('hello')
# d.addLeft(True)
# print(d.size())
# print(d.removeRight())
# print(d.removeLeft())

# 应用一： 回文问题


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addLeft(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeRight()
        last = chardeque.removeLeft()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))