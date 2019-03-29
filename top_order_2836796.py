import sys
import graph

def top_sort(g):
	if not g.nodes:
		return []
	v = []
	for node in g.nodes:
		if g.degrees[node.index] == 0:
			for childIndex in node.children:
				g.degrees[childIndex] -= 1
			v.append(node)
			g.nodes.remove(node)
			v+=top_sort(g)
			return v

def main():
	if(len(sys.argv) < 2):
		print("Usage: python top_order_2836796.py <input_n.txt>")
		sys.exit()
	sys.setrecursionlimit(10000)
	myGraph = graph.read_file(sys.argv[1]);
	sorted = top_sort(myGraph)

	for node in sorted:
		print(str(node.index)+' ', end='')

if __name__ == "__main__":
	main()