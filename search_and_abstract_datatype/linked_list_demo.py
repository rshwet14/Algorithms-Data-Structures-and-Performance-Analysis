class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    pass

node1 = Node(1)
print(node1)
