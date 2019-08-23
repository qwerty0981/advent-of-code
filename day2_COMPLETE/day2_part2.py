#!/usr/bin/python3

def diff(id1, id2):
	return len(list(filter(lambda x: x is not 0, [ord(i1) ^ ord(i2) for i1,i2 in zip(id1, id2) ])))

data = [line.rstrip("\n") for line in open("input") ]

for id1 in data:
	for id2 in data:
		if diff(id1, id2) is 1:
			ans = ""
			for i in range(len(id2)):
				if id1[i] is id2[i]:
					ans += id1[i]
			print(ans)
			exit()
