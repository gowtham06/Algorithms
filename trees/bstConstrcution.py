class Node:
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(node,value):
    if(not node):
        node=Node(value)
        return node
    else:
        if(value>=node.key):
            node.right=insert_node(node.right,value)
        else:
            node.left=insert_node(node.left,value)
    return node

def in_order_traversal(root):
    if(not root):
        return
    else:
        in_order_traversal(root.left)
        print(root.key),
        print(","),
        in_order_traversal(root.right)
