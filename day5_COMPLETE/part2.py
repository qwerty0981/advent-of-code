#!/usr/bin/python3

def parse(line):
	out = ""
	done = True
	ignore = False
	for i in range(len(line)-1, -1, -1):
		if ignore:
			ignore = False
			continue
		if abs(ord(line[i]) - ord(line[i-1])) == 32:
			ignore = True
			done = False
		else:
			out = line[i] + out
	return out, done

data = open("input", 'r').read().strip()
complete = False

minval = (1000000000000000, "")

for char in "abcdefghijklmnopqrstuvwxyz":
	complete = False
	print("Trying:", char)
	temp = data.replace(char, "")
	temp = temp.replace(char.upper(), "")
	while not complete:
		temp, complete = parse(temp)
	if len(temp) < minval[0]:
		minval = (len(temp), char)

print("Best:", minval)
