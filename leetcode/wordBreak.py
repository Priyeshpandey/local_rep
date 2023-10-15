import heapq

class Node:
    def __init__(self, nodeVal: str) -> None:
        self.val = nodeVal
        self.neighbors = []

    def addNeighbor(self, node: Node) -> None:
        self.neighbors.append(node)

    def removeNeighbor(self):
        pass

