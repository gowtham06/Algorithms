from bstConstrcution import Node
from bstConstrcution import in_order_traversal
from bstConstrcution import insert_node

def find_LCA(root,key_1,key_2):
    if(root==None):
        return None
    if(root.key==key_1 or root.key==key_2):
        return root
    left_LCA=find_LCA(root.left,key_1,key_2)
    right_LCA=find_LCA(root.right,key_1,key_2)
    if(left_LCA and right_LCA):
        return root
    if(left_LCA is None):
        return right_LCA
    if(right_LCA is None):
        return left_LCA

if __name__ == '__main__':
    print("To find the least common anchestor")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # in_order_traversal(root)
    print(find_LCA(root,4,5).key)
