#!/usr/bin/python3

pairs = [ list(map(int, l.strip().split(", "))) for l in open("input", 'r') ]

pairTouples = list(map(lambda x: (x[0], x[1]), pairs))
minx = min(map(lambda x: x[0], pairs))
miny = min(map(lambda x: x[1], pairs))
maxx = max(map(lambda x: x[0], pairs))
maxy = max(map(lambda x: x[1], pairs))

points = dict()
for p in pairTouples:
	points[p] = (0, False)


for x in range(minx, maxx+1):
	for y in range(miny, maxy+1):
		dist = list(map(lambda z: {"dist": abs(x-z[0]) + abs(y-z[1]), "point": (z[0], z[1])}, pairs))
		minDist = min(dist, key=lambda z: z["dist"])
		distancesAtMin = list(filter(lambda z: z == minDist["dist"], dist))
		if len(distancesAtMin) > 1:
			continue
		if x == 0 or x == maxx or y == 0 or y == maxy:
			points[minDist["point"]] = (points[minDist["point"]][0], True)
		points[minDist["point"]] = (points[minDist["point"]][0] + 1, points[minDist["point"]][1])

noInf = list(filter(lambda x: x[1] == False, list(map(points.get, points))))
print(noInf)
maxPoint = max(noInf, key=lambda x: x[0])
print("Max point is with size of:", maxPoint[0])

print((maxx-minx) * (maxy-miny))
