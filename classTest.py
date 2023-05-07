from Node import Node
from Way import Way

node1 = Node(1, 1)
node2 = Node(2, 1)
node3 = Node(1, 2)

nodeList = [node1, node2, node3]
way = Way(0, nodeList)

way.calculateLength()

print(way.length)