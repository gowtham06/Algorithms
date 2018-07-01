
from LCA import Node
INT_MAX = 4294967296
INT_MIN = -4294967296
def isBST(root):
    return isBSTUtill(root)
def isBSTUtill(root,left_node=None,right_node=None):
    if root is None:
        return True
    if left_node is not None and root.key<left_node.key:
        return False
    if right_node is not None and root.key>right_node.key:
        return False
    return isBSTUtill(root.left,left_node,root) and isBSTUtill(root.right,root,right_node)

if __name__ == '__main__':
    print("To check for BST condition")
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print (isBST(root))