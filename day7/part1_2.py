#!/usr/bin/python3

import networkx as nx

def solve(lines):
	graph = nx.DiGraph()
	for line in lines:
		vals = line.split(" ")
		graph.add_edge(vals[1], vals[7])
	print(''.join(nx.lexicographical_topological_sort(graph)))

solve(open("input", 'r').readlines())
