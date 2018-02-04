import time

# 求和函数算法分析

def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end = time.time()

    return theSum, end-start

# 乱序字符串检查

def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def isluanxu(s1,s2):
	pos1 = 0
	isLuan = True

	while pos1 < len(s1) and isLuan:
		pos2 = 0
		found = False
		while pos2 < len(s2) and not found:
			if s1[pos1] == s2[pos2]:
				found = True
			else:
				pos2 = pos2 + 1

		if not found:
			isLuan = False
		pos1 = pos1 + 1
	return isLuan

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


def main():
	# for i in range(5):
	# 	print('sum is %d required %.7f seconds' % sumOfN2(100000))

	print(anagramSolution1('abcd','dcba'))
	print(isluanxu('abcd','dcbf'))
	print(anagramSolution4('abcd','cdba'))

if __name__ == '__main__':
	main()