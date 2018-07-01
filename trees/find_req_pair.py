from bstConstrcution import Node
from bstConstrcution import insert_node
from bstConstrcution import in_order_traversal
def find_pair_sum(root,item_list,required_sum,key_1,key_2):
    if(root is None):
        return key_1,key_2
    else:
        if(required_sum-root.key in item_list):

            find_flag=True
            key_1=root.key
            key_2=required_sum-root.key
            return key_1,key_2
        else:
            item_list.append(root.key)
            key_1,key_2=find_pair_sum(root.left,item_list,required_sum,key_1,key_2)
            key_1,key_2=find_pair_sum(root.right,item_list,required_sum,key_1,key_2)

        return key_1,key_2
    return  key_1,key_2
if __name__ == '__main__':
    print("To find a pair with required sum")
    root = None
    num_arr = [15, 10, 20, 8, 12, 16, 25]
    for item in num_arr:
        root = insert_node(root, item)
    required_sum=90
    key_1,key_2=find_pair_sum(root,[],required_sum,None,None)
    print(key_1,key_2)

