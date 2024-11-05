import sys

class node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(root):
    if root == None:
        return
    print(root, end="")
    pre_order(tree[root].left)
    pre_order(tree[root].right)

def in_order(root):
    if root == None:
        return
    in_order(tree[root].left)
    print(root,end = "")
    in_order(tree[root].right)

def post_order(root):
    if root == None:
        return
    post_order(tree[root].left)
    post_order(tree[root].right)
    print(root,end="")

N = int(sys.stdin.readline())

tree = {}
for i in range(N):
    data, left, right = sys.stdin.readline().split()
    if left == '.':
        left = None
    if right =='.':
        right = None
    tree[data] = node(data,left,right)


pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()


