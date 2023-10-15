from collections import defaultdict


class Graph:
    def __init__(self, edgeList):
        self.edge = defaultdict(list)
        for u, v in edgeList:
            self.edge[u].append(v)
            self.edge[v].append(u)

    def printGraph(self):
        print(self.edge)


if __name__=='__main__':
    edgeList = [[1,2],[2,3]]
    gp = Graph(edgeList)
    gp.printGraph()
