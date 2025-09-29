import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            root = self.root
            while True:
                if root.data > node.data:
                    if root.left is None:
                        root.left = node
                        break
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = node
                        break
                    else:
                        root = root.right

nodes = []
while True:
    try:
        nodes.append(Node(int(input())))
    except:
        break

tree = Tree()
for node in nodes:
    tree.insert(node)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

postorder(tree.root)
