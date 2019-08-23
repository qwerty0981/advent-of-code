#!/usr/bin/python3

def parse(line):
	values = line.split(" ")
	time = int(values[1][:-1].split(":")[1])
	text = ' '.join(values[2:]).strip()
	return {"time": time, "text": text}

data = []
lines = [l.strip() for l in open("input", 'r') ]
lines.sort()
data = list(map(parse, lines))

guard_id = ""
temp_time = ""
guard_data = dict()
guard_entries = dict()
for entry in data:
	if entry["text"].startswith("Guard"):
		guard_id = entry["text"].split(" ")[1]
		if guard_id not in guard_data:
			guard_data[guard_id] = 0
		if guard_id not in guard_entries:
			guard_entries[guard_id] = []
	elif entry["text"] == "falls asleep":
		temp_time = entry["time"]
		guard_entries[guard_id].append(entry)
	elif entry["text"] == "wakes up":
		guard_data[guard_id] += entry["time"] - temp_time
		guard_entries[guard_id].append(entry)

maxval = 0
maxk = ""
for k,v in guard_data.items():
	if v > maxval:
		maxval = v
		maxk = k

asleep = [0 for x in range(60)]
for e in guard_entries[maxk]:
	if e["text"] == "falls asleep":
		temp_time = e["time"]
	elif e["text"] == "wakes up":
		for i in range(temp_time, e["time"]):
			asleep[i] += 1
print("Guard ID:", maxk)
print(asleep.index(max(asleep)) * int(maxk[1:]))
