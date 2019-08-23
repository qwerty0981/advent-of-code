#!/usr/bin/python3

test = open("input", 'r')

total = 0

for line in test:
	if line[0] == "+":
		total += int(line[1:])
	elif line[0] == "-":
		total -= int(line[1:])
print("Total is :", total)
