import sys

class node(object):
    def __init__(self, index):
        self.children = []
        self.index = index
        self.degree = 0
    def addChild(self, index):
        self.children.append(index)

class graph(object):
	def __init__(self, nodes):
		self.nodes = nodes

#read a graph in -> return a tree
def read_file(path):
    nodes = []
    with open(path, "r") as file:
        maxIndex = -1
        for line in file.readlines():
            split1 = int(line.split(',')[0])
            split2 = int(line.split(',')[1])
            index = max(split1, split2)

            if(maxIndex < index):
                while maxIndex < index:
                    nodes.append(None)
                    maxIndex += 1

            if(nodes[split1] is None):
                nodes[split1] = node(split1)
            nodes[split1].addChild(split2)

            if(nodes[split2] is None):
                nodes[split2] = node(split2)
            nodes[split2].degree += 1

    g = graph(nodes)
    return g
            