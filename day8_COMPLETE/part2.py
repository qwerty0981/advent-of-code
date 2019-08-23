#!/usr/bin/python3

def parse_node(num_list):
	node = {"children": [], "metadata":[], "count":(num_list[0],num_list[1])}
	num_list = num_list[2:]
	for n in range(node["count"][0]):
		new_node, num_list = parse_node(num_list)
		node["children"].append(new_node)

	for n in range(node["count"][1]):
		node["metadata"].append(num_list[0])
		num_list = num_list[1:]

	return node, num_list


def valueof_node(n):
	val = 0
	if len(n["children"]) == 0:
		val = sum(n["metadata"])
	else:
		limit = len(n["children"])
		for m in n["metadata"]:
			if m > limit:
				continue
			val += valueof_node(n["children"][m-1])
	return val


numbers = list(map(int, open("input", 'r').read().strip().split()))
root, temp = parse_node(numbers)
print(valueof_node(root))
