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

while not complete:
	data, complete = parse(data)

print("Best:", len(data))
