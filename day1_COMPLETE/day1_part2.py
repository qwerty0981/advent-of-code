#!/usr/bin/python3

test = open("input", 'r')
lines = [int(line) for line in test]
total = 0
i = 0
ilen = len(lines)
seen = set()

while True:
	total += lines[i % ilen]

	if total in seen:
		break
	else:
		seen.add(total)
	i += 1

print("Total is :", total)
