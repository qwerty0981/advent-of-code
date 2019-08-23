#!/usr/bin/python3

import collections

line = open("input", 'r').read().strip().split()
player_count = int(line[0])
max_marble = int(line[6]) * 100

d = collections.deque()
players = [0 for i in range(player_count)]

for i in range(max_marble+1):
	if i % 23 != 0 or i == 0:
		d.rotate(-2)
		d.appendleft(i)
	else:
		players[i % player_count] += i
		d.rotate(7)
		players[i % player_count] += d.popleft()
print(max(players))
