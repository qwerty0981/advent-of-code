#!/usr/bin/python3

def parseLine(line):
	two = False
	three = False
	while line is not "":
		letter = line[0]
		c = line.count(letter)
		if c is 2:
			two = True
		elif c is 3:
			three = True
		line = line.replace(letter, "")
		if two and three:
			break
	return two, three


data = [line.rstrip("\n") for line in open("input")]

twos = 0
threes = 0

for d in data:
	istwo, isthree = parseLine(d)
	if istwo:
		twos += 1
	if isthree:
		threes += 1

print("Checksum:", twos * threes)

