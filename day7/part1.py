#!/usr/bin/python3

from functools import reduce

def parse(line):
	vals = line.split()
	return {"name": vals[1], "pre": vals[7]}

def shrink(val, x):
	val[x["name"]].append(x["pre"])
	return val

steps = [ parse(l) for l in open("input", 'r') ]
tree = dict()
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	tree[char] = []
tree = reduce(shrink , steps, tree)
out = ""
done = False
while not done:
	minv = 1000000
	for k, v in tree.items():
		minv = min(minv, len(v))
	
	minvals = [ (key, val) for key, val in tree.items() if len(val) == minv]
	first = None
	if len(minvals) > 1:
		mins = list(map(lambda x: min(x[1]) if len(x[1]) > 0 else x[0], minvals))
		first = min(mins)
	elif len(minvals) == 1:
		if len(minvals[0][1]) != 0:
			first = min(minvals[0][1])
		else:
			first = minvals[0][0]
	out += first
	for k, v in tree.items():
		if first in v:
			tree[k].remove(first)
	tree.pop(first, None)
	if len(tree.keys()) == 0:
		done = True

print(out)
