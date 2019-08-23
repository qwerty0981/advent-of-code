#!/usr/bin/python3
from operator import add
from functools import reduce

coords = [ list(map(int, l.strip().split(", "))) for l in open("input", 'r') ]

minx = min(map(lambda x: x[0], coords))
miny = min(map(lambda x: x[1], coords))
maxx = max(map(lambda x: x[0], coords))
maxy = max(map(lambda x: x[1], coords))

count = 0

for x in range(minx, maxx+1):
	for y in range(miny, maxy+1):
		dists = list(map(lambda z: abs(x - z[0]) + abs(y - z[1]), coords))
		total = reduce(add, dists, 0)
		if total < 10000:
			count += 1
print(count)
