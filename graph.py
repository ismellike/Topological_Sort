import sys

class node(object):
    def __init__(self, index):
        self.children = []
        self.index = index
    def addChild(self, index):
        self.children.append(index)

class graph(object):
	def __init__(self, nodes, degrees = None):
		self.nodes = nodes
		if degrees == None:
			self.degrees = []
			for i in range(len(nodes)):
				self.degrees.append(0)
		else:
			self.degrees = degrees
	def setDegrees(self):
		for n in self.nodes:
			for cIndex in n.children:
				self.degrees[cIndex] += 1

#read a graph in -> return a tree
def read_file(path):
    nodes = []
    with open(path, "r") as file:
        index = -1
        node_i = None
        for line in file.readlines():
            split1 = int(line.split(',')[0])
            split2 = int(line.split(',')[1])
            if(index == split1):
                node_i.addChild(split2)
            else:
                #previous node needs to be appended
                if(index != -1):
                    nodes.append(node_i)

				#check for leaf nodes
                if(index + 1 != split1):
                    while index + 1 < split1:
                         index += 1
                         nodes.append(node(index))

                index = split1
                node_i = node(split1)
                node_i.addChild(split2)
        #add last node
        nodes.append(node_i)
    g = graph(nodes)
    g.setDegrees()
    return g
            