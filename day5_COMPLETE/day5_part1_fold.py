#!/usr/bin/python3

import functools
import operator

foldr = lambda func, acc, xs: functools.reduce(lambda x,y: func(y, x), xs[::-1], acc)

def step(x, y):
	if len(y) == 0:
		return x
	if abs(ord(x) - ord(y[0])) == 32:
		return y[1:]
	else:
		return x + y

data = open("input", 'r').read().strip()

print(len(foldr(step, "", data)))
