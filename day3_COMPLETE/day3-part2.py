#!/usr/bin/python3

data = [[0] * 1000 for x in range(1000)]

for line in open("input", 'r'):
	values = line.strip().split(" ")
	offset = values[2][:-1].split(",")
	dim = values[3].split("x")
	for x in range(int(offset[0]), int(offset[0]) + int(dim[0])):
		for y in range(int(offset[1]), int(offset[1]) + int(dim[1])):
			data[x][y] += 1

for line in open("input", 'r'):
	values = line.strip().split(" ")
	offset = values[2][:-1].split(",")
	dim = values[3].split("x")
	safe = True
	for x in range(int(offset[0]), int(offset[0]) + int(dim[0])):
		for y in range(int(offset[1]), int(offset[1]) + int(dim[1])):
			if data[x][y] is not 1:
				safe = False
	if safe:
		print(values[0])
		exit()
