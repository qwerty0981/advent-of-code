#!/usr/bin/python3
import functools

foldr = lambda func, acc, xs: functools.reduce(lambda x,y: func(y, x), xs[::-1], acc)

def step(x, y):
	if len(y) == 0:
		return x
	if abs(ord(x) - ord(y[0])) == 32:
		return y[1:]
	else:
		return x + y

data = open("input", 'r').read().strip()

minval = (1000000000000000, "")

for char in "abcdefghijklmnopqrstuvwxyz":
	complete = False
	temp = data.replace(char, "")
	temp = temp.replace(char.upper(), "")
	temp = foldr(step, "", temp)
	if len(temp) < minval[0]:
		minval = (len(temp), char)

print("Best:", minval)
