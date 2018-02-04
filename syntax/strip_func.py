#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
	if(len(s)>0):
		l = list(s)
		while(l[0]==' '):
			l.remove(l[0])
			if len(l) == 0:
				break
		s = ''.join(l)
		if len(l)>1:
			while(l[-1]==' '):
				l.remove(l[-1])
		s = ''.join(l)
	return s


s1 = ''
s2 = ' l'
s3 = 'm'
s4 = 'd '
s5 = ' 3 '
s6 = '  '
s7 = '  n  '

print(trim(s1))
print(trim(s2))
print(trim(s3))
print(trim(s4))
print(trim(s5))
print(trim(s6))
print(trim(s7))


