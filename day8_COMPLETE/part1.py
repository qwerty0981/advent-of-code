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


def sum_meta(n):
	total = 0
	if len(n["metadata"]) > 0:
		total += sum(n["metadata"])

	for nn in n["children"]:
		print(nn)
		total += sum_meta(nn)

	return total


numbers = list(map(int, open("input", 'r').read().strip().split()))
root, temp = parse_node(numbers)
print(sum_meta(root))
