#!/usr/bin/python3

data = [[0] * 1000 for x in range(1000)]

for line in open("input", 'r'):
	values = line.strip().split(" ")
	offset = values[2][:-1].split(",")
	dim = values[3].split("x")
	print(dim)
	for x in range(int(offset[0]), int(offset[0]) + int(dim[0])):
		for y in range(int(offset[1]), int(offset[1]) + int(dim[1])):
			print("Updating: x:", x, "y:", y)
			data[x][y] += 1

total = 0
for x in range(1000):
	for y in range(1000):
		if data[x][y] > 1:
			total += 1
print(total)
	
