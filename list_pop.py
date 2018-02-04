
import timeit

pop0 = timeit.Timer('x.pop(0)', 'from __main__ import x')
pop1 = timeit.Timer('x.pop()', 'from __main__ import x')

x = list(range(2000000))
print(pop0.timeit(number=1000))

x = list(range(2000000))
print(pop1.timeit(number=1000))
