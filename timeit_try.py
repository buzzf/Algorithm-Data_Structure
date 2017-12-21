import timeit

def test1():
	l = []
	for i in range(1000):
		l = l + [i]

def test2():
	l = []
	for i in range(1000):
		l.append(i)

def test3():
	l = [i for i in range(1000)]

def test4():
	l = list(range(1000))

def test5():
	pass

t1 = timeit.timeit(stmt='test1()', setup='from __main__ import test1', number=1000)
print('concat ', t1, 'ms')

t2 = timeit.timeit(stmt='test2()', setup='from __main__ import test2', number=1000)
print('append ', t2, 'ms')

t3 = timeit.timeit(stmt='test3()', setup='from __main__ import test3', number=1000)
print('comprehension ', t3, 'ms')

t4 = timeit.timeit(stmt='test4()', setup='from __main__ import test4', number=1000)
print('list range ', t4, 'ms')

t5 = timeit.timeit(stmt='test5()', setup='from __main__ import test5', number=1000)
print('none func ', t5, 'ms')


