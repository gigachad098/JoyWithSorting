class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.subtreelen = 1

    def addRight(self, right):
        self.right = right

    def addLeft(self, left):
        self.left = left